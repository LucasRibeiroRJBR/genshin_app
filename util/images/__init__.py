from tkinter import *

imagelist = {
    "albedo": ["img/Characters/Albedo.png", None],
    "amber": ["img/Characters/Amber.png", None],
    "barbara": ["img/Characters/Barbara.png", None],
    "beidou": ["img/Characters/Beidou.png", None],
    "bennett": ["img/Characters/Bennett.png", None],
    "chongyun": ["img/Characters/Chongyun.png", None],
    "diluc": ["img/Characters/Diluc.png", None],
    "diona": ["img/Characters/Diona.png", None],
    "fischl": ["img/Characters/Fischl.png", None],
    "jean": ["img/Characters/Jean.png", None],
    "kaeya": ["img/Characters/Kaeya.png", None],
    "keqing": ["img/Characters/Keqing.png", None],
    "klee": ["img/Characters/Klee.png", None],
    "lisa": ["img/Characters/Lisa.png", None],
    "mona": ["img/Characters/Mona.png", None],
    "ningguang": ["img/Characters/Ningguang.png", None],
    "noelle": ["img/Characters/Noelle.png", None],
    "qiqi": ["img/Characters/Qiqi.png", None],
    "razor": ["img/Characters/Razor.png", None],
    "sucrose": ["img/Characters/Sucrose.png", None],
    "tartaglia": ["img/Characters/Tartaglia.png", None],
    "traveler_Anemo": ["img/Characters/Traveler (Anemo).png", None],
    "traveler_Geo": ["img/Characters/Traveler (Geo).png", None],
    "venti": ["img/Characters/Venti.png", None],
    "xiangling": ["img/Characters/Xiangling.png", None],
    "xiao": ["img/Characters/Xiao.png", None],
    "xingqiu": ["img/Characters/Xingqiu.png", None],
    "xinyan": ["img/Characters/Xinyan.png", None],
    "zhongli": ["img/Characters/Zhongli.png", None],
    "anemo" : ["img/Elements/Anemo.png", None],
    "cryo" : ["img/Elements/Cryo.png", None],
    "dendro" : ["img/Elements/Dendro.png", None],
    "electro" : ["img/Elements/Electro.png", None],
    "geo" : ["img/Elements/Geo.png", None],
    "hydro" : ["img/Elements/Hydro.png", None],
    "pyro" : ["img/Elements/Pyro.png", None],
    "vazio" : ["img/vazio.png", None]
}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
      imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None

  