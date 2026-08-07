students = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("Original list:", students)

first = students.pop(0)
last = students.pop()
if "Charlie" in students:
    students.remove("Charlie")

print("Remaining list:", students)
