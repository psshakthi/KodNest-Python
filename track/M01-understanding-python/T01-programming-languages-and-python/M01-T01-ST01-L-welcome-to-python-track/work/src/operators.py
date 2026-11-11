# Arithmatic operator 
x = 15
y = 4
print(x+y) #19
print(x-y) #11
print(x*y) #60
print(x/y) #3.75
print(x%y) #3
print(x**y) #15*15*15*15 = 50625
print(x//y) #3
 

print("---Assignment Operator---")
x = 10
print("Starting value: x = ", x)# 10
x += 5
print("\nAfter += 5 :", x)#x=10 x+=5 is x=x+5 = 10+5:15
x -= 3
print("\nAfter -= 3 :", x)#x=15 x=15-3 = 12
x *= 2
print("\nAfter *= 2 :", x)#x=12 x*=2 is x=12*2=24
x /= 4
print("\nAfter /= 4 :", x)#x=24 x/=4 is x=24/4=6
x //= 2
print("\nAfter //= 2:", x)#x=6 x//=2 is x=6//2=3
x %= 3
print("\nAfter %=3:", x)#x=3 x%=3 is x=3%3=0
x = 6
print("\nReset x =", x)
x **= 2
print("\nAfter **=2:",x)#x=6 x^=2 is x=6^2=36

print("-----Logical Bitwise Operator-----")
x =6
print("\nReset x=", x)#x=6
x &= 3
print("\nAfter &= 3: ", x)#it finds the binary number #x=6 x&3 = 6 & 3 = 0110 & 0011 = 0010 = 2
x |= 2
print("\nAfter |= 2: ", x)#x=2 x|2 = 2 | 2 = 0010 | 0010 = 0010 = 2
x ^= 5
print("\nAfter ^= 5: ", x)# x=2 x^5=2^5=0010^0101=0111=7
x = 4
print("\nResent x=", x)
x <<= 2
print("After <<=2: ", x)#
print("----------Python allows you to chain comparison operators------")
x = 5
print(1 < x < 10) # t
print(1 < x and x < 10) # t

print("--------------------Logical Operators--------------------")
a = True
b = False

print("a and b =", a and b) # f
print("a or b  =", a or b) # t
print("not a   =", not a) # f
print("not b   =", not b) # t

x = 10
y = 5

print("\n(x > 5) and (y < 10) =", (x > 5) and (y < 10)) #
print("(x < 5) and (y < 10)  =", (x < 5) and (y < 10)) #

print("\n(x > 5) or (y > 10) =", (x > 5) or (y > 10)) #
print("(x < 5) or (y > 10)  =", (x < 5) or (y > 10)) #

print("\nnot (x == 10) =", not (x == 10)) #
print("not (y == 3)  =", not (y == 3)) #


exit()


print("-----identity operator-----")
x = ["apple","banana"]
y = ["apple","banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = [1,2,3]
y = [1,2,3]
print(x == y)#check for value
print(x is y)

print("-----Ternary operator-----")
age=21
res = "Adult" if age>=18 else "Minor"
print(res)
exit()

#WAP to find largest of 3 numbers
a = 20
b = 15
c = 50
biggest = a if a > b and a > c else b if b > a and b > c else c
print(biggest)
exit()