from main import *
from PyQt5 import uic, QtGui, QtWidgets
import sqlite3


def check(p):
    conn = sqlite3.connect('db/genshin.db')
    c = conn.cursor()

    data = c.execute(f"SELECT name,element,id_weapon_dps,id_weapon_dps_or,id_weapon_sup,id_weapon_sup_or,id_artifact_dps_1,id_artifact_dps_1_or,id_artifact_dps_2,id_artifact_dps_2_or,id_artifact_sup_1,id_artifact_sup_1_or,id_artifact_sup_2,id_artifact_sup_2_or,id_hypos_mat,id_nature_mat,id_common_mat,id_talent_mat,id_bosss_mat FROM chars WHERE name = '{p}';").fetchall()

    print(data[0][1])

    if data[0][1] == 'Geo':
        return tela.lb_element.setPixmap(QtGui.QPixmap('../../img/elements/Element_Geo.png'))




