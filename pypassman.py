from tkinter import *
from tkinter import messagebox


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You've entered\nUsername: {username}\nPassword: {password}\nAre you sure you want to save?")
        
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {username} | {password}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

screen = Tk()
screen.config(padx=50,pady=50)
screen.title("Password Manager")
canvas = Canvas(width=500, height=500)
photo = PhotoImage(file="image.png")
canvas.create_image(250,230, image=photo)
canvas.grid(column=1, row=0)

website = Label(text="Website: ")
website.grid(column=0, row=1)
username = Label(text="Username: ")
username.grid(column=0, row=2)
password = Label(text="Password: ")
password.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.insert(0, "Website")
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "Username")

password_entry = Entry(width=35)
password_entry.insert(0, "Password")
password_entry.grid(column=1, row=3, columnspan=2)

#buttons
add_button = Button(text="Store information", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

screen.mainloop()
