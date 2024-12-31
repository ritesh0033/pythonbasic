class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def update_status(self):
        self.is_borrowed = not self.is_borrowed
        action = "borrowed" if self.is_borrowed else "returned"
        return f'Book "{self.title}" has been {action}.'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f'Title: {book.title}, Author: {book.author}, Status: {status}')

    def modify_book_status(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book.update_status())
                return
        print(f'Book "{title}" not found in the library.')


# Example Usage
if __name__ == "__main__":
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    library.list_books()

    library.modify_book_status("The Great Gatsby")
    library.list_books()

    library.modify_book_status("The Great Gatsby")
    library.list_books()

    library.modify_book_status("Moby Dick")
