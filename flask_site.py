""" from flask import Flask, render_template
import plugin

app = Flask(__name__)

@app.route('/')
def home():
    result = my_function()
    return render_template('flaskHome.html', result=result)

def my_function():
    #Use plugin to get books (NEED TO CONNECT TO POSTGRESQL FIRST - need a connection string)
    #return plugin.get_book("George Orwell", plugin.connect(host, db, username, password))
    
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
 """

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('flaskSearch.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()

    with open('books.json', 'r') as f:
        books = json.load(f)

    results = [book for book in books if query in book['title'].lower()]

    return render_template('flaskSearch.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
