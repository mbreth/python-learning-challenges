student_scores = []

print("Welcome to the Grade Analyzer!")

students = 1

while students <= 5:
    score = int(input(f"Enter a score for student {students}: "))
    students += 1
    student_scores.append(score)

average = sum(student_scores) / len(student_scores)
average = "{:.2f}".format(average)

highest_score = max(student_scores)
lowest_score = min(student_scores)

passing_students = 0
failing_students = 0

for scores in student_scores:
    if scores >= 70:
        passing_students += 1
    else:
        failing_students += 1

print(f"Average Score: {average}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Students Passed: {passing_students}")
print(f"Students Failed: {failing_students}")













