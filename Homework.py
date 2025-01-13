# Homework:

# Define the parent class Car
class Car:
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")

# Define the BMW class which inherits from Car
class BMW(Car):
    def start_engine(self):
        return "BMW engine started with a smooth purr."

# Define the Ferrari class which inherits from Car
class Ferrari(Car):
    def start_engine(self):
        return "Ferrari engine roars to life!"

# Function to demonstrate polymorphism
def start_car_engine(car):
    print(car.start_engine())

# Create instances of BMW and Ferrari
bmw_car = BMW()
ferrari_car = Ferrari()

# Demonstrate polymorphism by calling start_engine() on both objects
start_car_engine(bmw_car)     # Output: BMW engine started with a smooth purr.
start_car_engine(ferrari_car) # Output: Ferrari engine roars to life!
