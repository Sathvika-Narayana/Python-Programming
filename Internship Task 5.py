#Internship Task 5

#Contacts Book

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"Contact '{name}' has been added to the address book.")

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' has been removed from the address book.")
    else:
        print(f"Contact '{name}' not found in the address book.")

def display_contacts():
    if contacts:
        print("Address Book:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print()
    else:
        print("Your address book is empty.")

while True:
    print("\nMenu:")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Display contacts")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        add_contact(name, phone, email)
    elif choice == '2':
        name = input("Enter the name of the contact to remove: ")
        remove_contact(name)
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Goodbye!")