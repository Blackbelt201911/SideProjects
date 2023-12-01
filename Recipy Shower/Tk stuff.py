from tkinter import *
from ttkbootstrap import *
from json import *
import ttkbootstrap as tb
import socket
import time
import json

PORT = 5050 #Where to concte to 
SERVER = socket.gethostname() #what ip to conect to
ADDR = (SERVER, PORT) # Port and sever in one varbile
FORMAT = "utf-8" # to make sure no viruse hehe
DISCONNECT_MESSAGE = "!DISCONNECT" # self explaintory
MESSAGE = "Hello World" # self explaintory

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #gets this device info and saves it
    client.connect(ADDR) #conctes to addr(Port and sever) using clint info
    return client # idk

connection = connect()

def send(client, msg): # letes you send stuff
    message = msg.encode(FORMAT)
    client.send(message)


def start(): # self explaintory
    answer = input('Would you like to connect (yes/no)? ')
    if answer.lower() != 'yes':
        return
    send(connection, MESSAGE)
    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            break
        

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')


def PostFunc():
    global PostingText
    PostingText = PostText.get(1.0, "end-1c")
    print(PostingText)

    RecpieLable = Label(TabInRecipeTab, text = PostingText, font =('Courier', 18))  
    RecpieLable.pack()  

    FStrText = (f"{PostingText}")

    send(connection, FStrText)

root = tb.Window(themename="darkly")

#root = Tk()
root.title("Just like Mama's")
root.geometry('750x500')

Screens = tb.Notebook(root, bootstyle="dark", width=675, height=424)
Screens.pack(pady=20)

PostTab = tb.Frame(Screens)
RecipieTab = tb.Frame(Screens)

my_canvas = Canvas(RecipieTab)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scroll_bar = tb.Scrollbar(RecipieTab, orient=VERTICAL, command=my_canvas.yview)
my_scroll_bar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scroll_bar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

TabInRecipeTab = Frame(my_canvas, )

my_canvas.create_window((0,0), window=TabInRecipeTab, anchor="nw")


label1 = Label(PostTab, text="Enter your Recipie", font=("Bookman Old Style", 18))
label1.pack(pady=20)

PostText = Text(PostTab, width=70, height=10)
PostText.pack(pady=10, padx=10)


PostBT = tb.Button(PostTab, text="Post", bootstyle="danger outline", command = PostFunc)
PostBT.pack(pady=20)


my_label2 = Label(TabInRecipeTab, text="Recipies", font=("Bookman Old Style", 28))
my_label2.pack(pady=20, padx=265)


# Add our frames to the notebook
Screens.add(PostTab, text="PotTab")
Screens.add(RecipieTab, text="RecipieTab")

start()

root.mainloop()

