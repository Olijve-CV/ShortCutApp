#-*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from utility import CConfigOper

class CApplication(CConfigOper,QWidget):

    def __init__(self, oConf):
        QWidget.__init__(self)
        CConfigOper.__init__(self,oConf)
        self.initUI()

    def initUI(self):

        self.SetTipFont()

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.setStyleSheet("color:red")
        btn.setStyleSheet("background-color:white")

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

    def SetTipFont(self):
        QToolTip.setFont(QFont('SansSerif', 8))

def Run():

    app = QApplication(sys.argv)
    ex = CApplication({})
    sys.exit(app.exec_())

if __name__ == '__main__':
    Run()