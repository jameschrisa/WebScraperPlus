# Full process roundtrip to API

import requests
from bs4 import BeautifulSoup
import re
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json

# Prompt the user for a URL and the name of an output file
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

# Authenticate using the service account
client = language.LanguageServiceClient.from_service_account_json('path/to/credentials.json')

# Read the output file
with open(output_file, 'r') as f:
    text = f.read()

# Create a document object
document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

# Extract the entities
response = client.analyze_entities(document=document)
entities = response.entities

# Extract the keyphrases
response = client.analyze_syntax(document=document)
keyphrases = [token.text.content for token in response.tokens if enums.PartOfSpeech.Tag(token.part_of_speech.tag).name == 'NOUN_PHRASE']

# Extract the salience score
response = client.analyze_sentiment(document=document)
salience_score = response.document_sentiment.magnitude

# Create a dictionary to store the results
results = {
    'entities': [{'name': entity.name, 'type': entity.type, 'salience': entity.salience} for entity in entities],
    'keyphrases': keyphrases,
    'salience_score': salience_score
}

# Write the results to a json file
with open('results.json', 'w') as json_file:
    json.dump(results, json_file)

print("Data has been analyzed by the Natural Language API and the results have been written to 'results.json")
