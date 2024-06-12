import requests
from bs4 import BeautifulSoup
import json

BASE_URL = 'http://quotes.toscrape.com'

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def scrape_quotes():
    quotes_data = []
    authors_data = {}
    page = 1

    while True:
        soup = get_soup(f'{BASE_URL}/page/{page}/')
        quotes = soup.select('.quote')
        
        if not quotes:
            break

        for quote in quotes:
            text = quote.select_one('.text').get_text(strip=True)
            author = quote.select_one('.author').get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.select('.tags .tag')]
            author_url = BASE_URL + quote.select_one('a')['href']

            quotes_data.append({
                'tags': tags,
                'author': author,
                'quote': text
            })

            if author not in authors_data:
                author_soup = get_soup(author_url)
                born_date = author_soup.select_one('.author-born-date').get_text(strip=True)
                born_location = author_soup.select_one('.author-born-location').get_text(strip=True)
                description = author_soup.select_one('.author-description').get_text(strip=True)
                
                authors_data[author] = {
                    'fullname': author,
                    'born_date': born_date,
                    'born_location': born_location,
                    'description': description
                }
        
        page += 1

    return quotes_data, list(authors_data.values())

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    quotes, authors = scrape_quotes()
    save_to_json(quotes, 'quotes.json')
    save_to_json(authors, 'authors.json')
    print("Data scraped and saved to quotes.json and authors.json")
