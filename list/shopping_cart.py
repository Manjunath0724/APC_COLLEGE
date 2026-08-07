cart = []

while True:
    print("\n1. Add | 2. Remove | 3. Search | 4. Display | 5. Count | 6. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        item = input("Enter item to add: ")
        cart.append(item)
        print("Item added")
    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Item removed")
        else:
            print("Item not in cart")
    elif choice == '3':
        item = input("Enter item to search: ")
        if item in cart:
            print("Item is in cart")
        else:
            print("Item not in cart")
    elif choice == '4':
        print("Cart:", cart)
    elif choice == '5':
        print("Total items:", len(cart))
    elif choice == '6':
        break
