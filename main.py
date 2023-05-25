
from tkinter import *
from tkinter import *

from time import strftime

root=Tk()
root.title("clock")
def time():
    string=strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1000,time)

lable = Label(root,font=("s-digital",30),background="black",foreground="cyan")
lable.pack(anchor="center")
time()

mainloop()