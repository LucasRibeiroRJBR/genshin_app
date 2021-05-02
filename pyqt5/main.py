from PyQt5 import uic, QtWidgets, QtGui
import sqlite3

def albedo():

    conn = sqlite3.connect('db/genshin.db')
    c = conn.cursor()

    tela.lb_element.setPixmap(QtGui.QPixmap('img/elements/Element_Geo.png'))
    tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_albedo.png'))


app = QtWidgets.QApplication([])

tela = uic.loadUi('ui/tela_inicial.ui')

tela.actionExit.triggered.connect(lambda: exit())
tela.actionAlbedo.triggered.connect(albedo)

tela.show()
app.exec_()
