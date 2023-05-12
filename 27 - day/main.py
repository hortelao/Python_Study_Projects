from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 18, "bold"))
my_label.pack()

#Button

def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

button = Button(text="Click Me", font=("Arial", 12, "normal"), command=button_clicked)
button.pack()


#Entry

input = Entry(width=10)
input.pack()




window.mainloop()