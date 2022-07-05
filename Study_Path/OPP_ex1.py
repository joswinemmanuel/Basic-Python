""" OOPS
    int is a 'class' and 42 or any other number is a 'instance' of the class int """

class Car:
    runs = False

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def start(self):
        self.runs = True

    def stop(self):
        self.runs = False 
        
    def run(self):
        if self.runs:
            print(f"{self.name} is started.....brooom vroom")
        else:
            print(f"{self.name} cannot be started...it is not drivable")


car1 = Car("Bugatti",10000)
print(car1)
print("Started : ",car1.runs)
car1.run()
print()

car1.start()
print("Started : ",car1.runs)
car1.run()
print()

car1.stop()
print("Started : ",car1.runs)
car1.run()