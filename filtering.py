# 4. Filter AI students using a loop
ai_students = []

for student in students:
    if student["track"] == "AI":
        ai_students.append(student)

print(len(ai_students))

# 5. Filter AI students using list comprehension
ai_students2 = [student for student in students if student["track"] == "AI"]

print(ai_students2 == ai_students)

# 6. Names of students who studied more than 30 hours
names = [student["name"] for student in students if student["hours_studied"] > 30]
print(names)

# 7. Students older than 24 and in AI
result = [student for student in students if student["age"] > 24 and student["track"] == "AI"]
print(result)
