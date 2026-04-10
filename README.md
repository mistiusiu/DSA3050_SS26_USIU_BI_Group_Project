![USIU Logo Color](docs/assets/usiu-logo-color.png)

# Social Media Business Intelligence

## Data Sources

Dataset: [DMO Social Media Engagement Dataset](https://www.kaggle.com/datasets/jocelyndumlao/dmo-social-media-engagement-dataset)


![Kaggle DMO Social Media Engagement Dataset](docs/assets/kaggle_data_source.png)

Primary Source: [DMO Social Media Engagement Dataset](https://data.mendeley.com/datasets/bfk3hvdcnt/1)

![Mendley DMO Social Media Engagement Dataset](docs/assets/mendley_data_source.png)

This dataset contains 21,677 tweets collected from 23 Destination Marketing Organizations (DMOs) between March 25, 2019 and January 31, 2022. It was created to study how social media content strategies and linguistic features affect user engagement on Twitter.

## Initializing the Documentation

The documentation uses Material for MkDocs and a custom Python script that knits the MkDocs documentation into a PDF report using pandoc (and LaTeX installed on the host machine).

### Environment Configuration

Setup a Python virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the requirements and their dependencies.

```bash
pip install -r requirements.txt
```

### Documentation in Development

Display the documentation in a development server.

```bash
mkdocs serve
```

### Documentation in Production

Build the documentation into a site folder ready to be served by a web server (like NGINX).

```bash
mkdocs build
```

This repository uses a CI/CD that builds and deploys to GitHub Pages.

## Contributors

Vivian Kipsang - Problem Definition  
Misati Nyambane - ETL & Power Query  
Trizah Nzioka - DAX Measures   
Samantha Masaki - Data Architecture   
Levin Ekuam - Visualization & Business Insights  
Ilham Mohammed - Visualization & Business Insights  



