import main
from PyQt5 import QtGui


def checar():
    main.tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_albedo.png'))
    main.tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Geo.png'))
