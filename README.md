# LinkedinJobs

Scraping selected LinkedIn job information, summarizing them using OpenAI API, and adding data to Airtable.

## 1. Overview
This project aims to automate the process of scraping job information from LinkedIn, extracting relevant details, generating role summaries and required skills/tools using the OpenAI API, and storing the data in an Airtable database. The provided scripts facilitate seamless web scraping, data processing, and integration with external APIs.

## 2. Project Structure

````
project/
├── main.py
├── airtable_api_functions.py
├── openai_api_functions.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
````
Here's a brief explanation of each file in the project:

**main.py**: This file contains the main script of the project. It interacts with the LinkedIn website, scrapes job information, and uses functions from other modules to process and store the data.

**airtable_api_functions.py**: This file contains functions related to interacting with the Airtable API. It includes a function to add a new job entry to the specified Airtable table.

**openai_api_functions.py**: This file contains functions related to interacting with the OpenAI API. It includes functions to generate summarized outputs for job roles, requirements, and a list of skills and tools required for a job.

**config.py**: This file stores the configuration variables used in the project, such as the Airtable API key, LinkedIn credentials, OpenAI API key, and other settings. You should fill in the appropriate values in this file before running the project.

**requirements.txt**: This file lists the Python packages and their versions required for the project. It includes packages like pyairtable, selenium, beautifulsoup4, openai, and webdriver_manager. You can install these dependencies using the pip install -r requirements.txt command.

**.gitignore**: This file specifies the files and directories that should be ignored by Git version control. In this case, the config.py file is added to the .gitignore file to prevent sensitive information from being committed to a repository.