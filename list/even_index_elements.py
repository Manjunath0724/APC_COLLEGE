elements = ["A", "B", "C", "D", "E", "F", "G", "H"]
print("Original list:", elements)

print("Elements at even indices:")
for i in range(0, len(elements), 2):
    print("Index", i, ":", elements[i])
