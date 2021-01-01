from tkinter import *
import tkinter.ttk as ttk
import pyglet
import pygame

pygame.init()

def sound():
    pygame.mixer.music.load("sound/element.mp3")
    pygame.mixer.music.play()

root = Tk()
root.geometry("600x300")
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
anemo = PhotoImage(file="img/Elements/Anemo.png")
cryo = PhotoImage(file="img/Elements/Cryo.png")
dendro = PhotoImage(file="img/Elements/Dendro.png")
electro = PhotoImage(file="img/Elements/Electro.png")
geo = PhotoImage(file="img/Elements/Geo.png")
hidro = PhotoImage(file="img/Elements/Hidro.png")
pyro = PhotoImage(file="img/Elements/Pyro.png")

letreiro = ttk.Label(container, text="Elements", font=("HYWenHei-85W", 25), foreground="White", background="#202020")
letreiro.grid(row=0, columnspan=7)

bt_anemo = ttk.Button(container, image=anemo, style="my.TButton", command=sound)
bt_cryo = ttk.Button(container, image=cryo, style="my.TButton", command=sound)
bt_dendro = ttk.Button(container, image=dendro, style="my.TButton", command=sound)
bt_electro = ttk.Button(container, image=electro, style="my.TButton", command=sound)
bt_geo = ttk.Button(container, image=geo, style="my.TButton", command=sound)
bt_hidro = ttk.Button(container, image=hidro, style="my.TButton", command=sound)
bt_pyro = ttk.Button(container, image=pyro, style="my.TButton", command=sound)

bt_pyro.grid(row=1,column=0)
bt_hidro.grid(row=1,column=1)
bt_anemo.grid(row=1,column=2)
bt_electro.grid(row=1,column=3)
bt_dendro.grid(row=1,column=4)
bt_cryo.grid(row=1,column=5)
bt_geo.grid(row=1,column=6)

root.mainloop()
