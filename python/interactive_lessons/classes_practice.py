# Python Lesson 11.2 - Practice Classes

# Inherits from object class (most basic class) which gives all properties of an object
class Car(object):
    # pass
    # Member variable
    condition = "new"
    
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    # Classes can also have methods
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

    def drive_car(self):
        self.condition = "used"

# Creating instance of class
# my_car = Car("DeLorean", "silver", 88)

# print my_car.condition
# print my_car.model
# print my_car.color
# print my_car.mpg

# print my_car.display_car()

# print my_car.condition
# my_car.drive_car()
# print my_car.condition

# Inheritance
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type
    
    def drive_car(self):
        self.condition = "like new"


my_car = ElectricCar("DeLorean", "midnight blue", 90, "molten salt")

print my_car.display_car()

print my_car.condition
my_car.drive_car()
print my_car.condition


# __repr__() method: Short for representation; tells Python how to represent an object of class
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        # Tell Python to represent object in (x, y, z) format
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print my_point