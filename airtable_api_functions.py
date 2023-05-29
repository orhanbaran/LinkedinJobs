# airtable_api_functions.py
import pyairtable
from config import AIRTABLE_BASE_KEY, AIRTABLE_TABLE_NAME, AIRTABLE_TOKEN_OR_API_KEY

# Initialize Airtable connection
base_key = AIRTABLE_BASE_KEY
table_name = AIRTABLE_TABLE_NAME
airtable_token = AIRTABLE_TOKEN_OR_API_KEY
airtable = pyairtable.Table(base_id=base_key, table_name=table_name, api_key=airtable_token)


# Prepare data to send to Airtable
def add_new_job(job_title, company_name, job_location, job_onsite_remote, job_salary, job_type, job_required_exp, job_link, job_role, skills_tools):
    data = {
        'Job Title': job_title,
        'Company Name': company_name,
        'Job Location': job_location,
        'Onsite/Remote': job_onsite_remote,
        'Salary': job_salary,
        'Job Type': job_type,
        'Required Level': job_required_exp,
        'Job Role': job_role,
        'Skills&Tools': skills_tools,
        'Job Link': job_link,
    }

    # Create a new row in Airtable
    airtable.create(data)