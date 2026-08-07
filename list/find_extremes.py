numbers = [23, 56, 12, 89, 4, 75, 43]
print("List of numbers:", numbers)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)
