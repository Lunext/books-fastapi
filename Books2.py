
from fastapi import FastAPI, Path, Query, HTTPException, status
from Models import  Book, BookRequest
from MockData.BOOKS import BOOKS
from Helpers.bookHelper import BookHelper
app = FastAPI()
Book = Book.Book
BookRequest = BookRequest.BookRequest


@app.get('/books', status_code= status.HTTP_200_OK)
async def read_all_books():
    return {'response': BOOKS}

@app.get('/books/{book_id}', status_code=  status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code= 404, detail= 'Item not found')

@app.get('/books/', status_code= status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt= 0, lt= 6)):
    books_to_return = []
    for book in BOOKS:
        if book_rating == book.rating:
            books_to_return.append(book)

    return books_to_return

@app.get('/books/filter_by_date/', status_code= status.HTTP_200_OK)
async def get_books_by_published_date(published_date: int = Query(gt= 1999, lt= 2031)):
    books_filtered = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_filtered.append(book)

    return books_filtered

@app.post('/create-book', status_code= status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(BookHelper.find_book_id(new_book))

@app.put('/books/update_book', status_code= status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True

    BookHelper.is_book_changed(book_changed)

@app.delete('/books/{book_id}', status_code= status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt= 0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    BookHelper.is_book_changed(book_changed)

