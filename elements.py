from tkinter import *
import tkinter.ttk as ttk
import pyglet
import pygame


pygame.init()


def sound():
    pygame.mixer.music.load("sound/element.mp3")
    pygame.mixer.music.play()


def ccryo():
    pygame.mixer.music.load("sound/element.mp3")
    pygame.mixer.music.play()
    exec("l = ttk.Button(container_char, image=cryo, style='my.TLabel', command=sound).grid(row=0,column=0)")


root = Tk()
root.geometry("600x500")
# root.resizable(False,False)
root.config(bg="#202020")
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

pyglet.font.add_file("font/HYWenHei.ttf")

style = ttk.Style()
style.theme_use('clam')
style.configure('my.TButton', background="#202020", relief=FLAT, padding=0)
style.configure('my.TLabel', padding=0, boderwidth=0, background="#202020")

container = Frame(root, background="#202020")
container.grid(row=0, column=0)

# IMAGES
anemo = PhotoImage(file="img/Elements/Anemo.png")
cryo = PhotoImage(file="img/Elements/Cryo.png")
dendro = PhotoImage(file="img/Elements/Dendro.png")
electro = PhotoImage(file="img/Elements/Electro.png")
geo = PhotoImage(file="img/Elements/Geo.png")
hydro = PhotoImage(file="img/Elements/Hydro.png")
pyro = PhotoImage(file="img/Elements/Pyro.png")
vazio = PhotoImage(file="img/vazio.png")

letreiro = ttk.Label(container, text="Elements", font=(
    "HYWenHei-85W", 25), foreground="White", background="#202020")
letreiro.grid(row=0, columnspan=7)

bt_anemo = ttk.Button(container, image=anemo,
                      style="my.TButton", command=sound)
bt_cryo = ttk.Button(container, image=cryo, style="my.TButton", command=ccryo)
bt_dendro = ttk.Button(container, image=dendro,
                       style="my.TButton", command=sound)
bt_electro = ttk.Button(container, image=electro,
                        style="my.TButton", command=sound)
bt_geo = ttk.Button(container, image=geo, style="my.TButton", command=sound)
bt_hydro = ttk.Button(container, image=hydro,
                      style="my.TButton", command=sound)
bt_pyro = ttk.Button(container, image=pyro, style="my.TButton", command=sound)

bt_pyro.grid(row=1, column=0)
bt_hydro.grid(row=1, column=1)
bt_anemo.grid(row=1, column=2)
bt_electro.grid(row=1, column=3)
bt_dendro.grid(row=1, column=4)
bt_cryo.grid(row=1, column=5)
bt_geo.grid(row=1, column=6)

container_char = Frame(root, background="#202020")
container_char.grid(row=1, column=0)

l_vazio = ttk.Label(container_char, image=vazio,
                    style="my.TLabel").grid(row=0, column=0)

root.mainloop()
