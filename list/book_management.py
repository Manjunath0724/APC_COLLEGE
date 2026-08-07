books = ["1984", "Moby Dick", "The Hobbit"]

while True:
    print("\n1. Add | 2. Search | 3. Remove | 4. Display | 5. Count | 6. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        book = input("Enter book to add: ")
        books.append(book)
        print("Book added")
    elif choice == '2':
        book = input("Enter book to search: ")
        if book in books:
            print("Book is available")
        else:
            print("Book not found")
    elif choice == '3':
        book = input("Enter book to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed")
        else:
            print("Book not found")
    elif choice == '4':
        print("Books:", books)
    elif choice == '5':
        print("Total books:", len(books))
    elif choice == '6':
        break
