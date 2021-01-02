from tkinter import *
import tkinter.ttk as ttk
import pyglet
import pygame
import util.images


pygame.init()


def sound():
    pygame.mixer.music.load("sound/element.mp3")
    pygame.mixer.music.play()


def aanemo():
    pygame.mixer.music.load("sound/element.mp3")
    pygame.mixer.music.play()
    exec("l = ttk.Button(container_char, image=util.images.get('jean'), style='my.TLabel', command=sound).grid(row=0,column=0)\n"
         "l = ttk.Button(container_char, image=util.images.get('sucrose'), style='my.TLabel', command=sound).grid(row=0,column=1)\n"
         "l = ttk.Button(container_char, image=util.images.get('traveler_Anemo'), style='my.TLabel', command=sound).grid(row=0,column=2)\n"
         "l = ttk.Button(container_char, image=util.images.get('venti'), style='my.TLabel', command=sound).grid(row=0,column=3)\n"
         "l = ttk.Button(container_char, image=util.images.get('xiao'), style='my.TLabel', command=sound).grid(row=0,column=4)")


def ccryo():
    pygame.mixer.music.load("sound/element.mp3")
    pygame.mixer.music.play()
    exec("l = ttk.Button(container_char).grid(row=0,column=0)\n"
         "l.destroy()\n"
         "l = ttk.Button(container_char, image=util.images.get('chongyun'), style='my.TLabel', command=sound).grid(row=0,column=0)\n"
         "l = ttk.Button(container_char, image=util.images.get('diona'), style='my.TLabel', command=sound).grid(row=0,column=1)\n"
         "l = ttk.Button(container_char, image=util.images.get('kaeya'), style='my.TLabel', command=sound).grid(row=0,column=2)\n"
         "l = ttk.Button(container_char, image=util.images.get('qiqi'), style='my.TLabel', command=sound).grid(row=0,column=3)")


root = Tk()
root.geometry("600x500")
# root.resizable(False,False)
root.config(bg="#202020")
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

pyglet.font.add_file("font/HYWenHei.ttf")

style = ttk.Style()
style.theme_use('clam')
style.configure('my.TButton', background="#202020", relief=FLAT, padding=0, bordercolor="#202020", borderwidth=-1)
style.configure('my.TLabel', padding=0, boderwidth=0, background="#202020", borderwidth=-1)

container = Frame(root, background="#202020")
container.grid(row=0, column=0)

letreiro = ttk.Label(container, text="Elements", font=("HYWenHei-85W", 25), foreground="White", background="#202020")
letreiro.grid(row=0, columnspan=7)

bt_anemo = ttk.Button(container, image=util.images.get('anemo'), style="my.TButton", command=aanemo)
bt_cryo = ttk.Button(container, image=util.images.get('cryo'), style="my.TButton", command=ccryo)
bt_dendro = ttk.Button(container, image=util.images.get('dendro'), style="my.TButton", command=sound)
bt_electro = ttk.Button(container, image=util.images.get('electro'), style="my.TButton", command=sound)
bt_geo = ttk.Button(container, image=util.images.get('geo'), style="my.TButton", command=sound)
bt_hydro = ttk.Button(container, image=util.images.get('hydro'), style="my.TButton", command=sound)
bt_pyro = ttk.Button(container, image=util.images.get('pyro'), style="my.TButton", command=sound)

bt_pyro.grid(row=1, column=0)
bt_hydro.grid(row=1, column=1)
bt_anemo.grid(row=1, column=2)
bt_electro.grid(row=1, column=3)
bt_dendro.grid(row=1, column=4)
bt_cryo.grid(row=1, column=5)
bt_geo.grid(row=1, column=6)

container_char = Frame(root, background="#202020")
container_char.grid(row=1, column=0)

l_vazio = ttk.Label(container_char, image=util.images.get('vazio'), style="my.TLabel").grid(row=0, column=0)

root.mainloop()
