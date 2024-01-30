from pydantic import BaseModel
from typing import List

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    id_: int
    name: str
    pages: int


class Library(BaseModel):
    books: List[Book] = []

    def get_next_book_id(self):
        if self.books:
            return len(self.books) + 1
        else:
            return 1

    def get_index_by_book_id(self, user_id: int) -> int:
        for book in self.books:
            if book.id_ == user_id:
                return self.books.index(book)
        raise ValueError("Книги с запрашиваемым id не существует.")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
