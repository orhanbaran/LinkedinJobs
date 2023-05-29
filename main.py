from openai_api_functions import the_role,list_skills_tools
from airtable_api_functions import add_new_job
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from config import LINKEDIN_USERNAME, LINKEDIN_PASSWORD, PROFILE_URL

# Creating an instance
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Logging into LinkedIn
driver.get("https://linkedin.com/uas/login")
username = driver.find_element(By.ID, "username")
username.send_keys(LINKEDIN_USERNAME)  # Enter Your Email Address

pword = driver.find_element(By.ID, "password")
pword.send_keys(LINKEDIN_PASSWORD)  # Enter Your Password


driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(40)
# Opening baran's Profile
# paste the URL of baran's profile here
profile_url = PROFILE_URL
driver.get(profile_url)  # this will open the link
time.sleep(20)
# get the job page you're interested
job_link = input("Enter the LinkedIn job listing link: ")
driver.get(job_link)
time.sleep(40
           )
job_src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(job_src, 'html.parser')
# Finding the source of job-info
job_info = soup.find('div', {'class': 'p5'})

# Checking the content of job_info
if job_info is not None:
    print('job info is ok')
else:
    print('job info is not working')

# finding the right location of job title
job_title_loc = job_info.find("h1")
if job_title_loc is not None:
    print('job_title_loc is ok')
else:
    print('job_title_loc is not working')

# Extracting the Job Title
job_title = job_title_loc.get_text().strip()

# Extracting the Company Name
company_name_loc = job_info.find_all('a', {'class': "ember-view"})
if company_name_loc is not None:
    print('company_name_loc is ok')
#    print(company_name_loc)
else:
    print('company_name_loc is not working')

# Getting the text of company name
company_name = ""
for element in company_name_loc:
    if element.get_text().strip():
        company_name += element.get_text().strip() + " "
# Extraction Location of the job
job_location_loc = job_info.find_all('span')[2]
if job_location_loc is not None:
    print('job_location_loc is ok')
else:
    print('job_location_loc is not working')

# Getting the text of job location
job_location = ""
for element in job_location_loc:
    if element.get_text().strip():
        job_location += element.get_text().strip() + " "

# Extraction Type of the job
job_onsite_remote_loc = job_info.find_all('span')[3]
if job_onsite_remote_loc is not None:
    print('job_onsite_remote_loc is ok')
else:
    print('job_onsite_remote_loc is not working')

# Getting the text of job type
job_onsite_remote = ""
for element in job_onsite_remote_loc:
    if element.get_text().strip():
        job_onsite_remote += element.get_text().strip() + " "

# Extraction Salary of the job
job_salary_loc = job_info.find_all('span')[6]
if job_salary_loc is not None:
    print('job_salary_loc is ok')
else:
    print('job_salary_loc is not working')

# Getting the text of job salary
job_salary_type_level = ""
for element in job_salary_loc:
    if element.get_text().strip():
        job_salary_type_level += element.get_text().strip() + " "

# Splitting the job_salary into three variables
job_salary_type_level = job_salary_type_level.split("·")

if len(job_salary_type_level) >= 3:
    job_salary = job_salary_type_level[0].strip()
    job_type = job_salary_type_level[1].strip()
    job_required_exp = job_salary_type_level[2].strip()
elif len(job_salary_type_level) > 2:
    job_salary = job_salary_type_level[0].strip()
    job_type = job_salary_type_level[1].strip()
else:
    job_salary = ""
    job_type = ""
    job_required_exp = ""

# Extracting Job Description from linkedin
job_description_loc = soup.find('div', {'class': 'jobs-description-content__text'})

if job_description_loc is not None:
    print('job_description_loc is ok')
else:
    print('job_description_loc is not working')

job_description = ""
for element in job_description_loc:
    if element.get_text().strip():
        job_description += element.get_text().strip() + " "




# Generate the role output
job_role = the_role(job_description)

# Generate the skills and tools output
skills_tools = list_skills_tools(job_description)

# Printing the information that are scraped
print("\n\n\nJob-Title -->", job_title,
      "\nCompany Name -->", company_name,
      "\nJob Location -->", job_location,
      "\nOnsite/Remote -->", job_onsite_remote,
      "\nJob Salary -->", job_salary,
      "\nJob Type -->", job_type,
      "\nJob Level -->", job_required_exp,
      "\nJob Role -->", job_role,
      "\nRequired Skills and tools -->", skills_tools,
      )

add_new_job(job_title, company_name, job_location, job_onsite_remote, job_salary, job_type, job_required_exp,job_link,job_role,skills_tools)
# Close the browser window when you're finished
driver.quit()