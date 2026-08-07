numbers = [10, 20, 10, 30, 20, 40, 10]
print("Original list:", numbers)

unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)
