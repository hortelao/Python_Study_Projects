from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import cryptocode

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password_text = password_input.get()
    encoded = cryptocode.encrypt(password_text, "my_password")
    new_data = {
        website: {
            "email": email_username,
            "password": encoded
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            email_username_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    website = website_input.get()

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found!")
    else:
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"Email/Username: {data[website]['email']}\n"
                                        f"Password: {cryptocode.decrypt(data[website]['password'], 'my_password')}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

my_pass_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=my_pass_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky='nesw')

email_username_input = Entry(width=52)
email_username_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
