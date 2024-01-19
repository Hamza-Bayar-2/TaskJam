import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QScrollArea, QVBoxLayout, QSlider, QLabel, QHBoxLayout,QPushButton, QDialog
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db_Helper
from UI.add_project_ui import Ui_project_add
from modals.projectInfo import ProjectInfo

class AddProjectWindow(QDialog):
    mainServer = pyqtSignal(str)

    def __init__(self, UserInfo ) -> None:
        super(AddProjectWindow, self).__init__()
        self.ui = Ui_project_add()
        self.ui.setupUi(self)
        self.db = db_Helper()
        self.user = UserInfo
        self.window_fix()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon(':/image/officalLogo.png'))
        self.setWindowTitle("TaskJam")
        self.buttonHandle()
        self.ui.starting_date_lineEdit.setText(str(datetime.datetime.strftime(datetime.datetime.now(),"%d.%m.%Y")))
        self.ui.ending_date_lineEdit.setText(str(datetime.datetime.strftime(datetime.datetime.now() ,"%d.%m.%Y")))

    def buttonHandle(self):
        self.ui.exit_btn.clicked.connect(lambda : self.close())
        self.ui.project_add_btn.clicked.connect(lambda : self.addProject())
    
    def addProject(self):
        projectName = self.ui.project_name_lineEdit.text()
        projectDescription = self.ui.project_describe_lineEdit.text()
        startingDate = self.ui.starting_date_lineEdit.text()
        endDate = self.ui.ending_date_lineEdit.text()
        

        if(projectName == "" or projectDescription == "" or startingDate == "" or endDate == ""):
            self.ui.status_label.setText("Boş bırakılamaz.")
            return
        elif(self.validateDate(startingDate, endDate)):
            self.ui.status_label.setText("lütfen tarih bilgilerinde formata uyunuz.")
            return
        elif(self.db.showProjectOnDetailPage(projectName=projectName) != None):
            self.ui.status_label.setText("Bu proje adına sahip zaten kayıt var")
            return
        elif self.dateNow > self.dateLater :
            self.ui.status_label.setText("Başlangıç taihi bitiş tarihinden küçük olamaz")
        else :
            newProject = ProjectInfo(
                projectID = None,
                userID= self.user.userID,
                projectName = projectName,
                projectDescription = projectDescription,
                startingDate = startingDate,
                endDate = endDate,
                delayAmount = 0,)
            self.db.addNewProject(self.user.userID,newProject)
            self.mainServer.emit("55 TAMM")
            self.close()
    def validateDate(self, taskStartDate, taskEndDate):
        try:
            self.dateNow = datetime.datetime.strptime(taskStartDate, "%d.%m.%Y")
            self.dateLater = datetime.datetime.strptime(taskEndDate, "%d.%m.%Y")
            return False
        except ValueError:
            return True

    def window_fix(self) :
        self.setWindowTitle("TaskJam Login")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint |Qt.FramelessWindowHint)
        #self.ui.app_bar_widget.mauseMoveEvent = self.mauseMoveEvent

    def mauseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

