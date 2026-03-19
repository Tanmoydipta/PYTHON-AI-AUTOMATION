import requests
from bs4 import BeautifulSoup

# 1. Fetch the webpage
page = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(page.text, "html.parser")

# 2. The Net: Grab EVERY quote element on the page
all_quotes = soup.find_all("span", class_="text")

# 3. The Loop: Go through them one by one
for quote in all_quotes:
    print(quote.text)