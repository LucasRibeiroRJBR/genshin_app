from PyQt5 import uic, QtWidgets, QtGui
from util.images import char_info
from util.commands import exiting

chars = ['Albedo','Amber','Barbara','Beidou','Bennett','Chongyun','Diluc','Diona','Eula','Fischl',
         'Ganyu','Hu Tao','Jean','Kaeya','Keqing','Klee','Lisa','Mona','Ningguang','Noelle',
         'Qiqi','Razor','Sucrose','Tartaglia', 'Traveler (Anemo)', 'Traveler (Geo)','Venti',
         'Xiangling','Xiao','Xingqiu','Xinyan','Yanfei','Zhongli']

chars2 = ['Albedo','Amber','Barbara','Beidou_4','Bennett','Chongyun','Diluc','Diona','Eula','Fischl_3',
          'Ganyu','Hu_Tao','Jean','Kaeya','Keqing_3','Klee','Lisa_2','Mona','Ningguang','Noelle',
          'Qiqi','Razor_3','Sucrose','Tartaglia', 'Traveler_Anemo', 'Traveler_Geo','Venti',
          'Xiangling','Xiao','Xingqiu','Xinyan','Yanfei','Zhongli']

# id,name,"element",id_hypos_mat,id_nature_mat,id_common_mat,id_weapon_dps,id_weapon_dps_or,id_weapon_sup,id_weapon_sup_or,id_artifact_dps_1,id_artifact_dps_2,id_artifact_dps_1_or,id_artifact_dps_2_or,id_artifact_sup_1,id_artifact_sup_2,id_artifact_sup_1_or,id_artifact_sup_2_or,id_talent_mat,id_bosss_mat
app = QtWidgets.QApplication([])
tela = uic.loadUi('ui/tela.ui')

tela.setWindowIcon(QtGui.QIcon('img/icon.ico'))

tela.lb_dps_build.setPixmap(QtGui.QPixmap('img/dps_build.png'))
tela.lb_sup_build.setPixmap(QtGui.QPixmap('img/sup_build.png'))
tela.lb_ascension.setPixmap(QtGui.QPixmap('img/ascension.png'))
tela.lb_skill_up.setPixmap(QtGui.QPixmap('img/skill_up.png'))
tela.actionExit.triggered.connect(lambda: exiting(tela))

for ii, i in enumerate(chars):
    exec(f"tela.action{chars2[ii]}.triggered.connect(lambda: char_info(tela,'{i}'))")

tela.show()
app.exec_()
