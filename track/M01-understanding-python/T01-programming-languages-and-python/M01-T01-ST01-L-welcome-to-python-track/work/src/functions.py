def add():
    a , b =10,10
    c = a+b
    print(c)
add()

print("---Find the sqaure numbers---")
def square():
    num = 5
    square = num * num
    res = square
    print (res)
square() 

print("---No Argument + No return value---")
def add1():
    a , b = 10 , 20
    c = a + b
    print(c)
add1()

print("---No argument +return value---")
def add2():
    a ,b = 10,20
    c = a+b
    return c
print(add2())

print("---Argument +return value---")
def add3(a,b):
    c = a + b
    print(c)
add3(10, 50)

print("---Argument + Return VAluie---")
def add4(a, b):
    c = a+b
    return c
res = add4(100, 200)    
print(res)