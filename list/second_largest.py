numbers = [12, 45, 2, 41, 31, 10, 8, 6]
print("Original list:", numbers)

unique_numbers = list(set(numbers))
unique_numbers.sort()
second_largest = unique_numbers[-2]

print("Second largest element is:", second_largest)
