filename = "library.txt"

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        status = "BORROWED" if self.is_borrowed else "AVAILABLE"
        return f"{self.title} by {self.author} ({self.year}) - {status}"
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self):
        title = input("Enter book title to add: ").strip()
        author = input("Enter author: ").strip()
        year = input("Enter year: ").strip()

        if title == "" or author == "" or year == "":
            print("Invalid info")
        else:
            new_book = Book(title, author, year)
            self.books.append(new_book)
            save_books(filename, self.books)
            print(f"'{title}' added to {self.name}")

    def remove_book(self):
        title = input("Enter book title to remove: ").strip()
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                save_books(filename, self.books)
                print(f"'{title}' removed.")
                return
        print(f"'{title}' not found")


    def borrow_book(self):
        title = input("Enter book title: ").strip()
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                found = True
                if  book.is_borrowed:
                    print(f"'{book.title}' is already borrowed")
                else:
                    book.is_borrowed = True
                    save_books(filename, self.books)
                    print(f"'{book.title}' successfully borrowed!")
                break
        if not found:
            print(f"'{title}' was not found")


    def return_book(self):
        title = input("Enter book title to return: ").strip()
        for book in self.books:
            if title.lower() == book.title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    save_books(filename, self.books)
                    print(f"{title} book return successful.")
                else:
                    print(f"'{title}' was not borrowed")
                return
        print(f"{title} not found.")

    def search_book(self):
        keyword = input("Enter keyword to search: ").strip().lower()
        for i,book in enumerate(self.books):
            if keyword in book.title.lower() or keyword in book.author.lower():
                print(f"{i+1}. {book}")
    
    def show_all(self):
        if not self.books:
            print("No books yet")
        else:
            for i, book in enumerate(self.books):
                print(f"{i+1}. {book}")

    def show_available(self):
        if not self.books:
            print("No books yet")
        else:
            for i, book in enumerate(self.books):
                if not book.is_borrowed:
                    print(f"{i+1}. {book}")


def load_books(filename):
    books = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                b = Book(parts[0], parts[1], parts[2])
                b.is_borrowed = parts[3] == "BORROWED"
                books.append(b)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error: {e}")
    return books

def save_books(filename, books):
    with open(filename,"w") as f:
        for book in books:
            status = "BORROWED" if book.is_borrowed else "AVAILABLE"
            f.write(f"{book.title}|{book.author}|{book.year}|{status}\n")
            

# Loading the data from file
loaded_data = load_books(filename)

# Creating library and assigning loaded data to its internal list 
my_library = Library("Central Library")
my_library.books = loaded_data

while(True):
    print("===========================")
    print("   LIBRARY BOOK TRACKER   ")
    print("===========================")
    print("1. Add book")
    print("2. Remove book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Search book")
    print("6. Show all books")
    print("7. Show available books")
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == "8":
        print("Goodbye!")
        break
    elif choice == "1":
        my_library.add_book()
    elif choice == "2":
        my_library.remove_book()
    elif choice == "3":
        my_library.borrow_book()
    elif choice == "4":
        my_library.return_book()
    elif choice == "5":
        my_library.search_book()
    elif choice == "6":
        my_library.show_all()
    elif choice == "7":
        my_library.show_available()
    else:
        print("Invalid choice")