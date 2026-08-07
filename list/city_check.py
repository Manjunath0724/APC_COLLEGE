cities = ["New York", "London", "Paris", "Tokyo", "Mumbai"]
print("Cities in list:", cities)

city = input("Enter city name: ")
if city in cities:
    print("City exists in the list")
else:
    print("City does not exist in the list")
