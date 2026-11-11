# square
square = []
for i in range(1,6):
    square.append(i*i)
print(square)

#print()
#list comprence
#[expression for item in iterable]
#set comprence
#{expression for item in iterable}

#lowecase
cities = ["Bengaluru","Pune","Bengaluru","Chennai","Pune"]
u_cities = {city.lower() for city in cities}
print(u_cities)
print(cities)

#square
numbers = [2,3,2,4,3]
unique_squares = set()#set removes the duplicate element
for number in numbers:
    unique_squares.add(number*number)#to add the square of number we will write .add
print(unique_squares)


unique_squares = {number*number for number in numbers}
print(unique_squares)
print(type(unique_squares))

numbers = [2,3,2,4,3]
square_list = [number*number for number in numbers]#it shows duplicates squares in result
square_set = {number*number for number in numbers}#it only shows the unique element result
print(square_list)
print(square_set)

