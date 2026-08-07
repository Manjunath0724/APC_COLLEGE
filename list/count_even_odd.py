numbers = [12, 15, 22, 33, 40, 55, 60, 71, 80, 93, 100, 115, 120, 131, 140]
print("List of numbers:", numbers)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
