from tkinter import *
# Import everything from the tkinter library


window = Tk()
window.title("Convert Weight")
# Give the window a title


def convert_weight_from_kg():
    grams = float(e1_value.get()) * 1000
    text1.insert(END, grams)
    # the above function will get the float of e1_value
    # it will then insert grams in the end of the text1

    pounds = float(e1_value.get()) * 2.20462
    text2.insert(END, pounds)

    ounces = float(e1_value.get()) * 35.274
    text3.insert(END, ounces)


label1 = Label(window, text="Kilograms")
label1.grid(row=0, column=0)
# creating a label and giving it an appropriate position

e1_value = StringVar()
entry1 = Entry(window, textvariable=e1_value)
entry1.grid(row=0, column=1)

label2 = Label(window, text="Grams")
label2.grid(row=1, column=0)

text1 = Text(window, height=1, width=20)
text1.grid(row=1, column=1)

label3 = Label(window, text="Pounds")
label3.grid(row=2, column=0)

text2 = Text(window, height=1, width=20)
text2.grid(row=2, column=1)

label4 = Label(window, text="Ounces")
label4.grid(row=3, column=0)

text3 = Text(window, height=1, width=20)
text3.grid(row=3, column=1)


button1 = Button(window, text="Convert", command=convert_weight_from_kg)
button1.grid(row=4, column=2, rowspan=2)


window.mainloop()
