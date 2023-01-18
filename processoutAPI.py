# process output scrape and send to Google Cloud NLP
# pip install google-cloud-language

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json

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
