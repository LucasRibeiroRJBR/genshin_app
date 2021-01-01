from tkinter import *
import tkinter.ttk as ttk
import pyglet
import pygame

pygame.init()

def sound():
    pygame.mixer.music.load("sound/element.mp3")
    pygame.mixer.music.play()

root = Tk()
root.geometry("750x300")
root.resizable(False,False)
root.config(bg="#202020")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

pyglet.font.add_file("font/HYWenHei.ttf")

style = ttk.Style()
style.theme_use('clam')
style.configure('my.TButton', background = "#202020", relief=FLAT, padding=0)

container = Frame(root, background="#202020")
container.grid(row=0, column=0)

# IMAGES
bow = PhotoImage(file="img/Weapons/bow.png")
catalyst = PhotoImage(file="img/Weapons/catalyst.png")
claymore = PhotoImage(file="img/Weapons/claymore.png")
polearm = PhotoImage(file="img/Weapons/polearm.png")
sword = PhotoImage(file="img/Weapons/sword.png")

letreiro = ttk.Label(container, text="Weapons", font=("HYWenHei-85W", 25), foreground="White", background="#202020")
letreiro.grid(row=0, columnspan=7)

bt_bow = ttk.Button(container, image=bow, style="my.TButton", command=sound)
bt_catalyst = ttk.Button(container, image=catalyst, style="my.TButton", command=sound)
bt_claymore = ttk.Button(container, image=claymore, style="my.TButton", command=sound)
bt_polearm = ttk.Button(container, image=polearm, style="my.TButton", command=sound)
bt_sword = ttk.Button(container, image=sword, style="my.TButton", command=sound)

bt_bow.grid(row=1,column=0)
bt_catalyst.grid(row=1,column=1)
bt_claymore.grid(row=1,column=2)
bt_polearm.grid(row=1,column=3)
bt_sword.grid(row=1,column=4)

root.mainloop()
