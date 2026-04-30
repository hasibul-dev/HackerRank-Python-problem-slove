from collections import namedtuple

N, Student = int(input()), namedtuple('Student', input().split())
marks = [int(Student(*input().split()).MARKS) for _ in range(N)]
print(f"{sum(marks) / N:.2f}")
