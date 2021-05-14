from PyQt5 import uic, QtWidgets, QtGui
from util.images import element

chars = ['Albedo','Amber','Barbara','Beidou','Bennett','Chongyun','Diluc','Diona','Fischl','Ganyu','Hu Tao','Jean','Kaeya','Keqing','Klee','Lisa','Mona','Ningguang','Noelle','Qiqi','Razor','Sucrose','Tartaglia','Venti','Xiangling','Xiao','Xingqiu','Xinyan','Zhongli']

chars2 = ['Albedo','Amber','Barbara','Beidou_4','Bennett','Chongyun','Diluc','Diona','Fischl_3','Ganyu','Hu_Tao','Jean','Kaeya','Keqing_3','Klee','Lisa_2','Mona','Ningguang','Noelle','Qiqi','Razor_3','Sucrose','Tartaglia','Venti','Xiangling','Xiao','Xingqiu','Xinyan','Zhongli']


app = QtWidgets.QApplication([])

tela = uic.loadUi('ui/tela.ui')

tela.lb_dps_build.setPixmap(QtGui.QPixmap('img/dps_build.png'))

tela.actionExit.triggered.connect(lambda: exit())

for ii, i in enumerate(chars):
    exec(f"tela.action{chars2[ii]}.triggered.connect(lambda: element(tela,'{i}'))")

tela.show()
app.exec_()
