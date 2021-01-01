from tkinter import *

root = Tk()
root.geometry('300x200')
root.columnconfigure(0, weight=1)   # Set weight to row and 
root.rowconfigure(0, weight=1)      # column where the widget is

container = Frame(root, bg='tan')   # bg color to show extent
container.grid(row=0, column=0)     # Grid cell with weight

# A couple of widgets to illustrate the principle.
b1 = Button(container, text='First', width=10)
b1.grid(pady=10, padx=20)
b2 = Button(container, text='second', width=10)
b2.grid(pady=(0,10), padx=20)

root.mainloop()