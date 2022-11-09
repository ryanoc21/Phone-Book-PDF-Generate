"""
This is the code for the backend of CA1.
It contains the two main classes that will allow for the functionality of the program.
"""


class Contact:
    """
    This class will define the attributes required for the contacts that will be contained in the address book,
    as specified in the assignment brief.
    """

    def __init__(self, firstname, lastname, company, email, landline, mobile_num):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.email = email
        self.landline = landline
        self.mobile_num = mobile_num


class Addressbook:
    def __init__(self):
        self.contact_list = []

        # Setting the maximum number of contacts allowed in the address book
        self.__max_num_contacts = 12  # private instance variable

    """Getter and Setter for the max number of contacts allowed in the addressbook"""

    def get_max_num_contacts(self):
        return self.__max_num_contacts

    def set_max_num_contacts(self, max_num):
        self.__max_num_contacts = max_num

    def add(self, contact_object):
        """
        This method takes a contact object as a parameter and appends it to the list that stores
        the data for the addressbook.
        """
        self.contact_list.append(contact_object)

    def delete(self, index):
        """
        This method will delete contact based on their index position from the address book.
        The list method pop is used to do this.
        """
        self.contact_list.pop(index - 1)

    def view(self, index):
        """
        This method takes the position of a contact object in the addressbook list as a paramter.
        It then displays all the information for that particular object
        """
        contact = self.contact_list[int(index) - 1]

        print('Name:', contact.firstname, contact.lastname, '\n',
              'Company:', contact.company, '\n', 'Email:', contact.email, '\n',
              'Landline:', contact.landline, '\n', 'Mobile Number:', contact.mobile_num)

    def update(self, index, updated_contact_object):
        """
        Takes the index position of the contact the user wants to update and the
        object they want to replace it with as parameters. Adds the updates object to
        the contact list.
        """
        self.contact_list[index - 1] = updated_contact_object

    def size(self):
        """
        Prints the size of the list using the len function and interpolation.
        """
        print(f"There are {len(self.contact_list)} contacts in the address book")

    def search_by_firstname(self):
        """
        This method will prompt the user to input a firstname,
        check for its presence in the contact book list using any() function and, if found, print the information
        of all contacts in the program who have that first name.
        """
        name = input("Please input the name you want to search. ")
        print(f"Is the firstname {name} in the address book? ")
        print("Searching....")

        if any(contact.firstname.lower() == name.lower() for contact in self.contact_list):
            print(f"Yes, the firstname {name} is in the address book, here are their details")
        else:
            print(f"No, the firstname {name} is not in the address book. ")

        for contact in self.contact_list:
            if contact.firstname.lower() == name.lower():
                print(contact.firstname, contact.lastname,
                      contact.company, contact.email,
                      contact.mobile_num, contact.landline, '\n')
                continue

    def search_by_lastname(self):
        """
        This method will prompt the user to input a last name,
        check for its presence in the contact book list using any() function and, if found, print the information
        of all contacts in the program who have that last name.
        """
        lastname = input("Please input the last name you want to search for. ")
        print(f"Is the lastname {lastname} in the address book? ")

        if any(contact.lastname.lower() == lastname.lower() for contact in self.contact_list):
            print(f"Yes, the lastname {lastname} is in the address book, here are their details.")
        else:
            print(f"No, the lastname {lastname} is not in the address book. ")

        for l_name in self.contact_list:
            if l_name.lastname.lower() == lastname.lower():
                print(l_name.firstname, l_name.lastname,
                      l_name.company, l_name.email,
                      l_name.mobile_num, l_name.landline, '\n')
                continue

    def search_by_companyname(self):
        """
        This function will prompt the user for an input of a company name,
        check if a contact matching the company name is in the phone book using the any() function.
        If the company name is found to be in the contact book, the details of all the contacts who
        work at that company will be printed.
        """
        companyname = input("Please input the company name you want to search for. ")
        print(f"Checking to see if the company {companyname} is in the address book...")

        if any(contact.company.lower() == companyname.lower() for contact in self.contact_list):
            print(f"Yes, the company {companyname} is in the address book, here are their details.")
        else:
            print(f"No, the company name {companyname} is not  in the address book")

        for comp_name in self.contact_list:
            if comp_name.company.lower() == companyname.lower():
                print(comp_name.firstname, comp_name.lastname,
                      comp_name.company, comp_name.email,
                      comp_name.mobile_num, comp_name.landline, '\n')

    def search_by_mobile(self):
        """
        This method will prompt the user to input a mobile number.
        The any() function passed into a conditional statement will check to see if the number is in the book.
        If the number is found, the details of the contact who owns that number will be printed.
        """
        mobile_number = input("Please insert the mobile number you want to search for. ")
        print(f"Checking to see if the mobile number {mobile_number} is in the address book...")

        if any(number.mobile_num.lower() == mobile_number.lower() for number in self.contact_list):
            print(f"Yes, the mobile number {mobile_number} is in the address book, here are the owner's details")
        else:
            print(f"No, the mobile number {mobile_number} is not in the address book ")

        for mob_num in self.contact_list:
            if mob_num.mobile_num == mobile_number:
                print(mob_num.firstname, mob_num.lastname,
                      mob_num.company, mob_num.email,
                      mob_num.landline, mob_num.mobile_num, '\n')

    def print_addressbook(self):
        """
        This method will print all the contacts in the address book.
        """
        print("Here is the full addressbook \n")
        for full_details in self.contact_list:
            print('Name: ', full_details.firstname, '\n',
                  'Lastname: ', full_details.lastname, '\n',
                  'Company: ', full_details.company,'\n',
                  'Email: ', full_details.email,'\n',
                  'Landline: ', full_details.landline,'\n',
                  'Mobile: ', full_details.mobile_num,'\n',
                  '---------------------------------- \n')