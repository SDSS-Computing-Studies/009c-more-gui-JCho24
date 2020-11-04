import tkinter as tk
from tkinter import *
import math

win = tk.Tk()
win.title("tk")
win.geometry("500x350")

answer = StringVar()
answer.set("Area = _____")

def calculate():
    side1 = s1.get()
    side2 = s2.get()
    side3 = s3.get()
    height = h.get()
    print(side1)
    print(side2)
    print(side3)
    print(height)
    

    if height == "":
        side1 = float(side1)
        side2 = float(side2)
        side3 = float(side3)

        t = ((side1 + side2 + side3)/2)
        area = ((t - side1) * (t - side2) * (t - side3))
        area = t * area
        area = math.sqrt(area)

        answer.set(area)
        
    
    else:
        side2 = float(side2)
        height = float(height)

        area = (side2 * height) / 2
        
        answer.set(area)
    

trianglephoto = PhotoImage(file = "triangle.png")
tri = Label(win, image = trianglephoto)
l1 = Label(win, text = "   Enter in as much information about the   \ntriangle shown and I will calculate the area")
b1 = Button(win, text = "Calculate!", command = calculate)
s1 = Entry(win, width = 7)
s2 = Entry(win, width = 7)
s3 = Entry(win, width = 7)
h = Entry(win, width = 7)
ans = Label(win, textvariable = answer)


tri.place(x = 0, y = 0)
l1.place(x = 0, y = 275)
b1.place(x = 275, y = 275)
s1.place(x = 175, y = 100)
s2.place(x = 230, y = 240)
s3.place(x = 400, y = 140)
h.place(x = 300, y = 130)
ans.place(x = 280, y = 300)


win.mainloop()
