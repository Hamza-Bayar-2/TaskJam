from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from myui import Ui_MainWindow

class MainWİndow(QMainWindow) :
    def __init__(self) :
        super(MainWİndow, self).__init__()
        self.ui = Ui_MainWindow()
        self.initUI()
    def initUI(self):
        self.ui.setupUi(self)
        self.setWindowTitle("TaskJam")
        self.show()
        # self.setWindowIcon(QIcon("planeLogo.ico"))
def mainLOOP():
    fas = QApplication(sys.argv)
    win = MainWİndow()
    sys.exit(fas.exec_())

mainLOOP()