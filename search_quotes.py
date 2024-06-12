from models import Author, Quote

def search_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(quote.quote)
    else:
        print("Author not found")

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(quote.quote)

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    for quote in quotes:
        print(quote.quote)

def main():
    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == 'exit':
            break
        command, value = user_input.split(':', 1)
        if command == 'name':
            search_by_author(value.strip())
        elif command == 'tag':
            search_by_tag(value.strip())
        elif command == 'tags':
            search_by_tags(value.strip())
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()
