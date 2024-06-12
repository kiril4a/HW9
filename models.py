from mongoengine import Document, StringField, ListField, ReferenceField, connect, BooleanField

# Підключення до MongoDB Atlas
connect(
    db="cluster0",
    username="kiril4a",
    password="matador1983",
    host="mongodb+srv://kiril4a:matador1983@cluster0.t1m9ifp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    email_sent = BooleanField(default=False)