class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    pass
c = Car()
c.start()
#Flow:Vehicle -> Car
#2. Multiple Inheritance - MRO
#One child inherits From multiple parents.
class Engine:
    def engine_type(self):
        print("Petrol ENgine")
class Wheels:
    def wheel_type(self):
        print("4 Wheels")
class Car(Engine, Wheels):
    pass
c = Car()
c.engine_type()
c.wheel_type()
#Flow Engin + Wheels -> Car

#3. Multilevel Inheritance
#A chain of Inheritance
class Vehicle:
    def start(self):
        print("Vehicle start")
class Car(Vehicle):
    def drive(self):
        print("Car drives")
class SportsCar(Car):
    def speed(self):
        print("Very fast")
s = SportsCar()
s.start()
s.drive()
s.speed()
#Flow Vehicle -> Car -> SportsCar

#4. Hierarchical Inheritance
#Multiple child classes inherit from 

class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
c = Car()
b = Bike()
c.start()
b.start()
# Flow:
#             Vehicle
#            /      \ 
#           Car     Bike

# 5. HYbrid Inheritance
# Combination of multiple type(like multiple)
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Engine(Vehicle):
    def engine(self):
        print("Engine working")
class Wheels:
    def wheels(self):
        print("Wheels rolling")
class Car(Engine, Wheels):
    pass

c = Car()
c.start()
c.engine()
c.wheels()
