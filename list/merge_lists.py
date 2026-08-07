list1 = []
n1 = int(input("Enter number of elements for list 1: "))
for i in range(n1):
    val = input("Enter element: ")
    list1.append(val)

list2 = []
n2 = int(input("Enter number of elements for list 2: "))
for i in range(n2):
    val = input("Enter element: ")
    list2.append(val)

merged = list1 + list2
print("Merged list:", merged)
