products = [
    ["P101", "Keyboard", 1200],
    ["P102", "Mouse", 600],
    ["P103", "Monitor", 8500]
]
required_code = "P103"
for product in products:
    if product[0] == required_code:
        print(product)
        break


print("--------index dictionary----------")
employees = [
    {"employee_id": "E101", "name": "Asha", "department": "Development"},
    {"employee_id": "E102", "name": "Ravi", "department": "Testing"},
    {"employee_id": "E103", "name": "Meera", "department": "Support"}
]
print(employees)
employee_by_id = {}
for employee in employees:  #Read the employee id
    employee_id = employee["employee_id"] # By emp_id from employee dictory "Get emp id"
    employee_by_id[employee_id] = employee # Use that ID to store the employee's details for easy searching.
print(employee_by_id)

print("--------group of lookup---------")
students = [
    {"name": "Asha", "course": "Python"},
    {"name": "Ravi", "course": "Java"},
    {"name": "Meera", "course": "Python"},
    {"name": "Kiran", "course": "SQL"}
]
students_by_course ={}
for student in students:
    course = student["course"]
    name = student["name"]
    if course not in students_by_course:
        students_by_course[course] = []
        students_by_course[course].append(name)
print(students_by_course[course].append(name))