from fpdf import FPDF  # External module; pip install in terminal if not present in your venv

"""
This file contains the code which will generate a pdf of the contact book should the use request to do so
when they input 'q' to quit the program. If you don't have fpdf imported, and don't want to import it, simply 
click 'n' when asked to generate a pdf report when quitting out of the program. 

If you want to generate a pdf of the contact book, type the following into terminal: 
pip install -r requirements.txt 
"""


class PDFReport:
    def __init__(self,filename):
        self.filename = filename

    def generate(self, contact_list):
        pdf = FPDF(orientation='P',unit='pt',format='A4')

        pdf.add_page()

        # Add the telephone icon to the pdf
        pdf.image('telephone.png',w=60,h=60)

        # Set the font for the title
        pdf.set_font('Arial','B',14)

        # Insert the title
        pdf.cell(w=0,h=40,txt='Contact Book',align='C',ln=1)

        # Insert the contact heading
        pdf.cell(w=110,h=40,txt='Contacts: ',ln=1)

        # Change the font for the individual contacts, so it looks cleaner
        pdf.set_font(family='Arial',size=12)

        # Loop over the contact list and add the details for each contact object to the pdf
        for contact in contact_list:
            pdf.cell(w=110, h=20,txt="Firstname: ")
            pdf.cell(w=110,h=20,txt=contact.firstname,ln=1)

            pdf.cell(w=110, h=20,txt="Lastname: ")
            pdf.cell(w=110,h=20,txt=contact.lastname,ln=1)

            pdf.cell(w=110, h=20,txt="Email: ")
            pdf.cell(w=110,h=20,txt=contact.email,ln=1)

            pdf.cell(w=110, h=20,txt="Company: ")
            pdf.cell(w=110, h=20,txt=contact.company,ln=1)

            pdf.cell(w=110, h=20,txt="Mobile Number: ")
            pdf.cell(w=110,h=20,txt=contact.mobile_num,ln=1)

            pdf.cell(w=110, h=20,txt="Landline: ")
            pdf.cell(w=110,h=20,txt=contact.landline,ln=1)

            pdf.cell(w=110,h=40,ln=1)

        # Generate the pdf
        pdf.output(self.filename)