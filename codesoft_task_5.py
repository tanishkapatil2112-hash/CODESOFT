contacts = []

def add_contact():
    name = input("Enter Store Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()

def search_contact():
    key = input("Enter name or phone to search: ")

    for c in contacts:
        if key in c["name"] or key in c["phone"]:
            print("\n Contact Found:")
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            print("Address:", c["address"])
            print()
            return

    print("Contact not found.\n")

def update_contact():
    phone = input("Enter phone number of contact to update: ")

    for c in contacts:
        if c["phone"] == phone:
            print("Enter new details (leave blank to keep old value)")

            new_name = input("New Name: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")

            if new_name:
                c["name"] = new_name
            if new_email:
                c["email"] = new_email
            if new_address:
                c["address"] = new_address

            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")

def delete_contact():
    phone = input("Enter phone number of contact to delete: ")

    for c in contacts:
        if c["phone"] == phone:
            contacts.remove(c)
            print("contact deleted successfully!\n")
            return

    print("Contact not found.\n")


while True:
    print(" Contact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting program. Thank you!")
        break
    else:
        print( "Invalid choice. Try again.\n")

