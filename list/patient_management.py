patients = [
    ["John Doe", 45],
    ["Jane Smith", 32]
]

while True:
    print("\n1. Add | 2. Delete | 3. Search | 4. Display | 5. Count | 6. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        patients.append([name, age])
        print("Patient added")
    elif choice == '2':
        name = input("Enter name to delete: ")
        found = False
        for p in patients:
            if p[0] == name:
                patients.remove(p)
                found = True
                break
        if found:
            print("Patient deleted")
        else:
            print("Patient not found")
    elif choice == '3':
        name = input("Enter name to search: ")
        found = False
        for p in patients:
            if p[0] == name:
                print("Found - Name:", p[0], "Age:", p[1])
                found = True
                break
        if not found:
            print("Patient not found")
    elif choice == '4':
        print("Patients:", patients)
    elif choice == '5':
        print("Total patients:", len(patients))
    elif choice == '6':
        break
