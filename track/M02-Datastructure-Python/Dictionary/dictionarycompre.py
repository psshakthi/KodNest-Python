
#Dictionary Comprehension
numbers = [ 2,3,4,5]
cube_by_number = {}
for num in numbers:
    cube_by_number[num]=num ** 3
print(cube_by_number)

cube_by_number = {number: number ** 3 for number in numbers}
print(cube_by_number)
print(type(cube_by_number))

#Frequency count
languages = ["Python","Java","Python","SQL","Java","Python"]
frequency = {}
for language in languages:
    if language in frequency:
        frequency[language] += 1
    else:
        frequency[language] = 1
print(frequency)
#Using Counter
from collections import Counter
languages = Counter(languages)
print(frequency)
print(frequency["Python"])
print(frequency["Java"])

languages = ["Python", "Java", "Python", "SQL"]
frequency = Counter(languages)
for lang, count in frequency.items():
    print(lang,count)
    