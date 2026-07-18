# Read N (students) and K (subjects)
n, k = map(int, input().split())

# Gather the marks for all K subjects
subject_marks = []
for _ in range(k):
    subject_marks.append(list(map(float, input().split())))

# Use zip(*...) to group marks by student instead of by subject
for student_marks in zip(*subject_marks):
    # Calculate the average score for the student
    student_average = sum(student_marks) / k
    # Print formatted to 1 decimal place
    print(f"{student_average:.1f}")
