from tkinter import *

window = Tk()
# Tk is the class we use to create the main window of our application

# code to add widgets will go here


# class myFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A Simple Python GUI")

#         self.label = Label(master, text="This is our Very First GUI !!")
#         self.label.pack()

#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()

#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()

#     def greet(self):
#         print("Greetings!!")


# mygui = myFirstGUI(window)


def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)


b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
