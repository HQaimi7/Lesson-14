class Library:
    def __init__(self, list_of_books, name):
        self.booklist = list_of_books
        self.name = name 
        self.lendDict = {}
    
    def displayBooks(self):
        print(f"\nWe have the following books in our Library: {self.name}")
        for book in self.booklist:
            if book in self.lendDict:
                print(f"The book '{book}' is already being used by {self.lendDict[book]}")
            else:
                print(f"'{book}' is available")

    def lendBook(self, user, book):
        if book not in self.booklist:
            print("Sorry, we do nat have that book in our Library.")
        elif book in self.lendDict:
            print(f"The book '{book}' is already being used by {self.lendDict[book]}")
        else:
            print(f"Lender-Book database has been updated. '{book}' has been lent to {user}")


    def addBook(self, book):
        self.booklist.append(book)
        print(f"'{book}' has been added to the book list")

    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print(f"'{book}' has been returned successfully")
        else:
            print("That book wasn't borrowed from our Library")


if __name__ == '__main__':
    books = Library([
        'Python', 'Rich Dad poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'
    ], "Let's Upskill")

    user_name = input("Welcome to our library! Please enter your name:  ")

    while True:
        print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:  ")
        print(
            "1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit"
        )

        user_choice = input("Enter your choice to continue:  ")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option")
            continue

        user_choice = int(user_choice)

        if user_choice == 1:
            books.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:  ")
            user = input("Enter your name:  ")
            books.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:  ")
            books.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:  ")
            books.returnBook(book)

        elif user_choice == 5:
            print("Thank you for using our library. Goodbye!")
            break
        
        print("Press 'Q' to quit or 'C' to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
            else:
                print("Enter a valid option")
                continue