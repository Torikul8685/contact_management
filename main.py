from contact_manager import add_contact, view_contact, remove_contact, search_contact



while True:
    print("\n\nWelcome to Contact Management System.")
    print ( "1. Add Contact")
    print ( "2. View Contact")
    print ( "3. Remove Contact")
    print ( "4. Search  Contact")
    print("5. Exit")


    choice = input("Enter Your Choice: ")
    if choice == "1":
        name = input("Enter Your Name: ").strip()
        phone = input("Enter Your Phone Number: ").strip()
        
        email = input("Enter Your email: ").strip()
        address = input("Enter Your address: ").strip()




        add_contact(name, phone, email, address)
        print("Contact Added Successfully")

    elif choice == "2":
        view_contact()
    
    elif choice == "3":
        index = int(input("Enter the index of the contact to remove: "))
        remove_contact(index)

    elif choice == "4":
        query = input("Enter Your Search Query: ")
        
        search_contact(query)
    elif choice == "5":
        print("Good Luck!")
        break

    else:
        print("Invalid Choice!")


