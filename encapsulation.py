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

#-----------------------Fitness Tracker---------------------
print("\n-----------------------------\n")
class FitnessTracker:
    def __init__(self):
        self._steps = 0 # Private attribute
        self._calories_burned = 0 # Private attribute
    
    def add_steps(self, steps):
        if steps > 0:
            self._steps += steps
            self._calories_burned += steps * 0.05 #Assure 0.05 calories burned per step
            print(f"Added {steps} steps. Total steps: {self._steps}")
        else:
            print("Steps must be positive number.")
    
    def get_summary(self):
        return {
            "steps": self.__steps,
            "calories_burned": self._calories_burned
        }
#example usage
tracker = FitnessTracker()
tracker.add_steps(1000)
tracker.add_steps(500)
print(tracker.get_summary())

print("------------- Airline System -------------\n")

class Passenger:
    def __init__(self, name, passport_number):
        self.__name = name  # Private attribute
        self.__passport_number = passport_number  # Private attribute

    def get_details(self):
        return f"Name: {self.__name}, Passport Number: {self.__passport_number}"

class Flight:
    def __init__(self, flight_number, destination):
        self.__flight_number = flight_number  # Private attribute
        self.__destination = destination  # Private attribute
        self.__passengers = []  # Private attribute

    def add_passenger(self, passenger):
        self.__passengers.append(passenger)
        print(f"Added passenger: {passenger.get_details()} to flight {self.__flight_number}.")

    def get_passenger_list(self):
        return [passenger.get_details() for passenger in self.__passengers]

    def get_flight_info(self):
        return f"Flight Number: {self.__flight_number}, Destination: {self.__destination}"

class Booking:
    def __init__(self):
        self.__bookings = []  # Private attribute

    def book_flight(self, flight, passenger):
        flight.add_passenger(passenger)
        self.__bookings.append((flight, passenger))
class Booking:
    def __init__(self):
        self.__bookings = []  # Private attribute

    def book_flight(self, flight, passenger):
        flight.add_passenger(passenger)
        self.__bookings.append((flight, passenger))
        print(f"Booking confirmed for {passenger.get_details()} on flight {flight.get_flight_info()}.")

    def get_all_bookings(self):
        return [(flight.get_flight_info(), passenger.get_details()) for flight, passenger in self.__bookings]

# Example usage
# Create passengers
passenger1 = Passenger("Alice Smith", "A1234567")
passenger2 = Passenger("Bob Johnson", "B2345678")

# Create a flight
flight = Flight("AA101", "New York")

# Create a booking
booking_system = Booking()
booking_system.book_flight(flight, passenger1)
booking_system.book_flight(flight, passenger2)

# View flight info and bookings
print("\nFlight Information:", flight.get_flight_info())
print("\nPassenger List:", flight.get_passenger_list())
print("\nAll Bookings:", booking_system.get_all_bookings())
