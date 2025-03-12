class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Added: {book}')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'Removed: {book}')
        else:
            print("Book not found in library.")

    def list_books(self):
        if self.books:
            print("Library Collection:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("The library has no books.")


# Example usage
my_library = Library()

book_0 = Book("To Kill a Mockingbird", "Harper Lee")
book_1 = Book("The Great Gatsby", "F. Scott Fitzgerald")

my_library.add_book(book_0)
my_library.add_book(book_1)
my_library.list_books()

my_library.remove_book(book_0)
my_library.list_books()