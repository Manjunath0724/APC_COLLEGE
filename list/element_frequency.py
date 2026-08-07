elements = ["apple", "banana", "apple", "cherry", "banana", "apple"]

frequency = {}
for item in elements:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

for key, value in frequency.items():
    print(key, ":", value)
