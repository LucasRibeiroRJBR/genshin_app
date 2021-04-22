from PyQt5 import uic, QtWidgets, QtGui

def albedo():
    tela.lb_weapon_1.setPixmap(QtGui.QPixmap('img/weapons/Skyward_Blade.png'))
    tela.lb_weapon_2.setPixmap(QtGui.QPixmap('img/weapons/Festering_Desire.png'))
    tela.lb_artifact_1.setPixmap(QtGui.QPixmap('img/artifact/archaic_petra.png'))
    tela.lb_artifact_2.setPixmap(QtGui.QPixmap('img/artifact/noblesse_oblige.png'))
    tela.lb_weapon_name_1.setText('Skyward Blade')
    tela.lb_weapon_name_2.setText('Festering Desire')
    tela.lb_artifact_name_1.setText('Archaic Petra')
    tela.lb_artifact_name_2.setText('Noblesse Oblige')


app = QtWidgets.QApplication([])

tela = uic.loadUi('ui/tela.ui')

tela.lb_dps_build.setPixmap(QtGui.QPixmap('img/dps_build.png'))
tela.lb_support_build.setPixmap(QtGui.QPixmap('img/support_build.png'))

tela.actionExit.triggered.connect(lambda: exit())
tela.actionAlbedo.triggered.connect(albedo)

tela.lb_background.setPixmap(QtGui.QPixmap('img/background/bg_albedo.png'))

tela.show()
app.exec_()
