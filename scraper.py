# scrape page

import requests
from bs4 import BeautifulSoup
import re

url = input("Enter the URL of the website you want to scrape: ")
output_file = input("Enter the name of the output file: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Exclude text from ads
for div in soup.find_all("div", {"class": "ad"}):
    div.decompose()

# Extract all headers
headers = []
for h in soup.find_all(re.compile('^h[1-6]$')):
    headers.append(h.text)

# Extract all text
text = soup.get_text()

# Write the data to the output file
with open(output_file, 'w') as f:
    for header in headers:
        f.write(header + '\n')
    f.write('\n')
    f.write(text)

print(f"Data has been written to {output_file}")
