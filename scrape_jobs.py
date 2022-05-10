import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all('div', class_="card-content")

for job_element in job_elements:
    title = job_element.find('h2', 'title')
    company = job_element.find('h3', 'company')
    location = job_element.find('p', 'location')
    time = job_element.find('time')

    time = datetime.strptime(time.text.strip(), '%Y-%m-%d')

    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(time)
    print()