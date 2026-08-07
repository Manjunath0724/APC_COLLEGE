salaries = [45000, 60000, 25000, 80000, 30000, 55000, 28000, 90000]
print("Employee Salaries:", salaries)

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50k = []
below_30k = []
for sal in salaries:
    if sal > 50000:
        above_50k.append(sal)
    if sal < 30000:
        below_30k.append(sal)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Salaries above Rs. 50,000:", above_50k)
print("Salaries below Rs. 30,000:", below_30k)
