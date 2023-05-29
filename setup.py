from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='LinkedinJobsScraping',
    version='1.0.0',
    author='Orhan Alp Baran',
    author_email='baranalp@proton.me',
    description='Scraping selected LinkedIn job information, summarizing them using OpenAI API, and adding data to Airtable.',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'linkedin_jobs=main:main',
        ],
    },
)
