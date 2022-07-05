print(isinstance(42, int))

# int is a 'class' and 42 is an 'instance' of the class int

print(issubclass(bool, int))

# bool is a 'subclass' of the 'class' int

print(issubclass(int, object))
print(issubclass(str, object))
print(issubclass(bool, object))

# technically, everything is a subclass of object
print()

""" __str__    and    __repr__
Both functions return a string representation of an object. __str__() should return readable end-user
output, and __repr__() should return the Python code necessary to rebuild the object. __str__() maps to
the built-in function str() and __repr__() maps to the built-in function repr() """

import datetime
now = datetime.datetime.now()
print(str(now))
print(repr(now),end="\n\n")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"

my_car = Car("Ford", "Thunderbird")
print(f"This object is a {str(my_car)}")
print(f"To reproduce it, type: {repr(my_car)}")