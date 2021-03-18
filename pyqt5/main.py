from PyQt5 import uic, QtWidgets, QtGui

def foe():
    pass


app = QtWidgets.QApplication([])

tela = uic.loadUi('ui/tela.ui')

tela.lb_dps_build.setPixmap(QtGui.QPixmap('img/dps_build.png'))
tela.lb_support_build.setPixmap(QtGui.QPixmap('img/support_build.png'))

tela.actionExit.triggered.connect(lambda: exit())
tela.show()

app.exec_()
