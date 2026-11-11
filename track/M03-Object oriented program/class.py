class Student:
    name = "Shakthi"
    age = 21
    mark = 75
    def study(self):
        print(f"{self.name} is studying {self.age} years")
    def play(self):
        print(f"{self.name} is playing {self.age} years")
s = Student()
print(s.name)
print(s.age)
s.study()
s.play()

print("\n---Constructor---")
class Student:
    #Constructor
    def __init__ (self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def study(self):
        print(f"{self.name} is studying {self.age} years")
    def play(self):
        print(f"{self.name} is playing {self.age} years")
s1 = Student("Rahul", 21, 78)
print(f"Name:{s1.name} \nAge:{s1.age} \nMarks:{s1.marks}")
s2 = Student("Shakthi", 21, 94)
print(f"Name:{s2.name} \nAge:{s2.age} \nMarks:{s2.marks}")
print(s1.age)
s1.study()
s1.play()
s2.study()
s2.play()

print("\n")
class Student:
    #Costructor
    def __init__(self, name, age, company):
        #Instance attributes - self or obj ref
        self.name = name
        self.age = age
        self.company = company
        #Instance method -using self refercence, obj ref
    def study(self):
        #a=10 #Local attribute
        #print(a)
        print(f"{self.name} is studying")
    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)
    def trip(self):
        print(f"{self.name} is goes a trip")
s1 = Student("Chai", 21, "Google")
s1.study()
s1.getDetails()

print("\n")
s2 = Student("Janu", 21, "Wipro")
print(s2.name)
s2.study()
s2.getDetails()


print("\n")
class Student:
    company = "Kodnest Technologies"
    #Costructor
    def __init__(self, name, age):
        #Instance attributes - self or obj ref
        self.name = name
        self.age = age
        #Instance method -using self refercence, obj ref
    def study(self):
        a=10 #Local attribute
        print(a)
        print(f"{self.name} is studying")
    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)
    def trip(self):
        print(f"{self.name} is goes a trip")
s1 = Student("Chai", 21)
print(Student.company)
print(s1.company)
print(s1.name)
s1.study()
s1.getDetails()
s1.trip()

print("\n")
s2 = Student("Janu", 21)
print(s2.name)
s2.study()
s2.getDetails()
s2.trip()

print("\n static and class method")
class Student:
    company = "Kodnest Technologies"
    #Costructor
    def __init__(self, name, age):
        #Instance attributes - self or obj ref
        self.name = name
        self.age = age
        #Instance method -using self refercence, obj ref
    def study(self):
        a=10 #Local attribute
        print(a)
        print(f"{self.name} is studying")
    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)
    
    @staticmethod
    def trip(name):
        print(f"{name} is goes a trip")
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
Student.change_company("KodNest Technollogy pvt limit")    
s1 = Student("Chai", 21)
print(Student.company)
print(s1.company)
print(s1.name)
s1.study()
s1.getDetails()


print("\n")
s2 = Student("Janu", 21)
print(s2.name)
s2.study()
s2.getDetails()
