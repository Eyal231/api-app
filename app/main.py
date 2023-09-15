import json
import logging
from fastapi import FastAPI, HTTPException

# Create a FastAPI instance
app = FastAPI()
def new_func(app):
    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# Load data from the JSON file
with open('book-dict.json', 'r') as file:
    book_dict = json.load(file)

# Define API endpoints
@app.get("/")
def get_intro():
    return "Welcome to the Book API!"

@app.get("/author/{author_name}")
def get_author(author_name: str):
    try:
        # Check if the author_name is present in the book_dict
        if any(book['author'] == author_name for book in book_dict):
            author_books = [book['title'] for book in book_dict if book['author'] == author_name]
            author_info = {
                'name': author_name,
                'books': author_books
            }
            return author_info
        else:
            raise HTTPException(status_code=404, detail="Author not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

#@app.get("/book/{book_title}")
#def get_book(book_title: str):
    try:
        if any(book['title'] == book_title for book in book_dict):
            book_info =  {
                'book': book_title,
                'genre': book[0]['genre'],
                'author': book[0]['author']
            }
            return book_info
        else:
            raise HTTPException(status_code=404, detail="book not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@app.get("/book/{book_title}")
def get_book(book_title: str):
    try:
        # Check if the book_title is present in the book_dict
        matching_books = [book for book in book_dict if book['title'] == book_title]
        if matching_books:
            # Assuming book titles are unique, return the first match
            book_info = {
                'book': matching_books[0]['title'],
                'genre': matching_books[0]['genre'],
                'author': matching_books[0]['author']
            }
            return book_info
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


    
    
   # for book_id, book_info in book_dict.items():
    #    if book_info['title'] == book_title:
     #       return book_info
   # return {"error": "Book not found"}
