from os import system


class Library:
    def show_message(self, message ="Welcome to Library Management System."):
        print(f"\n{message}")

class Book(Library): #inherit from Library Class
    def __init__(self, bookid, title, author, available = True):
        self.bookid = bookid
        self.title = title
        self.author = author
        self.available = available
    def __str__(self):
        return f"{self.bookid}, {self.title}, {self.author}, {self.available}"

class Users(Library): #inherit from Library Class
    def __init__(self, userid, name):
        self.userid = userid
        self.name = name

    def __str__(self):
        return f"{self.userid}, {self.name}"

class Library_System(Library):
    def __init__(self):
        self.books = []
        self.users = []
        self.loadbook = []
        self.loadusers = []


#_____________________File Handling_____________________#
    #Loading books.txt file

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    bookid, title, author, available = line.strip().split(",")
                    self.books.append(Book(bookid, title, author, available.strip() == "true"))
        except FileNotFoundError:
            print("Book was not found, please check your file path")

    #Saving to the books.txt file

    def save_books(self):
        with open("books.txt", "w") as file:
            for books in self.books:
                file.write(str(books) + "\n")
        print("All books saved to file")


    #Loading user information

    def load_users(self):
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    userid, name = line.strip().split(",")
                    self.users.append(Users(userid, name))
        except FileNotFoundError:
            print("User was not found, please check your file path")


    #Saving user information

    def save_users(self):
        with open("users.txt", "w") as file:
            for users in self.users:
                file.write(str(users) + "\n")

    #--------------------------Admin Functions--------------------------#
    def add_book(self):
        bookid = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        new_book = Book(bookid, title, author)
        self.books.append(new_book)
        self.save_books()
        self.show_message(f"{title} book added to the system")

    def remove_book(self):
        bookid = input("Enter book ID: ")
        for book in self.books:
            if book.bookid == bookid:
                self.books.remove(book)
                self.save_books()
                self.show_message(f"{book.title} removed from the system")
                return
        print("Book was not found, please check your book ID")

    def view_books(self):
        if not self.books:
            print("No book was found, please try again")
            return
        print("\nBook details:")
        for book in self.books:
            print(f"{book.bookid}, {book.title}, {book.author}")

    def add_user(self):
        userid = input("Enter user ID: ")
        name = input("Enter user name: ")
        new_user = Users(userid, name)
        self.users.append(new_user)
        self.save_users()
        self.show_message(f"{name} your user registration successful.")

    def view_users(self):
        if not self.users:
            print("No user was found, please try again")
            return
        print("\nUser details:")
        for user in self.users:
            print(f"{user.userid}, {user.name}")


    #------------------------Library System------------------------#
library_system = Library_System()

while True:
    print("=" * 40)
    print("Welcome to Library Management System")
    print("=" * 40, "\n")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")

    choice = input("Enter your choice(1 to 3): ")

    if choice == "1":
        admin_login = input("Enter Username: ")
        admin_password = input("Enter Password: ")

        if admin_login == "admin" and admin_password == "admin123":
            print("Login Successful, Welcome to Library Management System")
            while True:
                print("=" * 20)
                print("Admin Menu")
                print("=" * 20)
                print("1. Add a book")
                print("2. Remove a book")
                print("3. View a book")
                print("4. View user")
                print("5. Add User")
                print("6. Logout")
                admin_choice = input("Enter your choice(1 to 6): ")

                if admin_choice == "1":
                    library_system.add_book()
                elif admin_choice == "2":
                    library_system.remove_book()
                elif admin_choice == "3":
                    library_system.view_books()
                elif admin_choice == "4":
                    library_system.view_users()
                elif admin_choice == "5":
                    library_system.add_user()
                elif admin_choice == "6":
                    print("Logout Successful")
                    break

                else:
                    print("Invalid choice, please try again")

        else:
            print("Invalid admin credentials, please try again")

    elif choice == "2":
        name = input("Enter Username: ")
        print(f"Welcome {name} to Library Management System")

    elif choice == "3":
        print("Leaving the System. Thank You")
        break

    else:
        print("Invalid choice, please try again")