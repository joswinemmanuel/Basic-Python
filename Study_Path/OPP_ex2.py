class Car:
    runs = True
    number_of_wheels = 4

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
print(f"Cars have {Car.get_number_of_wheels()} wheels.")

# Of course, we can override this in our instance: the number_of_wheels of this instance 
# will become 6 and in the class it's still 4
my_car.number_of_wheels = 6

# And when we access our new instance variable: 6 is the output as in this instance value
# was changed
print(f"My car has {my_car.number_of_wheels} wheels.")

# But, when we call our class method on our instance: 4 will be the output as 
# get_number_of_wheels() is a class method and in the class number_of_wheels is 4
print(f"My car has {my_car.get_number_of_wheels()} wheels.")
