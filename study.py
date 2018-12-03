import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon #”¶”√Õº±Í

def Sample_1():

    app  = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    Sample_1()