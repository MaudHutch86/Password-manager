from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [(random.choice(letters)) for _ in range(random.randint(8, 10))]

    nr_symbols = [(random.choice(symbols)) for _ in range(random.randint(2, 4))]

    nr_numbers = [(random.choice(numbers)) for _ in range(random.randint(2, 4))]

    password_list = nr_letters + nr_symbols + nr_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f" {password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web_data = website_entry.get()
    email_data = email_username_entry.get()
    password_data = password_entry.get()
    if len(web_data) == 0:
        messagebox.showinfo(title="Error", message="The field is empty . You should add a website")

    if len(email_data) == 0:
        messagebox.showinfo(title="Error", message="The field is empty .You should add an email")

    if len(password_data) == 0:
        messagebox.showinfo(title="Error", message="The field is empty . You should add a password")

    else:

        is_ok = messagebox.askokcancel(title=web_data,
                                       message=f"the details entered:\n Email:{email_data} \nPassword: {password_data}"
                                               f"\n Is it ok to save?")
        if is_ok is True:
            with open("data.txt", "a") as data:
                data.write(f"{web_data}|{email_data}|{password_data} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Maud Homebrew Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=36)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "maudafrica@live.fr")

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Pass", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(width=34, text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
