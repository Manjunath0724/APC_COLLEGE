numbers = []
print("Enter 10 numbers:")
for i in range(10):
    val = int(input("Enter number: "))
    numbers.append(val)

total_sum = sum(numbers)
average = total_sum / len(numbers)

print("List of numbers:", numbers)
print("Sum:", total_sum)
print("Average:", average)
