# openai_api_functions.py
import openai
from config import OPENIA_API_KEY

# Set up your OpenAI API credentials
openai.api_key = OPENIA_API_KEY


# Define a function to generate the summarized output
def the_role(raw_data):
    prompt = "Raw Data: /n" + raw_data + "Q: can you give me the role of the job in the given data and summarize it in a sentence for me? no need to write down the requirements or anything else, just the role please"

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5
    )
    job_role = response.choices[0].text.strip()
    return job_role


def the_requirements(raw_data):
    prompt = "Raw Data: /n" + raw_data + "Q: can you find the required experiences and summarize them for me?"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5
    )
    job_req = response.choices[0].text.strip()
    return job_req


def list_skills_tools(raw_data):
    prompt = "Raw Data: /n" + raw_data + "Q:  can you just list the name of the required software,tools, frameworks, 3rd party applications? just the names that are mentioned as required for this role? just the names, NOTHING ELSE! just start your answer like this: python, sql, etc.."
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5
    )
    skills_tools = response.choices[0].text.strip()
    return skills_tools

