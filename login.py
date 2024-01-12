from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QScrollArea, QVBoxLayout, QSlider, QLabel, QHBoxLayout,QPushButton, QDialog
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from UI.login_ui import Ui_Dialog
from database import db_Helper
from register import RegisterWindow
from main import MainWİndow

class LoginWindow(QDialog) :
    def __init__(self) -> None:
        super(LoginWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.db = db_Helper()
        self.window_fix()
        self.ui.setupUi(self)
        self.initUi()
    def initUi(self):
        self.showNormal()
        self.buttonHandle()

        self.ui.eposta_lineedit.setText(".@")
        self.ui.password_lineedit.setText(".")

    def buttonHandle(self):
         self.ui.exit_btn.clicked.connect(lambda : self.close())
         self.ui.register_btn.clicked.connect(lambda : self.openRegister())
         self.ui.signin_btn.clicked.connect(lambda : self.openMain())

    def openMain(self):
        email = self.ui.eposta_lineedit.text()
        password = self.ui.password_lineedit.text()
        User = self.db.userInformation(email)
    
        if(email == "" or password == ""):
            self.ui.status_label.setText("Lütfen bilgileri eksiksiz giriniz.")
            return
        elif(User == None):
            self.ui.status_label.setText("Böyle bir Kullanıcı yok")
            return
        elif(User.userPassword == password):
            self.close()
            self.mainChannel = MainWİndow(User)
            self.mainChannel.showMaximized()
            return
        else:
            self.ui.status_label.setText("Email ya da Password Yanlış")  

    def openRegister(self):
        self.close()
        self.register = RegisterWindow()
        self.register.showNormal()

    def window_fix(self) :
        self.setWindowTitle("TaskJam Login")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint |Qt.FramelessWindowHint)
        #self.ui.app_bar_widget.mauseMoveEvent = self.mauseMoveEvent

    def mauseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
          
def mainLOOP():
    fas = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(fas.exec_())

mainLOOP()