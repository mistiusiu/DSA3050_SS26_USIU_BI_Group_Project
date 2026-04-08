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
        # e.g., 'project-setup' + '../assets/logo.png' -> 'assets/logo.png'
        rel_to_docs = os.path.normpath(os.path.join(original_subdir, path))
        
        # Now create the full path from the project root where the script runs
        # This ensures \includegraphics gets a path it can actually reach
        final_path = os.path.join(docs_dir, rel_to_docs)
        
        if is_cover:
            # Use raw LaTeX for the cover image to avoid "Figure 1" label
            # Using \includegraphics directly avoids the 'figure' environment entirely
            return f'\\begin{{center}}\\includegraphics[width=0.5\\textwidth]{{{final_path}}}\\end{{center}}'
        
        return f"![{alt_text}]({final_path})"

    return re.sub(r'!\[(.*?)\]\((.*?)\)', path_resolver, text)

def bold_titles(text):
    """
    Finds Markdown headers (e.g., # Title) and wraps the text in bold syntax.
    Handles headers with and without unnumbered tags {-}.
    """
    # Regex finds the hashes, the title content, and optional trailing tags
    # It wraps the title content in **bold**
    return re.sub(r'^(#+)\s*(.*?)\s*({-}|{.unnumbered})?$', r'\1 **\2** \3', text, flags=re.MULTILINE)

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
        "dashboard/insights.md",
        "deployment/service-links.md"
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
                            
                            # 1. Start Title Page
                            outfile.write("```{=latex}\n\\begin{titlepage}\n\\pagenumbering{gobble}\n\\centering\n\\vspace*{\\fill}\n```\n\n")
                            
                            # Add {-} to headers to keep them out of TOC
                            content = re.sub(r'^(#+.*)', r'\1 {-}', content, flags=re.MULTILINE)
                            # Bold the title on the cover page
                            content = bold_titles(content)
                            
                            outfile.write(content)
                            
                            # 2. End Title Page and manually trigger TOC AFTER the cover
                            outfile.write("\n\n```{=latex}\n\\vspace*{\\fill}\n\\end{titlepage}\n")
                            outfile.write("\\clearpage\n\\pagenumbering{roman}\n\\tableofcontents\n\\clearpage\n")
                            outfile.write("\\pagenumbering{arabic}\n\\setcounter{page}{1}\n\\setcounter{figure}{0}\n```\n")
                        else:
                            content = fix_image_paths(content, docs_dir, subdir, is_cover=False)
                            # Apply bold formatting to all headers in regular files
                            content = bold_titles(content)
                            outfile.write(f"\n\n{content}\n\n")
                else:
                    print(f"Warning: {relative_path} not found.")

        # Note: --toc is removed from pandoc_command because we inserted it manually via LaTeX
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
            # graphicx is usually loaded by pandoc but explicitly adding it for safety
            h.write("\\usepackage{graphicx}\n")

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
