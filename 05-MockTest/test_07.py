points = 95

if points >= 90:
    grade = 5.0
elif points >= 80:
    grade = 4.5
elif points >= 70:
    grade = 4.0
elif points >= 60:
    grade = 3.5
elif points >= 50:
    grade = 3.0
else:
    grade = 2.0

print(f'Points: {points}, grade: {grade}')