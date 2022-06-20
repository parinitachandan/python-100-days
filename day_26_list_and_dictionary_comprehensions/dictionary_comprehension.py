names = ["Alex", "Beth", "Hailey", "DJ", "Kimmy"]
import random

students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

higher_score = {student: score for (student, score) in students_score.items() if score >= 60}
print(f" Students with score greater than 60 - {higher_score}")

lower_score = {student: score for (student, score) in students_score.items() if score < 60}
print(f" Students with score lower than 60 - {lower_score}")
