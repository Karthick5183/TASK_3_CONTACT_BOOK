contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("This contact already exists.")
        return
    
    phone_number = input("Enter phone number: ").strip()
    address = input("Enter address: ").strip()
    email = input("Enter email: ").strip()
    
    contacts[name] = {
        "phone_number": phone_number,
        "address": address,
        "email": email
    }
    print("Contact added successfully.")

def delete_contact():
    name = input("Enter name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")

def update_contact():
    name = input("Enter name of the contact to update: ").strip()
    if name in contacts:
        phone_number = input("Enter new phone number: ").strip()
        address = input("Enter new address: ").strip()
        email = input("Enter new email: ").strip()
        
        contacts[name] = {
            "phone_number": phone_number,
            "address": address,
            "email": email
        }
        print("Contact updated successfully.")
    else:
        print("This contact does not exist.")

def search_contact():
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        contact = contacts[name]
        print(f"Contact Found: {name}, {contact['phone_number']}, {contact['address']}, {contact['email']}")
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("There are no such contacts.")
    else:
        print("Contacts List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone Number: {info['phone_number']}, Address: {info['address']}, Email: {info['email']}")

while True:
    print("\nContact Book:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Display Contacts")
    print("6. Stop")

    choice = input("Enter your choice (1-6): ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        print("Exiting Contact Book. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
