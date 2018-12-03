#-*-coding:utf-8
from PyQt5.QtWIdgets import QPushButton,QWidget,QApplication
from PyQt5.QtCore import QCoreApplication
from .utility import CConfigOper

class CButton(CConfigOper):

    WIDTH, HEIGHT = 20, 10

    def __init__(self, fathername, conf):
        CConfigOper.__init__(conf)
        self.GenerateButton()

    def GenerateButton(self):
        self.oButton = QPushButton(self.Name, self.father)
        self.SetToolTip()
        self.SetBgColor()
        self.SetTextColor()

    def Button(self):
        return self.oButton

    def SetToolTip(self):
        self.oButton.setToolTip(self.Tip)

    def SetBgColor(self):
        self.oButton.setStyleSheet('background-color:%s'%self.BgColor)

    def SetTextColor(self):
        self.oButton.setStyleSheet('background-color:self.BgColor'%self.TextColor)
