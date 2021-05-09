import sqlite3
from PyQt5 import uic, QtWidgets, QtGui
from util.images.characters import checar

app = QtWidgets.QApplication([])

tela = uic.loadUi('ui/tela.ui')

tela.lb_dps_build.setPixmap(QtGui.QPixmap('img/dps_build.png'))

tela.actionExit.triggered.connect(lambda: exit())
tela.actionAlbedo.triggered.connect(checar)

tela.show()
app.exec_()
