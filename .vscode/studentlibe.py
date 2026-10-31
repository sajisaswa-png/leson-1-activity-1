# ================================
# STUDENT GRADE BOOK
# ================================

# ---------- PART 1: the dictionary ----------
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Evan": 88
}

# ---------- PART 2: class average ----------
total = 0
for score in grades.values():
    total += score

class_average = total / len(grades)
print(f"Class Average: {class_average}")

# ---------- PART 3: highest score ----------
top_name = ""
top_score = 0

for name, score in grades.items():
    if score > top_score:
        top_score = score
        top_name = name

print(f"Highest Scorer: {top_name} with a score of {top_score}")

# ---------- PART 4: look up a student ----------
student_name = input("Enter the student's name to look up: ")
score = grades.get(student_name, "Not found")
print(f"Score: {score}")