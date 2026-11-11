class parent:
    p1 = 1200
    p2 = 1200
class child(parent):
    p3 = 2400
c = child()
print(c.p1)
print(c.p2)
print(c.p3)

class Employee:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone =phone
    #Inheretent Method
    def display(self):
        print(f"Name:{self.name}, Age:{self.age}, Email:{self.email}, Phone:{self.phone}")
    #Method Overridder
    def work(self):
        print("Employee is working")
#Child Class - developer
class Developer(Employee):
    #Overriding Method
    def work(self):
        print("Developer is working")
        #Specialized  Method
    def project(self,project_name):
        print("Developer developing the project:", project_name)
#Child Class - Tester
class Tester(Employee):
    def work(self):
        print("Tester is working")
    def project(self, project_name):
        print("Tester is testing project")
dev = Developer("Shakthi", 22, "psshakthi@gmail.com", 1234567890)
tes = Tester("Ranju", 22, "ranju@gmail.com", 9087654321 )

print("---Developer---")
dev.display()
dev.work()
dev.project("Medicine App")

print("---Tester---")
tes.display()
tes.work()
tes.project("E-commerce App")




