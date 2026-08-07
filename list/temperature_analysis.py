temperatures = [
    32, 34, 31, 30, 29, 33, 35, 36, 34, 32,
    31, 28, 27, 29, 30, 31, 33, 34, 35, 36,
    37, 38, 35, 34, 33, 32, 30, 29, 28, 30
]
print("Temperatures of 30 days:", temperatures)

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / len(temperatures)

above_average = 0
below_average = 0
for temp in temperatures:
    if temp > average:
        above_average += 1
    elif temp < average:
        below_average += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average temperature:", above_average)
print("Days below average temperature:", below_average)
