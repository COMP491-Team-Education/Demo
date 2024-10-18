import psycopg2

def connect(host, db, username, password):
    try:
        # Establish a connection
        conn = psycopg2.connect(
            host= host,
            database= db,
            user= username,
            password= password
        )

        # Create a cursor object to execute queries
        cur = conn.cursor()

    except:
        print(error)


# GET: Fetch a book by title
def get_book(book_title, cur):

        # query
        cur.execute(f'''SELECT id, title, author, picture FROM Books WHERE title = {book_title}''')

        # Fetch the result
        result = cur.fetchall()

        if result:
            # Convert the row into a dictionary
            book = {
                "id": result[0],
                "title": result[1],
                "author": result[2],
                "picture": result[3],
            }
            return book
        else:
           print("error: Book not found")


# GET: Fetch a book by author
def get_book(author, cur):

        # query
        cur.execute(f'''SELECT id, title, author, picture FROM Books WHERE author = {author}''')

        # Fetch the result
        result = cur.fetchall()

        if result:
            # Convert the row into a dictionary
            book = {
                "id": result[0],
                "title": result[1],
                "author": result[2],
                "picture": result[3],
            }
            return book
        else:
           print("error: Book not found")



# POST: Add a new book
def add_book(title, author, picture, cur):
    try:
        # Query to insert a new book
        cur.execute(f'''
            INSERT INTO Books (title, author, picture)
            VALUES {title, author, picture)}
        ''')
        
        # Commit the transaction
        cur.connection.commit()
        
        print("Book added successfully")
        return True
    except Exception as e:
        print(f"Error adding book: {str(e)}")
        return False


# DELETE: Remove a book by its ID
def remove_book(book_name, cur):
    try:
        # Query to delete the book
        cur.execute(f'''
            DELETE FROM Books 
            WHERE title = {book_name}
        ''')
        
        # Check if any row was affected
        if cur.rowcount > 0:
            # Commit the transaction
            cur.connection.commit()
            print("Book removed successfully")
            return True
        else:
            print("Error: Book not found")
            return False
    except Exception as e:
        print(f"Error removing book: {str(e)}")
        return False

#close the connection
def close(curr):
    cur.close()
    conn.close()
    