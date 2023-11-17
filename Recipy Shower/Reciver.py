import tkinter as tk
import time
from tkinter import *
from tkinter import colorchooser
import random




window = tk.Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("test")



class Player:
    def __init__(self, canvas, color):
        self.x = 0
        self.y = 0
        self.canvas = window
        self.id = canvas.create_rectangle(0, 0, 75, 75, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_height()
        self.canvas_width = self.canvas_width * 1.83
        canvas.bind_all('<KeyPress-d>', self.moving_right)
        canvas.bind_all('<KeyPress-a>',self.moving_left)
        canvas.bind_all('<KeyPress-w>', self.moving_up)
        canvas.bind_all('<KeyPress-s>', self.moving_down)




    def moving_right(self, event):
        self.x = 7.5
    def moving_left(self, event):
        self.x = -7.5
    def moving_up(self, event):
        self.y = -7.5
    def moving_down(self, event):
        self.y = 7.5




    def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0 or pos[2] >= self.canvas_width:
                self.x = self.x * -1
            if pos[1] <= 0 or pos[3] >= self.canvas_height:
                self.y = self.y * -1


class Ball:
    def __init__(self, canvas, color, speed, up, player):
        self.x = speed
        self.y = up
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,100,100, fill=color)
        self.canvas.move(self.id, 900, 400)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.player = player
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
             self.x = self.x * -1
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y = self.y * -1
    def hit(self):
        p = self.canvas.coords(self.player.id)
        coll = self.canvas.find_overlapping(p[0], p[1], p[2], p[3])
        hello = list(coll)
        if len(hello) != 1:
            return True
        return False
tk = Tk()
tk.title('Bounce the Game')
tk.resizable(0,0)
tk.wm_attributes()
canvas = Canvas(tk, width=485774776832, height=485774776832, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
player = Player(canvas,'blue')
ball = Ball(canvas, 'purple', 15, 20, player)
pos = canvas.coords(ball.id)
while True:
    if ball.hit() == False:
        player.draw()
        ball.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
