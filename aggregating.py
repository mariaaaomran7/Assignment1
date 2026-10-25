# 8. Average age
average_age = sum(student["age"] for student in students) / len(students)
print(average_age)

# 9. Total hours studied
total_hours = sum(student["hours_studied"] for student in students)
print(total_hours)

# 10. Student with the most study hours
top_hours = students[0]

for student in students:
    if student["hours_studied"] > top_hours["hours_studied"]:
        top_hours = student

print(top_hours["name"], top_hours["hours_studied"])

# 11. Average score of each student
for student in students:
    average = sum(student["scores"]) / len(student["scores"])
    print(student["name"], round(average, 1))
    