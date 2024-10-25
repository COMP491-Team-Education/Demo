import requests

def get_books_info(partial_title, limit=10):
    base_url = "https://openlibrary.org/search.json"
    params = {
        "title": partial_title,
        "fields": "key,title,author_name,cover_i",
        "limit": limit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data["numFound"] > 0:
            books = []
            for book in data["docs"]:
                info = {
                    "title": book.get("title", "N/A"),
                    "author": book.get("author_name", ["N/A"])[0] if book.get("author_name") else "N/A",
                    "cover": f"http://covers.openlibrary.org/b/id/{book['cover_i']}-M.jpg" if book.get("cover_i") else None
                }
                books.append(info)
            return books
        else:
            return "No books found with that title."
    else:
        return f"Error: {response.status_code}"

def get_books_by_author(author_name, limit=10):
    base_url = "https://openlibrary.org/search.json"
    params = {
        "author": author_name,
        "fields": "key,title,author_name,cover_i",
        "limit": limit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        books = []
        for book in data["docs"]:
            book_info = {
                "title": book.get("title", "N/A"),
                "author": book.get("author_name", ["N/A"])[0] if book.get("author_name") else "N/A",
                "cover": f"http://covers.openlibrary.org/b/id/{book['cover_i']}-M.jpg" if book.get("cover_i") else None
            }
            books.append(book_info)
        return books
    else:
        return f"Error: {response.status_code}"