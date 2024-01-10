from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget
from UI.register_ui import Ui_Dialog

from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db_Helper
from modals.userInfo import UserInfo
from main import MainWİndow

class RegisterWindow(QDialog):
    def __init__(self) -> None:
        super(RegisterWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.db = db_Helper()
     
        self.ui.setupUi(self)
        self.window_fix()
        self.initUi()
    def initUi(self):
        self.buttonHandle()   

    def buttonHandle(self):
         self.ui.exit_btn.clicked.connect(lambda : self.close())
         self.ui.create_btn.clicked.connect(lambda : self.createUser())

    def createUser(self):
         self.readHandleInfo()
    
    def readHandleInfo(self):
        email = self.ui.eposta_lineedit.text()
        password = self.ui.password_lineedit.text()
        repassword = self.ui.repassword_lineedit.text()
        if((email.find("@") == -1 ) or (email.find(".") == -1) ) :
             self.ui.status_label.setText("Email'i doğru biçimde giriniz.")
        elif(password != repassword):
             self.ui.status_label.setText("Şifreler Uyuşmuyor")
        else :
               newUser = UserInfo(
                    kullaniciAdi= "kaan",
                    kullaniciSoyadi= "Akbıyık",
                    kullaniciMail= self.ui.eposta_lineedit.text(),
                    kullaniciSifre = self.ui.password_lineedit.text(),
               )
               self.db.kullaniciEkle(newUser)
               self.close()
               self.main = MainWİndow()
               self.main.showMaximized()
               
               self.db.kullaniciKisiselBilgilari(newUser.kullaniciMail)
               print(self.db.cursor.fetchall()[0])

    def window_fix(self) :
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint |Qt.FramelessWindowHint)
            self.ui.frame_2.mauseMoveEvent = self.mauseMoveEvent

    def mauseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()