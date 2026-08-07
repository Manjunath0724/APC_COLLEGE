attendance = ["Alice", "Bob", "Charlie"]

while True:
    print("\n1. Total | 2. Search | 3. Add | 4. Remove | 5. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        print("Total students:", len(attendance))
    elif choice == '2':
        name = input("Enter student name: ")
        if name in attendance:
            print("Present")
        else:
            print("Absent")
    elif choice == '3':
        name = input("Enter student name to add: ")
        attendance.append(name)
        print("Student added")
    elif choice == '4':
        name = input("Enter absent student to remove: ")
        if name in attendance:
            attendance.remove(name)
            print("Student removed")
        else:
            print("Student not found")
    elif choice == '5':
        break
