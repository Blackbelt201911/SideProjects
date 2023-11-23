from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as tb


def PostFunc():
    global PostingText
    PostingText = PostText.get(1.0, "end-1c")
    print(PostingText)

    RecpieLable = Label(TabInRecipeTab, text = PostingText, font =('Courier', 24))  
    RecpieLable.pack()  


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

my_scroll_bar = ttk.Scrollbar(RecipieTab, orient=VERTICAL, command=my_canvas.yview)
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



root.mainloop()

