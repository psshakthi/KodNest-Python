seat = [
    ["Asha", "Ravi"],
    ["Meera", "Kiran"]
]
student = {
    "name": "Asha",
    "subjects": ["Python","SQL","Java"]
}
print(student)

print("----Dictionary contain dictionary-----")
student = {
    "name" : "Asha",
    "marks" : {
        "python":88,
        "SQl":82,
        "Java":91
    }
}
print(student)

# list Containing Dictionaries
students = [
    {
        "name":"Asha",
        "branch":"CSE"
    },
    {
        "name": "Ravi",
        "branch": "ECE"
    }
]
print(students)
