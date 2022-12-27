from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    password_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Take inputs in website, email/username and password entry such that when user clicks
# on the add button, figure out how to save data into data.txt in
# website | email | password format
# Tips learn about write()
# insert, delete from tkinter
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    stuff_to_be_added = f"{website} | {email} | {password}\n"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Oops", message="Please don't leave any fields empty!")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}\n"
                                                              f"Is it ok to save?")
    if is_ok:
        with open("/Users/a65911/Downloads/Udemy/Udemy Python/Day 29/password-manager-start/new_file.txt") as file:
            contents = file.read()
        if len(contents) == 0:
            # This is to add the file if it doesn't exit
            with open("/Users/a65911/Downloads/Udemy/Udemy Python/Day 29/password-manager-start/new_file.txt",
                      mode="w") as file_content:
                file_content.write("")
        # # This is to extract
        # with open("/Users/a65911/Downloads/Udemy/Udemy Python/Day 29/password-manager-start/new_file.txt") as file:
        #     contents = file.read()
        with open("new_file.txt", mode="w") as new_content:
            new_content.write(contents + stuff_to_be_added)
        website_entry.delete(0, END)
        email_username_entry.delete(0, END)
        email_username_entry.insert(0, "hikari007.gmail.com")
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website display
website_display = Label(text="Website: ", bg="white", fg="black")
website_display.grid(column=0, row=1)

# Email_Username display
email_username_display = Label(text="Email/Username: ", bg="white", fg="black")
email_username_display.grid(column=0, row=2)

# Password display
password_display = Label(text="Password: ", bg="white", fg="black")
password_display.grid(column=0, row=3)

# Website entry
website_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username entry
email_username_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "hikari007.gmail.com")

# Password entry
password_entry = Entry(bg="white", fg="black", highlightthickness=0, width=19)
password_entry.grid(column=1, row=3)

# Generate Password button
password_button = Button(text="Generate Password", highlightbackground="white", width=12, command=password_generator)
password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", highlightbackground="white", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
