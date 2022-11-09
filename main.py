from backend import Contact, Addressbook
from frontend import Interface
"""
If there is an issue with the venv not importing the fpdf module, please type the following in the terminal: 
pip install -r requirements.txt 
"""

# Manually instantiating 10 contact objects
bruce = Contact("Bruce", "Wayne", "Wayne Enterprises", "bw@gmail.com", "2345423", "0862324323")
jack = Contact("Jack", "Dawson", "JD Art", "jd@gmail.com", "9889323", "0873242352")
danny = Contact("Daenerys", "Targaryen", "Dragon Rental", "dt@gmail.com", "234324", "0852342341")
tommy = Contact("Thomas", "Shelby", "Shelby Company Ltd", "ts@hotmail.com", "234324", "0832344324")
barney = Contact("Barney", "Stinson", "Goliath National Bank", "stinson@yahoo.com", "098234", "0872344234")
rachel = Contact("Rachel", "Greene", "Macy's", "rg@outlook.com", "090345", "0892344325")
elvis = Contact("Elvis", "Presley", "LV Hilton", "ep@outlook.com", "928433", "0852342585")
harvey = Contact("Harvey", "Specter", "Pearson Hardman", "hs@gmail.com", "324432", "08723453245")
james = Contact("James", "Bond", "MI6", "jb@gmail.com", "2344234","0872344325")
jason = Contact("Jason", "Bourne", "CIA", "jas_b@gmail.com", "234324", "0852344356")

# Instantiating the Addressbook object
address_book = Addressbook()

# Storing the contact objects in a list in the Address book
address_book.add(bruce)
address_book.add(jack)
address_book.add(danny)
address_book.add(tommy)
address_book.add(barney)
address_book.add(rachel)
address_book.add(elvis)
address_book.add(harvey)
address_book.add(james)

"""
The following code will run the command line interface that allows for user interaction
"""

# Option list is quite long, scroll up or enlarge the terminal to see the output of the previous method you input.
# Otherwise, you will just see the options again as the standard terminal screen is quite small.
# I'm sure you already know this but better safe than sorry :)

# Instantiating the console, takes a list as an argument.
company_addressbook_console = Interface(address_book.contact_list)
if __name__ == '__main__':
    company_addressbook_console.run_menu()
