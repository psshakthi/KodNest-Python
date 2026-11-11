marks = [90,89,45,60]
marks.pop(2)
print(marks)


marks = [70, 81, 60]
stud_marks = marks
print(marks)
print(stud_marks)

first = [1, 2, 3]
second = first
print(first is second)#it stored in same memory location
print(first == second)#it check wether the value is same

first = [1, 2, 3]
second = [1, 2, 3]
print(first is second)#because are stored separatly in memory location
print(first == second)

num = [10, 20]
values = num
values.append(30)
print(num)
print(values)

num = [10,20]
values = num
values = [100, 200]
print(num)
print(values)

