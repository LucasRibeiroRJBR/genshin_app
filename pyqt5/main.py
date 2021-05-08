from PyQt5 import uic, QtWidgets, QtGui
import sqlite3
from util import set_element

def albedo():

    person = 'Albedo'

    tela.lb_background.setPixmap(QtGui.QPixmap('img/background/64z64/bg_albedo.png'))

    print(set_element.check(person))


app = QtWidgets.QApplication([])

tela = uic.loadUi('ui/tela_inicial.ui')

tela.lb_dps_build.setPixmap(QtGui.QPixmap('img/dps_build.png'))

tela.actionExit.triggered.connect(lambda: exit())
tela.actionAlbedo.triggered.connect(albedo)

tela.show()
app.exec_()
