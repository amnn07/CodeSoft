class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts available.")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, old_contact, new_contact):
        index = self.contacts.index(old_contact)
        self.contacts[index] = new_contact

    def delete_contact(self, contact):
        self.contacts.remove(contact)

# Function to display contact details
def display_contact(contact):
    print("Contact Details:")
    print(f"Name: {contact.name}")
    print(f"Phone: {contact.phone_number}")
    print(f"Email: {contact.email}")
    print(f"Address: {contact.address}")

# Main function
def main():
    contact_book = ContactBook()
    
    # Sample contacts
    contact1 = Contact("John Doe", "1234567890", "john@example.com", "123 Main St")
    contact2 = Contact("Jane Smith", "9876543210", "jane@example.com", "456 Elm St")
    contact3 = Contact("Alice Brown", "5555555555", "alice@example.com", "789 Oak St")
    
    contact_book.add_contact(contact1)
    contact_book.add_contact(contact2)
    contact_book.add_contact(contact3)

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Found contacts:")
                for i, contact in enumerate(found_contacts, 1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No contacts found.")
        
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            found_contacts = contact_book.search_contact(name)
            if found_contacts:
                display_contact(found_contacts[0])
                print("\nEnter updated details:")
                name = input("Enter name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                updated_contact = Contact(name, phone_number, email, address)
                contact_book.update_contact(found_contacts[0], updated_contact)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
        
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            found_contacts = contact_book.search_contact(name)
            if found_contacts:
                contact_book.delete_contact(found_contacts[0])
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
