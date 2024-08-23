class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
            return
        print("Contact List:")
        for i, contact in enumerate(self.contacts):
            print(f"{i+1}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def edit_contact(self):
        self.view_contacts()
        if not self.contacts:
            return
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            print("Enter new details for the contact:")
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            contact.name = name
            contact.phone = phone
            contact.email = email
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")

    def delete_contact(self):
        self.view_contacts()
        if not self.contacts:
            return
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.edit_contact()
        elif choice == '4':
            manager.delete_contact()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()