from tkinter import *
import tkinter as tk
import ttkbootstrap as tb


def PostFunc():
    inp = PostText.get(1.0, "end-1c")
    print(inp)



root = tb.Window(themename="darkly")

#root = Tk()
root.title("Just like Mama's")
root.geometry('720x500')

Screens = tb.Notebook(root, bootstyle="dark")
Screens.pack(pady=20)

PostTab = tb.Frame(Screens)
Recipies = tb.Frame(Screens)



my_scroll = tb.Scrollbar(Recipies, orient='vertical', bootstyle="dark round")
my_scroll.pack(side="right", fill="y")


label1 = Label(PostTab, text="Enter your Recipies", font=("Helvetica", 18))
label1.pack(pady=20)

PostText = Text(PostTab, width=70, height=10)
PostText.pack(pady=10, padx=10)


PostBT = tb.Button(PostTab, text="Post", bootstyle="danger outline", command = PostFunc)
PostBT.pack(pady=20)


my_label2 = Label(Recipies, text="Recipies", font=("Helvetica", 18))
my_label2.pack(pady=20)

# Add our frames to the notebook
Screens.add(PostTab, text="Poster")
Screens.add(Recipies, text="Recipies")




root.mainloop()

