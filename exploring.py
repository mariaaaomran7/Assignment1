# 1. First and last student
print(students[0]["name"])
print(students[-1]["name"])

# 2. Rim's scores
for student in students:
    if student["name"] == "Rim":
        print(student["scores"])

# 3. Print information about all students
for student in students:
    print(f'{student["name"]} is {student["age"]} years old and studies {student["track"]}')
    