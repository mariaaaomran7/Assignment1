students = [
    {"name": "Lara", "age": 23, "track": "AI", "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar", "age": 31, "track": "Data", "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim", "age": 27, "track": "AI", "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web", "hours_studied": 8, "scores": [50, 65, 40]},
    {"name": "Nour", "age": 25, "track": "AI", "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami", "age": 35, "track": "Data", "hours_studied": 48, "scores": [88, 91, 79]}
]
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
    
    
# 12. New list with name and average score
score_data = [
    {
        "name": student["name"],
        "average_score": sum(student["scores"]) / len(student["scores"])
    }
    for student in students
]
print(score_data)

# 13. Count students in each track
track_counts = {}

for student in students:
    track = student["track"]
    if track in track_counts:
        track_counts[track] += 1
    else:
        track_counts[track] = 1

print(track_counts)

# 14. Unique tracks
tracks = {student["track"] for student in students}
print(tracks)

# A set removes duplicates automatically.


# 15. Filter by track
def filter_by_track(students, track):
    return [student for student in students if student["track"] == track]

print(filter_by_track(students, "AI"))
print(filter_by_track(students, "Data"))


# 16. Average score of one student
def average_score(student):
    return sum(student["scores"]) / len(student["scores"])

print(average_score(students[0]))


# 17. Student with the highest average score
def top_student(students):
    best = max(students, key=average_score)
    return best["name"]

print(top_student(students))


# 18. Summary of students
def summary(students):
    return {
        "total_students": len(students),
        "average_age": sum(student["age"] for student in students) / len(students),
        "tracks": {student["track"] for student in students}
    }

print(summary(students))

# 19. Report sorted by average score
def report(students, min_hours):
    result = []

    for student in students:
        if student["hours_studied"] >= min_hours:
            result.append({
                "name": student["name"],
                "average_score": average_score(student)
            })

    return sorted(result, key=lambda student: student["average_score"], reverse=True)

print(report(students, 30))


