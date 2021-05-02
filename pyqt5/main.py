from PyQt5 import uic, QtWidgets, QtGui
import sqlite3
from util import check_element

def albedo():

    person = 'Albedo'

    tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Geo.png'))
    tela.lb_background.setPixmap(QtGui.QPixmap('img/background/64z64/bg_albedo.png'))

    print(check_element.check(person))

app = QtWidgets.QApplication([])

tela = uic.loadUi('ui/tela_inicial.ui')

tela.actionExit.triggered.connect(lambda: exit())
tela.actionAlbedo.triggered.connect(albedo)

tela.show()
app.exec_()
