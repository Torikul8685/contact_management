
from store_contact import save_contact, load_contact

def add_contact(name, phone, email, address):
    # Load existing contacts
    contacts = load_contact()
    
    # Check if phone number already exists
    if any(contact["phone"] == phone for contact in contacts):
        print("Error: Duplicate phone number! Contact not added.")
        return

    # Create new contact
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contact(contacts)
    print("Contact added successfully!")

def view_contact():
    contact_list = load_contact()
    print("\nContact List\n")
    for i, contact in enumerate(contact_list, start=1):
        print(f" {i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def remove_contact(index):
    contacts = load_contact()
    if 0 < index <= len(contacts):
        del contacts[index - 1]
        save_contact(contacts)
        print("Contact removed successfully!")
    else:
        print("Invalid index!")

def search_contact(query):
    contacts = load_contact()
    result = []
    for contact in contacts:
        if (query.lower() in contact["name"].lower() or
            query.lower() in contact["phone"] or
            query.lower() in contact["email"].lower()):
            result.append(contact)
    
    print("\nSearch Results:\n")
    for i, contact in enumerate(result, start=1):
        print(f" {i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")


    


    


