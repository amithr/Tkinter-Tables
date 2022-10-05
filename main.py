from tkinter import *
from table import generate_table

# https://www.geeksforgeeks.org/create-table-using-tkinter/
# https://www.activestate.com/resources/quick-reads/how-to-display-data-in-a-table-using-tkinter/


main_window = Tk()
contact_information = []

label_1 = Label(main_window, text="Name:")
label_2 = Label(main_window, text="Phone Number:")
label_3 = Label(main_window, text="Email Address:")

name_field = Entry()
phone_number_field = Entry()
email_field = Entry()

label_1.place(x=50, y=50)
name_field.place(x=250, y=50)

label_2.place(x=50, y=100)
phone_number_field.place(x=250, y=100)

label_3.place(x=50, y=150)
email_field.place(x=250, y=150)

def open_table(name, phone_number, address_field, contact_information):
    contact_information.append([name, phone_number, address_field])
    table_window = Toplevel()
    generate_table(contact_information, table_window)

contact_list_button = Button(main_window, text="Submit", command= lambda: open_table(name_field.get(), phone_number_field.get(), email_field.get(), contact_information))
contact_list_button.place(x=250, y=200)


main_window.geometry('500x300')
main_window.title('Contact Form')
main_window.mainloop()