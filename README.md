# WebScraperPlus
Scrapes text from page and send output to API

# Scraping Text

In this script, the user is prompted to enter the URL of the website they want to scrape and the name of the output file. The script uses the requests library to make a GET request to the website, and the BeautifulSoup library to parse the HTML content.

It uses the find_all method to extract all headers by searching for elements with a tag name that starts with h followed by a number from 1 to 6. And it uses the get_text() method to extract all the text from the website.

Then it uses the decompose() method to remove the "div" elements with the class "ad", so that the text from ads is excluded.

Finally, it creates an output file with the name specified by the user and writes the headers and text to the file.

# Requirements

> Install SDK from https://cloud.google.com/sdk/docs/install

```./google-cloud-sdk/install.sh```

Then initialize using:

```./google-cloud-sdk/bin/gcloud init```

Once you have set up your GCP project, you will need to install the google-cloud-language library using pip:

```pip install google-cloud-language```

Python script that prompts the user for a URL and the name of an output file, then extracts all headers and text from the website, excludes any text from ads, and generates a flat file based on the name the user entered as the output file:

# Process Text via API

You can use the Google Cloud Natural Language API to analyze the text in your output file and extract information such as keywords, keyphrases, and salience scores. To do this, you'll need to set up a Google Cloud Platform (GCP) project and enable the Natural Language API. You can find more information on how to do this in the GCP documentation: https://cloud.google.com/natural-language/docs/getting-started
