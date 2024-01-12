import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QScrollArea, QVBoxLayout, QSlider, QLabel, QHBoxLayout,QPushButton, QDialog
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from database import db_Helper
from UI.add_project_ui import Ui_project_add
from modals.projectInfo import ProjectInfo
from modals.userInfo import UserInfo

class AddProjectWindow(QDialog):
    mainServer = pyqtSignal(str)

    def __init__(self, UserInfo) -> None:
        super(AddProjectWindow, self).__init__()
        self.ui = Ui_project_add()
        self.ui.setupUi(self)
        self.db = db_Helper()
        self.user = UserInfo
        self.window_fix()
        self.initUI()
    def initUI(self):
        self.buttonHandle()
        self.ui.start_day_lineedit.setText("11.11.2024")
        self.ui.finish_day_lineedit.setText("20.11.2024")

    def buttonHandle(self):
        self.ui.exit_btn.clicked.connect(lambda : self.close())
        self.ui.project_add_btn.clicked.connect(lambda : self.addProject())
    
    def addProject(self):
        projectName = self.ui.project_name_lineedit.text()
        projectDescription = self.ui.project_describe_lineedit.text()
        startingDate = self.ui.start_day_lineedit.text()
        endDate = self.ui.finish_day_lineedit.text()


        if(projectName == "" or projectDescription == "" or startingDate == "" or endDate == ""):
            self.ui.status_label.setText("Boş bırakılamaz.")
            return
        elif(len(startingDate.split(".")) != 3 or len(endDate.split(".")) != 3 or len(startingDate) != 10 or len(endDate) != 10 ):
            self.ui.status_label.setText("lütfen tarih bilgilerinde formata uyunuz.")
            return
        elif(self.db.projectDetailPage(projectName=projectName) != None):
            self.ui.status_label.setText("Bu proje adına sahip zaten kayıt var")
            return
        elif 0:
            # startdate en date den önce olamaz kontrol et
            pass
        else :
            newProject = ProjectInfo(
                projectID = None,
                projectName = projectName,
                projectDescription = projectDescription,
                startingDate = startingDate,
                endDate = endDate,
                delayAmount = 0,)
            self.db.addProject(self.user, newProject)
            self.mainServer.emit("55 TAMM")
            self.close()


    def window_fix(self) :
        self.setWindowTitle("TaskJam Login")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint |Qt.FramelessWindowHint)
        #self.ui.app_bar_widget.mauseMoveEvent = self.mauseMoveEvent

    def mauseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

