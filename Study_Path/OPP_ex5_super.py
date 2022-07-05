class Vehicle:
    
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel
    
    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        else:
            return True
    
class Car(Vehicle):

    def __init__(self, make, model, fuel="gas", name="unknown"):
        super().__init__(make, model, fuel)
        self.name = name

    def horn(self):
        print(f"{self.name} pom pom {self.make}")


v1 = Vehicle("make1", "model1")

c1 = Car("car1", "model2", "cng", "robo")

c1.horn()

print(v1.is_eco_friendly())
print(c1.is_eco_friendly())