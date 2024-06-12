import json
from mongoengine import connect
from models import Author, Quote

connect(
    db="cluster0",
    username="kiril4a",
    password="matador1983",
    host="mongodb+srv://kiril4a:matador1983@cluster0.t1m9ifp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        authors = json.load(f)
        for author in authors:
            new_author = Author(
                fullname=author['fullname'],
                born_date=author['born_date'],
                born_location=author['born_location'],
                description=author['description']
            )
            new_author.save()

def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        quotes = json.load(f)
        for quote in quotes:
            author = Author.objects(fullname=quote['author']).first()
            if author:
                new_quote = Quote(
                    tags=quote['tags'],
                    author=author,
                    quote=quote['quote']
                )
                new_quote.save()

if __name__ == '__main__':
    load_authors('authors.json')
    load_quotes('quotes.json')
    print("Data loaded into MongoDB")
