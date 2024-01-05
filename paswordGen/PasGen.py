import secrets
import string
from tkinter import *
from ttkbootstrap import *
from json import *
import ttkbootstrap as tb
import socket
import time
import json



def Get_Site():
    Site = PostText.get()
    password = generate_password()
    print("Generated Password:", password)
    save_password(Site, password)



def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password(website, password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(f"Website/App: {website}\nPassword: {password}\n\n")



root = tb.Window(themename="darkly")

#root = Tk()
root.title("PasGen")
root.geometry('750x500')

Screens = tb.Notebook(root, bootstyle="dark", width=675, height=424)
Screens.pack(pady=20)

GenTab = tb.Frame(Screens)
PasTab = tb.Frame(Screens)

my_canvas = Canvas(GenTab)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scroll_bar = tb.Scrollbar(GenTab, orient=VERTICAL, command=my_canvas.yview)
my_scroll_bar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scroll_bar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

TabInRecipeTab = Frame(my_canvas, )

my_canvas.create_window((0,0), window=TabInRecipeTab, anchor="nw")


label1 = Label(PasTab, text="Enter where your Pasword is for", font=("Bookman Old Style", 18))
label1.pack(pady=20)

PostText = Entry(PasTab)
PostText.pack(pady=10, padx=10)


MakeB = tb.Button(PasTab, text="Make Pasword", bootstyle="danger outline", command = Get_Site)
MakeB.pack(pady=20)


my_label2 = Label(TabInRecipeTab, text="Paswords", font=("Bookman Old Style", 28))
my_label2.pack(pady=20, padx=265)


# Add our frames to the notebook
Screens.add(PasTab, text="PotTab")
Screens.add(GenTab, text="GenTab")


root.mainloop()
