class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.availability = True
        self.ISBN = ISBN

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Availability: {self.availability}")

    def check_availability(self):
        return self.availability

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books_borrowed = []

    def display(self):
        print(f"User ID: {self.user_id}, Username: {self.username}, Books Borrowed: {', '.join(book.title for book in self.books_borrowed)}")

class Transaction:
    def __init__(self, user, book, status):
        self.user = user
        self.book = book
        self.status = status

    def display(self):
        print(f"User ID: {self.user.user_id}, Book Title: {self.book.title}, Status: {self.status}\n")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def display_users(self):
        for user in self.users:
            user.display()
    
    def display_books(self):
        for book in self.books:
            book.display()

    def add_book(self, title, author, ISBN):
        book = Book(title, author, ISBN)
        self.books.append(book)
        print(f"Book {book.title} added successfully!")
    
    def add_user(self, user_id, username):
        user = User(user_id, username)
        self.users.append(user)
        print(f"User {user.username} added successfully!")

    def borrow_book(self, user_id, title):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.title == title and b.availability), None)

        if user and book:
            transaction = Transaction(user, book, "borrowed")
            self.transactions.append(transaction)
            book.availability = False
            user.books_borrowed.append(book)
            print(f"Book {title} borrowed by {user.username}")
        else:
            print("Book or User not found or book not available!")

    def return_book(self, user_id, title):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.title == title and not b.availability), None)

        if user and book:
            transaction = Transaction(user, book, "returned")
            self.transactions.append(transaction)
            book.availability = True
            user.books_borrowed.remove(book)
        else:
            print("Book not borrowed by the user or book not found.")

    def transaction_report(self):
        print("\nTransaction Report:")
        for transaction in self.transactions:
            transaction.display()

def main():
    library = Library()

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Check Book Availability")
        print("6. Display User Information")
        print("7. Display all books")
        print("8. Generate Transaction Report")
        print("0. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            ISBN = input("Enter ISBN: ")
            library.add_book(title, author, ISBN)

        elif choice == '2':
            user_id = input("Enter user ID: ")
            username = input("Enter user name: ")
            library.add_user(user_id, username)

        elif choice == '3':
            user_id = input("Enter user ID: ")
            book_title = input("Enter book title to borrow: ")
            library.borrow_book(user_id, book_title)

        elif choice == '4':
            user_id = input("Enter user ID: ")
            book_title = input("Enter book title to return: ")
            library.return_book(user_id, book_title)

        elif choice == '5':
            title = input("Enter book title to check: ")
            book = next((b for b in library.books if b.title == title), None)
            if book:
                print(f"Book {title} is {'available' if book.check_availability() else 'not available'}")
            else:
                print(f"Book {title} not found.")

        elif choice == '6':
            library.display_users()

        elif choice == '7':
            library.display_books()

        elif choice == '8':
            library.transaction_report()

        elif choice == '0':
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 8.")

if __name__ == '__main__':
    main()
