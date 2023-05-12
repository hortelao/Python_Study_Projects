from tkinter import *

window = Tk()
window.minsize(width=150, height=40)
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

input_miles = Entry(width=10)
input_miles.grid(column= 1, row= 0)
label1 = Label()
label1["text"] = "Miles"
label1.grid(column= 2, row= 0)

label2 = Label()
label2 ["text"] = "is equal to "
label2.grid(column= 0, row= 1)

label3 = Label()
label3["text"] = 0
label3.grid(column= 1, row= 1)

label4 = Label()
label4 ["text"] = "Km"
label4.grid(column= 2, row= 1)

def calculate():
    miles = input_miles.get()
    calc = int(miles) * 1.609344
    label3["text"] = round(calc, 1)


calculate = Button(command=calculate)
calculate["text"] = "Calculate"
calculate.grid(column= 1, row= 2)

window.mainloop()