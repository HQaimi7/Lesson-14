from abc import ABC, abstractmethod
#abc = abstract base class

class Vehicle(ABC):
    @abstractmethod
    def num_wheels(self):
        """Return the number of wheels the vehicle has."""
        pass
    
class Bike(Vehicle):
    @property
    def num_wheels(self):
        return 2 # Bikes have 2 wheels
    
class Car(Vehicle):
    @property
    def num_wheels(self):
        return 4 # Cars have 4 wheels
    
#Example usage

bike = Bike()
car = Car()

print(f"A bike has {bike.num_wheels} wheels.")
print(f"A car has {car.num_wheels} wheels.")

print("-----------------------------")
#Abstract class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

#Concrete class:Cirlce   
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
            
        def area(self):
            return 3.14 * self.radius * self.radius
        
#Concrete class:Rectangle
    class Rectangle(shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            
        def area(self):
            return self.width * self.height
        
#Example usage
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")

c1= Circle[5]
r1= Rectangle[4,6]
print(f"Area of Circle: {c1.area()}")
print(f"Area of Rectangle: {r1.area()}")

#-------------------------Example 2 -- Payment management -------------------------

print("\n-----------------------------\n")


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Process a payment for the given amount."""
        pass

class CreditCardPayment(Payment):
    from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Process the payment of the specified amount."""
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")

# Creating instances of payment methods
credit_card = CreditCardPayment()
paypal = PayPalPayment()

# Directly calling the methods to make payments
credit_card.process_payment(50.00)
paypal.process_payment(30.75)


#--------------------------Example 3-------------------------

print("\n-----------------------------\n")

print("\n-----------------------------------------")

"""

Question:

We have different modes of transportation like Car, Bicycle, and Bus. While they all share common behaviors like starting, stopping, and displaying vehicle information, they differ in how they operate.

Abstract Class: Vehicle

-------------------------

Contains shared properties (brand, wheels) and methods (showDetails()).

Defines abstract methods (start(), stop()) to enforce implementation in subclasses.

Subclasses: Car, Bicycle, and Bus

----------------------------------

Each subclass provides its unique implementation for start() and stop().

Subclasses can have additional attributes and methods, e.g., Car has a fuelCapacity attribute and Bus has a seatingCapacity attribute.

Polymorphism and Reusability

-----------------------------

The Vehicle class ensures common behavior across all vehicle types, promoting code reusability.

Subclasses implement only their specific functionalities.

"""

class Vehicle(ABC):
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def showDetails(self):
        return f"Brand: {self.brand}, Wheels: {self.wheels}"

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

def showDetails(self):
    return f"Brand: {self.brand}, Wheels: {self.wheels}"

@abstractmethod
def start(self):
    pass

@abstractmethod
def stop(self):
    pass

#Car subclass
class Car(Vehicle):
    def __init__(self, brand, fuelCapacity):
        super().__init__(brand, 4)
        self.fuelCapacity = fuelCapacity

    def start(self):
        return f"{self.brand} car is starting with fuel capacity {self.fuelCapacity} litres."

    def stop(self):
        return f"{self.brand} car is stopping."

    def honk (self):
        return f"{self.brand} car is honking."
    
#Bicycle subclass
class Bycicle(Vehicle):
    def __init__(self, brand,):
        super().__init__(brand, 2)

    def start(self):
        return f"{self.brand} bicycle is starting by pedaling."
    def stop(self):
        return f"{self.brand} bycicle is stopping by applying brakes."

    def ringBell(self):
        return f"Biycle bell: Ring ring!"
    
