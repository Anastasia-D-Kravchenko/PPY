import random

scores = [random.randint(0, 100) for _ in range(50)]

grades = []
for s in scores:
    if 90 <= s <= 100: grades.append(5)
    elif 75 <= s <= 89: grades.append(4)
    elif 60 <= s <= 74: grades.append(3)
    else: grades.append(2)

average = sum(scores) / len(scores)
passed_count = sum(1 for i in grades if i > 2)

scores.sort(reverse=True)
best_five = scores[:5]

print(f"Average: {average:.2f}")
print(f"Students passed: {passed_count}")
print(f"Top 5 scores: {best_five}")