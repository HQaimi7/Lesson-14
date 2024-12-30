class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner       # Public attribute
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Outputs: 1500

account.withdraw(200)
print(account.get_balance())  # Outputs: 1300

# Attempting to access the private attribute directly (not recommended)
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
        self.__speed = 0  # Private attribute

    def accelerate(self, increment):
        if increment > 0:
            self.__speed += increment
            print(f"Accelerated to {self.__speed} km/h")
        else:
            print("Increment must be positive.")

    def brake(self, decrement):
        if decrement > 0 and self.__speed - decrement >= 0:
            self.__speed -= decrement
            print(f"Decelerated to {self.__speed} km/h")
        else:
            print("Invalid brake amount.")

    def get_speed(self):
        return self.__speed

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)

    def get_speed(self):
        return self.speed


# Example usage
car = Car("Toyota", "Corolla")
car.accelerate(50)
car.brake(20)
print("Current speed:", car.get_speed())


#---------------------------------------------------------

print("\n-----------------------------\n")

class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Added grade: {grade}")
        else:
            print("Grade must be between 0 and 100")

    def get_average_grade(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0
    
    def got_details(self):
        return f"Name: {self.__name}, Average Grade: {self.get_average_grade()}"
    
#Example usage
student = Student("Alice")
student.add_grade(85)
student.add_grade(90)
print(student.get_details())


#--------------Library Management System-------------------

print("\n-----------------------------\n")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("You have borrowed '{self.title}'. ")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def get_details(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"
    
#Example usage
book = Book("1984", "George Orwell")
print(book.get_details())
book.borrow()
print(book.get_details())
book.return_book()
print(book.get_details())