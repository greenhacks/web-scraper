# Reference: https://www.freecodecamp.org/news/python-projects-for-beginners/#binary-search-python-project

import requests
from bs4 import BeautifulSoup as bs
import csv

# send request to URL
url = "https://www.re-plus.com/see-whos-attending/"
r = requests.get(url)

# make soup
soup = bs(r.content, "html.parser")
company_name = soup.find_all("span", {"class": "pp-table-cell-text"})

# extract to csv
dataset = [x for x in zip(company_name)]
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for data in dataset:
        writer.writerow(data)
