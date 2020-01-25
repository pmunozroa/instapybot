from bs4 import BeautifulSoup
import requests
# Here, we're just importing both Beautiful Soup and the Requests library
page_link = 'https://simple.ripley.cl/'
# this is the url that we've already determined is safe and legal to scrape from.
page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")
# we use the html parser to parse the url content and store it in a variable.
paragraphs = page_content.find_all("li")
textContent = []
for i in paragraphs:
    textContent.append(i.text)
print(textContent)
