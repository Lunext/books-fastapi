from Models.Book import Book
from MockData.BOOKS import BOOKS
from fastapi import  HTTPException



class BookHelper:
    @staticmethod
    def find_book_id(book: Book):
        book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
        return book

    @staticmethod
    def is_book_changed(book_changed_param: bool):
        if not book_changed_param:
            raise HTTPException(status_code=404, detail='Item not found')

