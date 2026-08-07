marks = [78, 85, 92, 67, 74, 88, 59, 90, 82, 71, 95, 63, 80, 77, 89, 66, 83, 72, 91, 55]
print("Student marks:", marks)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above_count = 0
below_count = 0
for m in marks:
    if m > average:
        above_count += 1
    elif m < average:
        below_count += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students scoring above average:", above_count)
print("Students scoring below average:", below_count)
