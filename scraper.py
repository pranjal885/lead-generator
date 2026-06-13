import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://realpython.github.io/fake-jobs/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

jobs = []

cards = soup.find_all("div", class_="card-content")

for card in cards:

    title = card.find("h2").text.strip()

    company = card.find("h3").text.strip()

    location = card.find("p", class_="location").text.strip()

    link = card.find_all("a")[1]["href"]

    jobs.append({
        "Job Title": title,
        "Company": company,
        "Location": location,
        "Apply Link": link
    })

df = pd.DataFrame(jobs)

df.to_csv("output/leads.csv", index=False)

print(f"{len(df)} job leads saved successfully!")