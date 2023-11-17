import tkinter as tk
from tkinter import Entry
from ttkbootstrap import Label
from ttkbootstrap.constants import *
import ttkbootstrap as ttk


window = tk.Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Spanish Conjactor")

Noun_label = Label(window, text = "Noun", font =('Courier', 24))  
Noun_label.pack()  

#make varibles
def All_cal():
   Noun_Entry_text = Noun_Entry.get()
   Verb_Entry_text = Verb_Entry.get()
   print(Noun_Entry_text)
   print(Verb_Entry_text)
   
   string = Verb_Entry_text
   lst = []
 
   for letter in string:
        lst.append(letter)
 
   print(lst)
   
   sup = 0
   res = ''
   c = Noun_Entry_text
   b = Verb_Entry_text
   a = [b]
   d = lst
   cat = len(d)
   dog = cat - 2
   rabbit = d[dog] 
   global output
   
   if c == 'Yo':
      for i in d:
        sup += 1
        res += i
        if sup == dog:
          res = res + 'o'
          output = res
          print(res)
          break
   elif c == 'Tu' and rabbit == 'e':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'es'
                output = res
                print(res)
                break
   elif c == 'Tu' and rabbit == 'a':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'as'
                output = res
                print(res)
                break
   elif c == 'Tu' and rabbit == 'i':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'es'
                output = res
                print(res)
                break
   elif c == 'Ella' or c == 'El' or c == 'Ud.'and rabbit == 'a':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'a'
                output = res
                print(res)
                break  
   elif c == 'Ella' or c == 'El' or c == 'Ud.'and rabbit == 'i':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'e'
                output = res
                print(res)
                break
   elif c == 'Ella' or c == 'El' or c == 'Ud.'and rabbit == 'e':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'e'
                output = res
                print(res)
                break
   elif c == 'Nosotros' and rabbit == 'e':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'emos'
                output = res
                print(res)
                break
   elif c == 'Nosotros' and rabbit == 'a':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'amos'
                output = res
                print(res)
                break
   elif c == 'Nosotros' and rabbit == 'i':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'imos'
                output = res
                print(res)
                break
   elif c == 'Ellas' or c == 'Ellos' or c == 'Uds.'and rabbit == 'e':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'en'
                output = res
                print(res)
                break
   elif c == 'Ellas' or c == 'Ellos' or c == 'Uds.'and rabbit == 'i':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'en'
                output = res
                print(res)
                break
   elif c == 'Ellas' or c == 'Ellos' or c == 'Uds.'and rabbit == 'a':
        for i in d:
            sup += 1
            res += i
            if sup == dog:
                res = res + 'an'
                output = res
                print(res)
                break


   output_lable = Label(window, text = output, font =('Courier', 24))  
   output_lable.pack()  


#Define an Entry widget
Noun_Entry = Entry(window, width= 40)
Noun_Entry.pack(pady=10)

Verb_label = Label(window, text = "Verb", font =('Courier', 24))  
Verb_label.pack() 

Verb_Entry = Entry(window, width= 40)
Verb_Entry.pack(pady=10)

#Create Buttons with proper position
All_but = ttk.Button(window, text= "All Enter", command = All_cal)
All_but.pack()

window.mainloop()