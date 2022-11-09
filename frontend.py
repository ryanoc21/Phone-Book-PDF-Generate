from backend import Contact, Addressbook
import sys  # Needed for the quit method (to exit out of the menu)
from pdf_report import PDFReport  # Used to generate a PDF of the contact book, pip install fpdf if not working.

"""
This file contains the code for the frontend of the project, i.e., the console that will allow the user to
interact with the functionality of the addressbook. If you don't have fpdf imported, and don't want to import it, simply 
click 'n' when asked to generate a pdf report when quitting out of the program and the code will work fine. 

If there is an issue with importing fpdf, type the following into terminal: 
pip install -r requirements.txt 
"""


class Interface(Addressbook):
    """
    This class inherits the functionality of methods from the Addressbook class defined in the backend.
    It will allow the user to interact with the console to use the backend methods.
    """

    def __init__(self, addressbook_list):
        super().__init__()
        self.contact_list = addressbook_list

        # Will be used to check if the book is full before adding more contacts.
        self.current_num_contacts = len(addressbook_list)

        # Allow the user to choose by inputting the corresponding number in the run_menu() method.
        self.choices = {
            "1": self.user_create_contact,
            "2": self.user_read_contact,
            "3": self.user_update_contact,
            "4": self.user_delete_contact,
            "5": self.size,
            "6": self.search_by_firstname,
            "7": self.search_by_lastname,
            "8": self.search_by_mobile,
            "9": self.search_by_companyname,
            "10": self.print_addressbook,
            "q": self.quit

        }

    def show_options(self):
        # Show the options to the user to allow them to make a choice.
        print(f"Welcome to the company addressbook where you can store up to {self.get_max_num_contacts()} contacts !")
        print("""
            Address Book Menu. 
            What would you like to do?  
            
            1. Create a contact (C)
            2. View a contact (R)
            3. Update a contact (U)
            4. Delete a contact (D) 
            5. Check the size of the contact book 
            6. Search for a contact by first name 
            7. Search for a contact by last name 
            8. Search for a mobile number 
            9. Search for a company name
            10. Print the entire addressbook
            Press q to quit  
            
            """)

    def run_menu(self):
        """
        This method will run in an infinite loop and allow the user to carry out full
        functionality of the addressbook by inputting their chosen task.
        """
        while True:
            self.show_options()
            user_choice = input("Choose an option  ")
            action = self.choices.get(user_choice)
            print(action())

    def quit(self):
        """This will break out of the menu loop when corresponding value is entered"""

        exit_message = "Thank you for using the contact book, have a great day! "

        print(exit_message)
        sys.exit(0)

    def user_create_contact(self):
        """
        This method builds on the add method from the backend. It allows user input to create new
        contacts from interaction with the console menu and adds the new contact to the addressbook.
        """
        # First checks if the book is full. If it isn't the user can add a new contact to the book.
        if self.get_max_num_contacts() <= self.current_num_contacts:
            print("The Address Book is full, you cannot enter any more contacts. ")
        else:
            while True:
                name = input("Please enter a firstname ")
                lastname = input("Please enter a lastname ")
                company = input("Please enter a company ")
                email = input("Please enter an email address ")
                mob = input("Please enter a mobile number ")
                land = input("Please enter a landline ")

                contact_object = Contact(name, lastname, company, email, mob, land)
                self.add(contact_object)
                self.current_num_contacts += 1
                continue_input = input("\nDo you want to add another contact: yes/no ")
                if continue_input.lower() == 'no':
                    break
                else:
                    if self.get_max_num_contacts() <= self.current_num_contacts:
                        print("The Address Book is full, you cannot enter any more contacts. ")
                        break
                    continue

    def user_read_contact(self):
        """
        This method builds on the view method from the backend and allows the user to input the
        list location of what contact they want to view.
        """
        # Print the names of contacts next to their corresponding number in the list
        names = [contact.firstname for contact in self.contact_list]
        for contact_number in range(len(self.contact_list)):
            print(contact_number + 1, names[contact_number])

        # Ask the user for input and pass to the view method.
        user_input = int(input("What number contact do you want to view? "))
        return self.view(user_input)

    def user_update_contact(self):
        """
        This method builds on the update method of the backend and allows for user input through
        interaction with the console.
        """
        names = [contact.firstname for contact in self.contact_list]
        for contact_number in range(len(self.contact_list)):
            print(contact_number + 1, names[contact_number])
        # Ask the user to input the position in the book (list) of what contact needs updating
        contact_position = int(input("Please enter the position of the contact you want to update. "))

        # Ask the user to input the details for the updated contact 
        print("Please supply the details for the updated contact. ")
        name = input("Please enter a firstname ")
        lastname = input("Please enter a lastname ")
        company = input("Please enter a company ")
        email = input("Please enter an email address ")
        mob = input("Please enter a mobile number ")
        land = input("Please enter a landline ")

        # Add the input values to a contact object
        updated_contact_object = Contact(name, lastname, company, email, mob, land)

        # Use the update method from the backend to update the contact in the contact list
        return self.update(contact_position, updated_contact_object)

    def user_delete_contact(self):
        """
        This method allows the user to input which contact they want to delete,
        """
        names = [contact.firstname for contact in self.contact_list]
        for contact_number in range(len(self.contact_list)):
            print(contact_number + 1,names[contact_number])
        contact_position = int(input("Please enter the position of the contact you want to delete. "))
        return self.delete(contact_position)