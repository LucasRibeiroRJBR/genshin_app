# Form implementation generated from reading ui file 'c:\Users\user\Documents\GitHub\genshin_app\pyqt5\ui\tela.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 713)
        MainWindow.setStyleSheet("/* QWidget#centralwidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(164, 241, 202, 255), stop:0.142 rgba(205, 255, 255, 255), stop:0.285 rgba(176, 234, 42, 255), stop:0.428 rgba(222, 186, 255, 255), stop:0.571 rgba(244, 214, 96, 255), stop:0.714 rgba(8, 228, 255, 255), stop:0.857 rgba(255, 169, 112, 255));\n"
"} */\n"
"\n"
"QWidget#centralwidget {\n"
"    background-color: #302554;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: white;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: #717171;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenuBar::item::selected {\n"
"    background-color: #FF0000;\n"
"    font: bold 12pt \"Arial\";\n"
"}\n"
"QMenu {\n"
"    background-color: #717171;\n"
"    color: #FFFFFF;\n"
"    font: bold 12pt \"Arial\";\n"
"    }\n"
"QMenu::item::selected {\n"
"    background-color: #2E2E2E;\n"
"    color: #FFFF00;\n"
"    border: 3px solid;    \n"
"    border-left-color:#FFFF00;        \n"
"    border-top-color: #00000000;\n"
"    border-bottom-color: #00000000;\n"
"    border-right-color: #00000000;\n"
"    font: bold 12pt \"Arial\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_background = QtWidgets.QLabel(self.centralwidget)
        self.lb_background.setGeometry(QtCore.QRect(0, 0, 391, 221))
        self.lb_background.setAutoFillBackground(False)
        self.lb_background.setText("")
        self.lb_background.setScaledContents(False)
        self.lb_background.setObjectName("lb_background")
        self.lb_element = QtWidgets.QLabel(self.centralwidget)
        self.lb_element.setGeometry(QtCore.QRect(10, 10, 64, 64))
        self.lb_element.setText("")
        self.lb_element.setObjectName("lb_element")
        self.lb_weapon_dps = QtWidgets.QLabel(self.centralwidget)
        self.lb_weapon_dps.setGeometry(QtCore.QRect(10, 270, 64, 64))
        self.lb_weapon_dps.setAutoFillBackground(True)
        self.lb_weapon_dps.setObjectName("lb_weapon_dps")
        self.lb_dps_build = QtWidgets.QLabel(self.centralwidget)
        self.lb_dps_build.setGeometry(QtCore.QRect(60, 230, 281, 30))
        self.lb_dps_build.setAutoFillBackground(False)
        self.lb_dps_build.setText("")
        self.lb_dps_build.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lb_dps_build.setObjectName("lb_dps_build")
        self.lb_artifact_dps_1 = QtWidgets.QLabel(self.centralwidget)
        self.lb_artifact_dps_1.setGeometry(QtCore.QRect(170, 270, 64, 64))
        self.lb_artifact_dps_1.setAutoFillBackground(True)
        self.lb_artifact_dps_1.setObjectName("lb_artifact_dps_1")
        self.lb_artifact_dps_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_artifact_dps_2.setGeometry(QtCore.QRect(280, 270, 64, 64))
        self.lb_artifact_dps_2.setAutoFillBackground(True)
        self.lb_artifact_dps_2.setObjectName("lb_artifact_dps_2")
        self.lb_weapon_dps_or = QtWidgets.QLabel(self.centralwidget)
        self.lb_weapon_dps_or.setGeometry(QtCore.QRect(10, 360, 64, 64))
        self.lb_weapon_dps_or.setAutoFillBackground(True)
        self.lb_weapon_dps_or.setObjectName("lb_weapon_dps_or")
        self.lb_artifact_dps_1_or = QtWidgets.QLabel(self.centralwidget)
        self.lb_artifact_dps_1_or.setGeometry(QtCore.QRect(170, 360, 64, 64))
        self.lb_artifact_dps_1_or.setAutoFillBackground(True)
        self.lb_artifact_dps_1_or.setObjectName("lb_artifact_dps_1_or")
        self.lb_artifact_dps_2_or = QtWidgets.QLabel(self.centralwidget)
        self.lb_artifact_dps_2_or.setGeometry(QtCore.QRect(280, 360, 64, 64))
        self.lb_artifact_dps_2_or.setAutoFillBackground(True)
        self.lb_artifact_dps_2_or.setObjectName("lb_artifact_dps_2_or")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 450, 304, 50))
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.lb_artifact_dps_3 = QtWidgets.QLabel(self.centralwidget)
        self.lb_artifact_dps_3.setGeometry(QtCore.QRect(280, 510, 64, 64))
        self.lb_artifact_dps_3.setAutoFillBackground(True)
        self.lb_artifact_dps_3.setObjectName("lb_artifact_dps_3")
        self.lb_artifact_dps_2_or_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_artifact_dps_2_or_2.setGeometry(QtCore.QRect(280, 600, 64, 64))
        self.lb_artifact_dps_2_or_2.setAutoFillBackground(True)
        self.lb_artifact_dps_2_or_2.setObjectName("lb_artifact_dps_2_or_2")
        self.lb_artifact_dps_1_or_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_artifact_dps_1_or_2.setGeometry(QtCore.QRect(170, 600, 64, 64))
        self.lb_artifact_dps_1_or_2.setAutoFillBackground(True)
        self.lb_artifact_dps_1_or_2.setObjectName("lb_artifact_dps_1_or_2")
        self.lb_weapon_dps_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_weapon_dps_2.setGeometry(QtCore.QRect(10, 510, 64, 64))
        self.lb_weapon_dps_2.setAutoFillBackground(True)
        self.lb_weapon_dps_2.setObjectName("lb_weapon_dps_2")
        self.lb_artifact_dps_4 = QtWidgets.QLabel(self.centralwidget)
        self.lb_artifact_dps_4.setGeometry(QtCore.QRect(170, 510, 64, 64))
        self.lb_artifact_dps_4.setAutoFillBackground(True)
        self.lb_artifact_dps_4.setObjectName("lb_artifact_dps_4")
        self.lb_weapon_dps_or_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_weapon_dps_or_2.setGeometry(QtCore.QRect(10, 600, 64, 64))
        self.lb_weapon_dps_or_2.setAutoFillBackground(True)
        self.lb_weapon_dps_or_2.setObjectName("lb_weapon_dps_or_2")
        self.lb_background.raise_()
        self.lb_weapon_dps.raise_()
        self.lb_dps_build.raise_()
        self.lb_artifact_dps_1.raise_()
        self.lb_artifact_dps_2.raise_()
        self.lb_weapon_dps_or.raise_()
        self.lb_artifact_dps_1_or.raise_()
        self.lb_artifact_dps_2_or.raise_()
        self.label.raise_()
        self.lb_artifact_dps_3.raise_()
        self.lb_artifact_dps_2_or_2.raise_()
        self.lb_artifact_dps_1_or_2.raise_()
        self.lb_weapon_dps_2.raise_()
        self.lb_artifact_dps_4.raise_()
        self.lb_weapon_dps_or_2.raise_()
        self.lb_element.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 21))
        self.menubar.setObjectName("menubar")
        self.menuAnemo = QtWidgets.QMenu(self.menubar)
        self.menuAnemo.setObjectName("menuAnemo")
        self.menuDendro = QtWidgets.QMenu(self.menubar)
        self.menuDendro.setObjectName("menuDendro")
        self.menuGeo = QtWidgets.QMenu(self.menubar)
        self.menuGeo.setObjectName("menuGeo")
        self.menuHydro = QtWidgets.QMenu(self.menubar)
        self.menuHydro.setObjectName("menuHydro")
        self.menuPyro = QtWidgets.QMenu(self.menubar)
        self.menuPyro.setObjectName("menuPyro")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuCryo = QtWidgets.QMenu(self.menubar)
        self.menuCryo.setObjectName("menuCryo")
        self.menuElectro = QtWidgets.QMenu(self.menubar)
        self.menuElectro.setObjectName("menuElectro")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionJean = QtGui.QAction(MainWindow)
        self.actionJean.setObjectName("actionJean")
        self.actionSucrose = QtGui.QAction(MainWindow)
        self.actionSucrose.setObjectName("actionSucrose")
        self.actionTraveler_Anemo = QtGui.QAction(MainWindow)
        self.actionTraveler_Anemo.setObjectName("actionTraveler_Anemo")
        self.actionVenti = QtGui.QAction(MainWindow)
        self.actionVenti.setObjectName("actionVenti")
        self.actionXiao = QtGui.QAction(MainWindow)
        self.actionXiao.setObjectName("actionXiao")
        self.actionBeidou = QtGui.QAction(MainWindow)
        self.actionBeidou.setObjectName("actionBeidou")
        self.actionFischl = QtGui.QAction(MainWindow)
        self.actionFischl.setObjectName("actionFischl")
        self.actionKeqing = QtGui.QAction(MainWindow)
        self.actionKeqing.setObjectName("actionKeqing")
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionRazor = QtGui.QAction(MainWindow)
        self.actionRazor.setObjectName("actionRazor")
        self.actionBeidou_2 = QtGui.QAction(MainWindow)
        self.actionBeidou_2.setObjectName("actionBeidou_2")
        self.actionFischl_2 = QtGui.QAction(MainWindow)
        self.actionFischl_2.setObjectName("actionFischl_2")
        self.actionKeqing_2 = QtGui.QAction(MainWindow)
        self.actionKeqing_2.setObjectName("actionKeqing_2")
        self.actionLisa = QtGui.QAction(MainWindow)
        self.actionLisa.setObjectName("actionLisa")
        self.actionRazor_2 = QtGui.QAction(MainWindow)
        self.actionRazor_2.setObjectName("actionRazor_2")
        self.actionAlbedo = QtGui.QAction(MainWindow)
        self.actionAlbedo.setObjectName("actionAlbedo")
        self.actionNingguang = QtGui.QAction(MainWindow)
        self.actionNingguang.setObjectName("actionNingguang")
        self.actionNoelle = QtGui.QAction(MainWindow)
        self.actionNoelle.setObjectName("actionNoelle")
        self.actionTraveler_Geo = QtGui.QAction(MainWindow)
        self.actionTraveler_Geo.setObjectName("actionTraveler_Geo")
        self.actionZhongli = QtGui.QAction(MainWindow)
        self.actionZhongli.setObjectName("actionZhongli")
        self.actionBarbara = QtGui.QAction(MainWindow)
        self.actionBarbara.setObjectName("actionBarbara")
        self.actionMona = QtGui.QAction(MainWindow)
        self.actionMona.setObjectName("actionMona")
        self.actionTartaglia = QtGui.QAction(MainWindow)
        self.actionTartaglia.setObjectName("actionTartaglia")
        self.actionXingqiu = QtGui.QAction(MainWindow)
        self.actionXingqiu.setObjectName("actionXingqiu")
        self.actionAmber = QtGui.QAction(MainWindow)
        self.actionAmber.setObjectName("actionAmber")
        self.actionBennett = QtGui.QAction(MainWindow)
        self.actionBennett.setObjectName("actionBennett")
        self.actionDiluc = QtGui.QAction(MainWindow)
        self.actionDiluc.setObjectName("actionDiluc")
        self.actionHu_Tao = QtGui.QAction(MainWindow)
        self.actionHu_Tao.setObjectName("actionHu_Tao")
        self.actionKlee = QtGui.QAction(MainWindow)
        self.actionKlee.setObjectName("actionKlee")
        self.actionXiangling = QtGui.QAction(MainWindow)
        self.actionXiangling.setObjectName("actionXiangling")
        self.actionXinyan = QtGui.QAction(MainWindow)
        self.actionXinyan.setObjectName("actionXinyan")
        self.actionChongyun = QtGui.QAction(MainWindow)
        self.actionChongyun.setObjectName("actionChongyun")
        self.actionDiona = QtGui.QAction(MainWindow)
        self.actionDiona.setObjectName("actionDiona")
        self.actionGanyu = QtGui.QAction(MainWindow)
        self.actionGanyu.setObjectName("actionGanyu")
        self.actionKaeya = QtGui.QAction(MainWindow)
        self.actionKaeya.setObjectName("actionKaeya")
        self.actionQiqi = QtGui.QAction(MainWindow)
        self.actionQiqi.setObjectName("actionQiqi")
        self.actionBeidou_3 = QtGui.QAction(MainWindow)
        self.actionBeidou_3.setObjectName("actionBeidou_3")
        self.actionBeidou_4 = QtGui.QAction(MainWindow)
        self.actionBeidou_4.setObjectName("actionBeidou_4")
        self.actionFischl_3 = QtGui.QAction(MainWindow)
        self.actionFischl_3.setObjectName("actionFischl_3")
        self.actionKeqing_3 = QtGui.QAction(MainWindow)
        self.actionKeqing_3.setObjectName("actionKeqing_3")
        self.actionLisa_2 = QtGui.QAction(MainWindow)
        self.actionLisa_2.setObjectName("actionLisa_2")
        self.actionRazor_3 = QtGui.QAction(MainWindow)
        self.actionRazor_3.setObjectName("actionRazor_3")
        self.menuAnemo.addAction(self.actionJean)
        self.menuAnemo.addAction(self.actionSucrose)
        self.menuAnemo.addAction(self.actionTraveler_Anemo)
        self.menuAnemo.addAction(self.actionVenti)
        self.menuAnemo.addAction(self.actionXiao)
        self.menuGeo.addAction(self.actionAlbedo)
        self.menuGeo.addAction(self.actionNingguang)
        self.menuGeo.addAction(self.actionNoelle)
        self.menuGeo.addAction(self.actionTraveler_Geo)
        self.menuGeo.addAction(self.actionZhongli)
        self.menuHydro.addAction(self.actionBarbara)
        self.menuHydro.addAction(self.actionMona)
        self.menuHydro.addAction(self.actionTartaglia)
        self.menuHydro.addAction(self.actionXingqiu)
        self.menuPyro.addAction(self.actionAmber)
        self.menuPyro.addAction(self.actionBennett)
        self.menuPyro.addAction(self.actionDiluc)
        self.menuPyro.addAction(self.actionHu_Tao)
        self.menuPyro.addAction(self.actionKlee)
        self.menuPyro.addAction(self.actionXiangling)
        self.menuPyro.addAction(self.actionXinyan)
        self.menuMenu.addAction(self.actionExit)
        self.menuCryo.addAction(self.actionChongyun)
        self.menuCryo.addAction(self.actionDiona)
        self.menuCryo.addAction(self.actionGanyu)
        self.menuCryo.addAction(self.actionKaeya)
        self.menuCryo.addAction(self.actionQiqi)
        self.menuElectro.addAction(self.actionBeidou_4)
        self.menuElectro.addAction(self.actionFischl_3)
        self.menuElectro.addAction(self.actionKeqing_3)
        self.menuElectro.addAction(self.actionLisa_2)
        self.menuElectro.addAction(self.actionRazor_3)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAnemo.menuAction())
        self.menubar.addAction(self.menuCryo.menuAction())
        self.menubar.addAction(self.menuDendro.menuAction())
        self.menubar.addAction(self.menuElectro.menuAction())
        self.menubar.addAction(self.menuGeo.menuAction())
        self.menubar.addAction(self.menuHydro.menuAction())
        self.menubar.addAction(self.menuPyro.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_weapon_dps.setText(_translate("MainWindow", "arma dps 1"))
        self.lb_artifact_dps_1.setText(_translate("MainWindow", "artifact"))
        self.lb_artifact_dps_2.setText(_translate("MainWindow", "artifact"))
        self.lb_weapon_dps_or.setText(_translate("MainWindow", "arma dps 1"))
        self.lb_artifact_dps_1_or.setText(_translate("MainWindow", "artifact"))
        self.lb_artifact_dps_2_or.setText(_translate("MainWindow", "artifact"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.lb_artifact_dps_3.setText(_translate("MainWindow", "artifact"))
        self.lb_artifact_dps_2_or_2.setText(_translate("MainWindow", "artifact"))
        self.lb_artifact_dps_1_or_2.setText(_translate("MainWindow", "artifact"))
        self.lb_weapon_dps_2.setText(_translate("MainWindow", "arma dps 1"))
        self.lb_artifact_dps_4.setText(_translate("MainWindow", "artifact"))
        self.lb_weapon_dps_or_2.setText(_translate("MainWindow", "arma dps 1"))
        self.menuAnemo.setTitle(_translate("MainWindow", "Anemo"))
        self.menuDendro.setTitle(_translate("MainWindow", "Dendro"))
        self.menuGeo.setTitle(_translate("MainWindow", "Geo"))
        self.menuHydro.setTitle(_translate("MainWindow", "Hydro"))
        self.menuPyro.setTitle(_translate("MainWindow", "Pyro"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuCryo.setTitle(_translate("MainWindow", "Cryo"))
        self.menuElectro.setTitle(_translate("MainWindow", "Electro"))
        self.actionExit.setText(_translate("MainWindow", " Exit"))
        self.actionJean.setText(_translate("MainWindow", " Jean"))
        self.actionSucrose.setText(_translate("MainWindow", " Sucrose"))
        self.actionTraveler_Anemo.setText(_translate("MainWindow", " Traveler (Anemo)"))
        self.actionVenti.setText(_translate("MainWindow", " Venti"))
        self.actionXiao.setText(_translate("MainWindow", " Xiao"))
        self.actionBeidou.setText(_translate("MainWindow", "Beidou"))
        self.actionFischl.setText(_translate("MainWindow", "Fischl"))
        self.actionKeqing.setText(_translate("MainWindow", "Keqing"))
        self.action.setText(_translate("MainWindow", "Lisa"))
        self.actionRazor.setText(_translate("MainWindow", "Razor"))
        self.actionBeidou_2.setText(_translate("MainWindow", " Beidou"))
        self.actionFischl_2.setText(_translate("MainWindow", " Fischl"))
        self.actionKeqing_2.setText(_translate("MainWindow", " Keqing"))
        self.actionLisa.setText(_translate("MainWindow", " Lisa"))
        self.actionRazor_2.setText(_translate("MainWindow", " Razor"))
        self.actionAlbedo.setText(_translate("MainWindow", " Albedo"))
        self.actionNingguang.setText(_translate("MainWindow", " Ningguang"))
        self.actionNoelle.setText(_translate("MainWindow", " Noelle"))
        self.actionTraveler_Geo.setText(_translate("MainWindow", " Traveler (Geo)"))
        self.actionZhongli.setText(_translate("MainWindow", " Zhongli"))
        self.actionBarbara.setText(_translate("MainWindow", " Barbara"))
        self.actionMona.setText(_translate("MainWindow", " Mona"))
        self.actionTartaglia.setText(_translate("MainWindow", " Tartaglia"))
        self.actionXingqiu.setText(_translate("MainWindow", " Xingqiu"))
        self.actionAmber.setText(_translate("MainWindow", " Amber"))
        self.actionBennett.setText(_translate("MainWindow", " Bennett"))
        self.actionDiluc.setText(_translate("MainWindow", " Diluc"))
        self.actionHu_Tao.setText(_translate("MainWindow", " Hu Tao"))
        self.actionKlee.setText(_translate("MainWindow", " Klee"))
        self.actionXiangling.setText(_translate("MainWindow", " Xiangling"))
        self.actionXinyan.setText(_translate("MainWindow", " Xinyan"))
        self.actionChongyun.setText(_translate("MainWindow", " Chongyun"))
        self.actionDiona.setText(_translate("MainWindow", " Diona"))
        self.actionGanyu.setText(_translate("MainWindow", " Ganyu"))
        self.actionKaeya.setText(_translate("MainWindow", " Kaeya"))
        self.actionQiqi.setText(_translate("MainWindow", " Qiqi"))
        self.actionBeidou_3.setText(_translate("MainWindow", "Beidou"))
        self.actionBeidou_4.setText(_translate("MainWindow", "Beidou"))
        self.actionFischl_3.setText(_translate("MainWindow", "Fischl"))
        self.actionKeqing_3.setText(_translate("MainWindow", "Keqing"))
        self.actionLisa_2.setText(_translate("MainWindow", "Lisa"))
        self.actionRazor_3.setText(_translate("MainWindow", "Razor"))
