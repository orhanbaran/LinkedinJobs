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


## Installation and Usage

To use this project, follow the steps below:

1. Clone the repository to your local machine using the following command:
   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```
   cd project
   ```

3. Create a virtual environment to isolate the project dependencies. Run the following command to create and activate a virtual environment:

   For Windows:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   For macOS and Linux:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the project dependencies by running the following command:
   ```
   python setup.py install
   ```

   This will use the `setup.py` file to install the required packages listed in the `requirements.txt` file.

5. Update the `config.py` file with your own configuration details. Replace the placeholder values with your **Airtable API key, LinkedIn credentials, OpenAI API key, and other settings**.

6. Run the following command to start the job scraping process:
   ```
   python main.py
   ```

   This command will prompt you to enter the LinkedIn job listing link. The script will open a web browser, log into your LinkedIn account, scrape the job information, generate summaries using the OpenAI API, and add the data to your specified Airtable table.

   **Note:** Make sure you have a stable internet connection during the process.

7. Review the output and verify that the job information has been added to your Airtable table.

Once you have finished using the project, you can deactivate the virtual environment by running the following command:
```
deactivate
```

By following these steps, you should be able to set up and run the project successfully. If you encounter any issues, make sure you have provided the correct configuration details and that the required dependencies are installed properly.
## 4. Configuration

Before running the project, make sure to update the config.py file with your own configuration details. The config.py file contains various settings and API keys required for the project to function correctly. Here's a breakdown of the configuration variables:

**Airtable API Key**: Replace YOUR_AIRTABLE_API_KEY with your Airtable API key. This key authorizes access to your Airtable account and allows the project to interact with your specified Airtable table.

**Airtable Base ID**: Replace YOUR_AIRTABLE_BASE_ID with the ID of your Airtable base. This ID identifies the specific base where you want to store the job data.

**Airtable Table Name**: Replace YOUR_AIRTABLE_TABLE_NAME with the name of the table in your Airtable base where you want to store the job data.

**LinkedIn Credentials**: Replace YOUR_LINKEDIN_USERNAME and YOUR_LINKEDIN_PASSWORD with your LinkedIn account credentials. These credentials are used to log into your LinkedIn account and access the job listings.

**OpenAI API Key**: Replace YOUR_OPENAI_API_KEY with your OpenAI API key. This key allows the project to utilize the OpenAI API for generating job role summaries, requirements, andtools required for a job.

**Browser Options**: The config.py file includes options for customizing the web browser used for scraping. You can modify the BROWSER_TYPE variable to specify a different browser, such as "chrome" or "firefox". Additionally, you can adjust the HEADLESS_MODE variable to True or False to enable or disable the headless mode of the browser.

**Other Settings**: The config.py file may include additional settings specific to your project requirements. Feel free to review and update any other variables as needed.

## 5. Troubleshooting
If you encounter any issues while using the project, consider the following troubleshooting steps:

Ensure Correct Configuration: Double-check the config.py file to ensure that all the required configuration variables are filled in correctly. Verify that the API keys, credentials, and other settings are accurate.

**Check Dependencies**: Make sure you have installed the necessary dependencies listed in the requirements.txt file. You can install them using the pip install -r requirements.txt command.

**Internet Connectivity**: Ensure that you have a stable internet connection while running the project, as it relies on web scraping and API interactions.

**API Limitations**: Take note of any usage limits or restrictions imposed by the LinkedIn, Airtable, or OpenAI APIs. Exceeding these limits may cause errors or unexpected behavior.

**Error Handling**: The project may include error handling mechanisms to handle common issues. Pay attention to any error messages displayed during execution and refer to the project's code or documentation for troubleshooting guidance.

If the troubleshooting steps above do not resolve your issue, consider raising an issue in the project's repository, providing details about the problem you encountered and any relevant error messages.


## 6. Contributing

Contributions to this project are welcome! If you have any ideas, improvements, or bug fixes, feel free to submit a pull request. Ensure that your contributions align with the project's scope and follow the established coding conventions.

When contributing, please provide clear and concise documentation, along with any necessary updates to the project's code or configuration.


## 7. License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code for personal or commercial purposes.
