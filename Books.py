from fastapi import FastAPI, Body
from BookResponseModel import BOOKS as books


app = FastAPI()

@app.get('/books')
async def read_all_books():
    return {'response': books}


@app.get('/books/{book_title}')
async def read_book(book_title:str):

    for book in books:
       if book.get('title').casefold() == book_title.casefold():
           return book


@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/get-by-author/')
async def get_books_by_author(book_author: str):
    books_by_author = []

    for book in books:
        if book.get('author').casefold() == book_author.casefold():
            books_by_author.append(book)

    return books_by_author

@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category:str):
    books_to_return = []

    for book in books:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post('/books/create_book')
async def create_book(new_book = Body()):
    books.append(new_book)
    return {'errorCode': '0000', 'errorDescription': 'Book Created Successfully'}

@app.put('/books/updated_book')
async def update_book(updated_book=Body()):
    for i in range(len(books)):
        if books[i].get('title').casefold() == updated_book.get('title').casefold():
            books[i] = updated_book
    return {'errorCode': '0000', 'errorDescription': 'Book updated successfully'}

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(books)):
        if books[i].get('title').casefold() == book_title.casefold():
            books.pop(i)
            break

