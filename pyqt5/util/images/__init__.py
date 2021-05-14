import sqlite3
from PyQt5 import QtGui

def element(tela,e):
    conn = sqlite3.connect('db/genshin.db')
    c = conn.cursor()
    dado = c.execute(f"SELECT * FROM chars WHERE name = '{e}';").fetchall()
    
    if dado[0][2] == 'Anemo':
        tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Anemo.png'))
    if dado[0][2] == 'Cryo':
        tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Cryo.png'))
    if dado[0][2] == 'Dendro':
        tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Dendro.png'))
    if dado[0][2] == 'Electro':
        tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Electro.png'))
    if dado[0][2] == 'Geo':
        tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Geo.png'))
    if dado[0][2] == 'Hydro':
        tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Hydro.png'))
    if dado[0][2] == 'Pyro':
        tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Pyro.png'))

    if dado[0][1] == 'Albedo':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_albedo.png'))
    if dado[0][1] == 'Amber':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_amber.png'))
    if dado[0][1] == 'Barbara':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_barbara.png'))
    if dado[0][1] == 'Beidou':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_beidou.png'))
    if dado[0][1] == 'Bennett':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_bennett.png'))
    if dado[0][1] == 'Chongyun':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_chongyun.png'))
    if dado[0][1] == 'Diluc':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_diluc.png'))
    if dado[0][1] == 'Diona':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_diona.png'))
    if dado[0][1] == 'Fischl':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_fischl.png'))
    if dado[0][1] == 'Ganyu':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_ganyu.png'))
    if dado[0][1] == 'Hu Tao':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_hu_tao.png'))
    if dado[0][1] == 'Jean':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_jean.png'))
    if dado[0][1] == 'Kaeya':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_kaeya.png'))
    if dado[0][1] == 'Keqing':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_keqing.png'))
    if dado[0][1] == 'Klee':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_klee.png'))
    if dado[0][1] == 'Lisa':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_lisa.png'))
    if dado[0][1] == 'Mona':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_mona.png'))
    if dado[0][1] == 'Ningguang':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_ninnguang.png'))
    if dado[0][1] == 'Noelle':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_noelle.png'))
    if dado[0][1] == 'Qiqi':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_qiqi.png'))
    if dado[0][1] == 'Razor':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_razor.png'))
    if dado[0][1] == 'Sucrose':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_sucrose.png'))
    if dado[0][1] == 'Tartaglia':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_tartaglia.png'))
    if dado[0][1] == 'Venti':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_venti.png'))
    if dado[0][1] == 'Xiangling':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_xiangliang.png'))
    if dado[0][1] == 'Xiao':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_xiao.png'))
    if dado[0][1] == 'Xingqiu':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_xingqiu.png'))
    if dado[0][1] == 'Xinyan':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_xinyan.png'))
    if dado[0][1] == 'Zhongli':
        tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_zhongli.png'))
    
