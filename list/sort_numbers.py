numbers = []
print("Enter 10 numbers:")
for i in range(10):
    val = int(input("Enter number: "))
    numbers.append(val)

print("Original list:", numbers)

numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)
