from tkinter import *
from tkinter import ttk as ttk
import pyglet
import util.images

root = Tk()
root.resizable(False, False)
root.config(bg="#202020")

style = ttk.Style()
style.theme_use('clam')
style.configure('my.TButton', background="#202020", relief=FLAT, padding=0)
style.configure('my.TLabel', padding=20)

pyglet.font.add_file("font/HYWenHei.ttf")


letreiro = ttk.Label(root, text="Characters", font=(
    "HYWenHei-85W", 25), foreground="White", background="#202020", style='my.TLabel').grid(row=0, columnspan=10)

bt_albedo = ttk.Button(root, image=util.images.get('albedo'), style="my.TButton").grid(row=1, column=0)
bt_amber = ttk.Button(root, image=util.images.get('amber'), style="my.TButton").grid(row=1, column=1)
bt_barbara = ttk.Button(root, image=util.images.get('barbara'), style="my.TButton").grid(row=1, column=2)
bt_beidou = ttk.Button(root, image=util.images.get('beidou'), style="my.TButton").grid(row=1, column=3)
bt_bennett = ttk.Button(root, image=util.images.get('bennett'), style="my.TButton").grid(row=1, column=4)
bt_chongyun = ttk.Button(root, image=util.images.get('chongyun'), style="my.TButton").grid(row=1, column=5)
bt_diluc = ttk.Button(root, image=util.images.get('diluc'), style="my.TButton").grid(row=1, column=6)
bt_diona = ttk.Button(root, image=util.images.get('diona'), style="my.TButton").grid(row=1, column=7)
bt_fischl = ttk.Button(root, image=util.images.get('fischl'), style="my.TButton").grid(row=1, column=8)
bt_jean = ttk.Button(root, image=util.images.get('jean'), style="my.TButton").grid(row=1, column=9)

bt_kaeya = ttk.Button(root, image=util.images.get('kaeya'), style="my.TButton").grid(row=2, column=0)
bt_qeqing = ttk.Button(root, image=util.images.get('keqing'), style="my.TButton").grid(row=2, column=1)
bt_klee = ttk.Button(root, image=util.images.get('klee'), style="my.TButton").grid(row=2, column=2)
bt_lisa = ttk.Button(root, image=util.images.get('lisa'), style="my.TButton").grid(row=2, column=3)
bt_mona = ttk.Button(root, image=util.images.get('mona'), style="my.TButton").grid(row=2, column=4)
bt_ningguang = ttk.Button(root, image=util.images.get('ningguang'), style="my.TButton").grid(row=2, column=5)
bt_noelle = ttk.Button(root, image=util.images.get('noelle'), style="my.TButton").grid(row=2, column=6)
bt_qiqi = ttk.Button(root, image=util.images.get('qiqi'), style="my.TButton").grid(row=2, column=7)
bt_razor = ttk.Button(root, image=util.images.get('razor'), style="my.TButton").grid(row=2, column=8)
bt_sucrose = ttk.Button(root, image=util.images.get('sucrose'), style="my.TButton").grid(row=2, column=9)

bt_tartaglia = ttk.Button(root, image=util.images.get('tartaglia'), style="my.TButton").grid(row=3, column=0)
bt_traveler_Anemo = ttk.Button(root, image=util.images.get('traveler_Anemo'), style="my.TButton").grid(row=3, column=1)
bt_traveler_Geo = ttk.Button(root, image=util.images.get('traveler_Geo'), style="my.TButton").grid(row=3, column=2)
bt_venti = ttk.Button(root, image=util.images.get('venti'), style="my.TButton").grid(row=3, column=3)
bt_xiangling = ttk.Button(root, image=util.images.get('xiangling'), style="my.TButton").grid(row=3, column=4)
bt_xiao = ttk.Button(root, image=util.images.get('xiao'), style="my.TButton").grid(row=3, column=5)
bt_xingqiu = ttk.Button(root, image=util.images.get('xingqiu'), style="my.TButton").grid(row=3, column=6)
bt_xinyan = ttk.Button(root, image=util.images.get('xinyan'), style="my.TButton").grid(row=3, column=7)
bt_zhongli = ttk.Button(root, image=util.images.get('zhongli'), style="my.TButton").grid(row=3, column=8)


root.mainloop()
