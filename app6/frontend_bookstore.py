"""
    A program that will store the following book information
    Title, Author
    Year, ISBN

    The User can:
    View all the records
    Serachan entry
    Add entry
    Update entry
    Delete 
    Close


    Pages read ? or Just read ?
    Rating



"""
from tkinter import *
import backend_bookstore

# wrapper functions
# can help to identify sql injections
# and run functions from the backend as they cannot be
# called with their brackets

"""
        the view_command is a wrapper function from the backend running 
        the view_book function and will first clear the listbox and then
        iterate the rows in the dbase and insert them in the listbox
"""


def view_command():
    listbox1.delete(0, END)
    for row in backend_bookstore.view_book():
        listbox1.insert(END, row)
        # the  data (tuple is inserted at the end of the row)


"""
        the search_command(wrapper function) will first clear the listbox 
        It will search for a book using the entries from the entry boxes 
        It uses the get method to get the string from the entry boxes
"""


def search_command():
    listbox1.delete(0, END)
    for row in backend_bookstore.search_book(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get()):
        listbox1.insert(END, row)


"""
        the add-command (wrapper function for populate_bookstore)
        will add books to the dbase.
        it will use get method to fetch the user input in the entry boxes 
        then clear the entries and will then populate the listboxes
"""


def add_command():
    backend_bookstore.populate_bookstore(
        title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    listbox1.delete(0, END)
    listbox1.insert(END, (title_entry.get(), author_entry.get(),
                          year_entry.get(), isbn_entry.get()))


"""
        get_selected_rows command is used to listen to 
        the mouse event of a selected row in the listbox
        selected_tuple variable is created with a global scope in order 
        for it to be accessed outside the function.
        the cursor selection index 0 is stored in the index variable and will
        then used to get its string variables .
        The entry boxes are first cleared and will then be poulated
        using the various indices accordingly
"""


def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox1.curselection()[0]
        selected_tuple = listbox1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
    except IndexError:
        pass


"""
        delete_commandn(wrapper func for delete book) is used 
        to delete a book on cursor selection
"""


def delete_command():
    backend_bookstore.delete_book(selected_tuple[0])


"""
        update_command is used to update t=book details
        it will first get a selected row in the listbox and populate the
        entry boxes accordingly upon which the used will then change the details
        
"""


def update_command():
    backend_bookstore.update_book(
        selected_tuple[0], title_entry.get(), author_entry.get(),
        year_entry.get(), isbn_entry.get())


window = Tk()

window.wm_title("BookStore")

# creating labels
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

# creating text entry boxes
title_entry = StringVar()
entry1 = Entry(window, textvariable=title_entry)
entry1.grid(row=0, column=1)

year_entry = StringVar()
entry2 = Entry(window, textvariable=year_entry)
entry2.grid(row=1, column=1)

author_entry = StringVar()
entry3 = Entry(window, textvariable=author_entry)
entry3.grid(row=0, column=3)

isbn_entry = StringVar()
entry4 = Entry(window, textvariable=isbn_entry)
entry4.grid(row=1, column=3)


# creating a listbox and setting its dimensions
listbox1 = Listbox(window, height=6, width=35)
listbox1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)

# the scrollbar is configured to scroll along the set of the listbox
listbox1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=listbox1.yview)

# This will listen to the seleted item in the listbox
#  and the call the get_selected_row function
listbox1.bind('<<ListboxSelect>>', get_selected_row)

# creating buttons
button1 = Button(window, text="View All", width=12, command=view_command)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search", width=12, command=search_command)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add Entry", width=12, command=add_command)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update Selected",
                 width=12, command=update_command)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete Selected",
                 width=12, command=delete_command)
button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=12, command=window.destroy)
button6.grid(row=7, column=3)

window.mainloop()
