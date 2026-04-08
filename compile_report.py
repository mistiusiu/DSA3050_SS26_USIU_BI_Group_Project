import subprocess
import os
import re
import argparse

def fix_image_paths(text, docs_dir, original_subdir, is_cover=False):
    """
    Converts relative paths like ../assets/img.png to a path that
    is relative to the execution root or absolute, ensuring LaTeX can find it.
    """
    def path_resolver(match):
        alt_text = match.group(1)
        path = match.group(2)
        
        # Calculate the path relative to the root docs directory
        rel_to_docs = os.path.normpath(os.path.join(original_subdir, path))
        
        # Now create the full path from the project root where the script runs
        final_path = os.path.join(docs_dir, rel_to_docs)
        
        if is_cover:
            # Use raw LaTeX for the cover image to avoid "Figure 1" label
            # Auto-scaled for the cover page specifically
            return f'\\begin{{center}}\\includegraphics[width=0.6\\textwidth,height=0.4\\textheight,keepaspectratio]{{{final_path}}}\\end{{center}}'
        
        return f"![{alt_text}]({final_path})"

    return re.sub(r'!\[(.*?)\]\((.*?)\)', path_resolver, text)

def bold_titles(text):
    """
    Finds Markdown headers (e.g., # Title) and wraps the text in bold syntax.
    Handles headers with and without unnumbered tags {-}.
    """
    return re.sub(r'^(#+)\s*(.*?)\s*({-}|{.unnumbered})?$', r'\1 **\2** \3', text, flags=re.MULTILINE)

def force_image_placement(text):
    """
    Wraps standard Markdown image syntax in a raw LaTeX block that 
    forces the [H] (HERE) placement and applies automatic scaling limits.
    """
    def float_fixer(match):
        alt = match.group(1)
        path = match.group(2)
        # Using a raw LaTeX figure block with [H] forces 'Here' placement.
        # keepaspectratio ensures it doesn't look 'washed out' or stretched.
        # height=0.5\textheight prevents it from taking up the whole page if vertical.
        return (
            f"\\begin{{figure}}[H]\n"
            f"\\centering\n"
            f"\\includegraphics[width=\\textwidth,height=0.5\\textheight,keepaspectratio]{{{path}}}\n"
            f"\\caption{{{alt}}}\n"
            f"\\end{{figure}}"
        )
    
    return re.sub(r'!\[(.*?)\]\((.*?)\)', float_fixer, text)

def knit_business_report(docs_dir):
    base_path = os.path.abspath(os.getcwd())
    output_dir = os.path.join(base_path, "report")
    output_file = os.path.join(output_dir, "BI_Project_Report.pdf")
    temp_combined_md = os.path.join(base_path, "temp_combined_report.md")
    
    ordered_files = [
        "cover_page.md",
        "index.md",
        "project-setup/problem-statement.md",
        "project-setup/data-dictionary.md",
        "power-query/transformations.md",
        "data-modeling/star-schema.md",
        "dax-development/measures.md",
        "dax-development/logic-deep-dive.md",
        "dashboard/visuals-design.md",
        "dashboard/insights.md"
    ]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(temp_combined_md, "w", encoding="utf-8") as outfile:
            for i, relative_path in enumerate(ordered_files):
                full_path = os.path.join(docs_dir, relative_path)
                
                if os.path.exists(full_path):
                    with open(full_path, "r", encoding="utf-8") as infile:
                        content = infile.read()
                        subdir = os.path.dirname(relative_path)
                        
                        if relative_path == "cover_page.md":
                            content = fix_image_paths(content, docs_dir, subdir, is_cover=True)
                            
                            # Start Title Page
                            outfile.write("```{=latex}\n\\begin{titlepage}\n\\pagenumbering{gobble}\n\\centering\n\\vspace*{\\fill}\n```\n\n")
                            
                            content = re.sub(r'^(#+.*)', r'\1 {-}', content, flags=re.MULTILINE)
                            content = bold_titles(content)
                            
                            outfile.write(content)
                            
                            # End Title Page and trigger TOC
                            outfile.write("\n\n```{=latex}\n\\vspace*{\\fill}\n\\end{titlepage}\n")
                            outfile.write("\\clearpage\n\\pagenumbering{roman}\n\\tableofcontents\n\\clearpage\n")
                            outfile.write("\\pagenumbering{arabic}\n\\setcounter{page}{1}\n\\setcounter{figure}{0}\n```\n")
                        else:
                            # 1. Resolve paths
                            content = fix_image_paths(content, docs_dir, subdir, is_cover=False)
                            # 2. Bold the titles
                            content = bold_titles(content)
                            # 3. Force images to stay "HERE" [H] and apply scaling
                            content = force_image_placement(content)
                            
                            outfile.write(f"\n\n{content}\n\n")
                else:
                    print(f"Warning: {relative_path} not found.")

        pandoc_command = [
            "pandoc",
            temp_combined_md,
            "--pdf-engine=xelatex",
            f"--resource-path={docs_dir}",
            "-V", "mainfont=Times New Roman",
            "-V", "geometry:margin=1in",
            "-V", "linestretch=1.5",
            "-V", "fontsize=12pt",
            "--number-sections",
            "--include-in-header", "header.tex",
            "-o", output_file
        ]

        with open("header.tex", "w") as h:
            h.write("\\usepackage{graphicx}\n")
            h.write("\\usepackage{float}\n") # Required for [H] placement
            h.write("\\floatplacement{figure}{H}\n") # Global fallback to 'Here'

        print("Knitting BI Report...")
        subprocess.run(pandoc_command, check=True)
        print(f"Success! Report generated at: {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error during Pandoc execution: {e}")
    finally:
        if os.path.exists(temp_combined_md):
            os.remove(temp_combined_md)
        if os.path.exists("header.tex"):
            os.remove("header.tex")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Knit BI Project docs to PDF.")
    parser.add_argument("docs_dir", help="The path to your /docs folder.")
    args = parser.parse_args()
    knit_business_report(args.docs_dir)
