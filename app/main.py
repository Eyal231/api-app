import json
import logging
from fastapi import FastAPI, HTTPException

# Create a FastAPI instance
app = FastAPI()
def new_func(app):
    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)


# Load data from the JSON file
with open('book-dict.json', 'r') as file:
    book_dict = json.load(file)

# Define API endpoints:
#root
@app.get("/")
def get_intro():
    return ["Welcome to the Book API!" ,
    {"server": "author API Server",
     "version": "1.0",
     "status": "Running"}
     ]

#authors
@app.get("/author/{author_name:path}")
def get_author(author_name: str):
    try:
        if author_name == "":
            raise HTTPException(status_code=400, detail="Bad Request - use: book/<author_name>")
        # Check if the author_name is present in the book_dict
        if any(book['author'] == author_name for book in book_dict):
            author_books = [book['title'] for book in book_dict if book['author'] == author_name]
            author_info = [{
                'name': author_name,
                'books': author_books
            },
            {   "server": "author API Server",
                "version": "1.0",
                "status": "Running"
            }]
            return author_info
         else:
            raise HTTPException(status_code=404, detail="Author not found")
    except HTTPException as e:
        # Re-raise the HTTPException with the appropriate status code and detail message
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
#books
@app.get("/book/{book_title:path}")
def get_book(book_title: str):
    if book_title == "":
            raise HTTPException(status_code=400, detail="Bad Request - use: book/<book_title>")
        matching_books = [book for book in book_dict if book['title'] == book_title]
        if matching_books:
            book_info = {
                'book': matching_books[0]['title'],
                'genre': matching_books[0]['genre'],
                'author': matching_books[0]['author']
            }
            return book_info
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    except HTTPException as e:
        # Re-raise the HTTPException with the appropriate status code and detail message
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

