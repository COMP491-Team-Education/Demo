import psycopg2

# Import your plugin functions
from plugin import connect, get_book, add_book, remove_book, close

# Database connection details
db_details = {
    'host': 'your_host',
    'database': 'your_db',
    'user': 'your_username',
    'password': 'your_password'
}

# Connect to the database
conn, cur = connect(**db_details)

# Define URL mappings
urls = (
    '/book/title/(.*)', 'GetBookByTitle',
    '/book/author/(.*)', 'GetBookByAuthor',
    '/book/add', 'AddBook',
    '/book/remove/(.*)', 'RemoveBook'
)

app = web.application(urls, globals())

class GetBookByTitle:
    def GET(self, title):
        book = get_book(title, cur)
        if book:
            return book
        else:
            return "Book not found"

class GetBookByAuthor:
    def GET(self, author):
        book = get_book(author, cur)
        if book:
            return book
        else:
            return "Book not found"

class AddBook:
    def POST(self):
        data = web.input()
        success = add_book(data.title, data.author, data.picture, cur)
        if success:
            return "Book added successfully"
        else:
            return "Error adding book"

class RemoveBook:
    def POST(self, title):
        success = remove_book(title, cur)
        if success:
            return "Book removed successfully"
        else:
            return "Error removing book"

if __name__ == "__main__":
    app.run()
    close(cur, conn)
