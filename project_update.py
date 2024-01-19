import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db_Helper
from UI.project_update_ui import Ui_TaskJamProjectInfo
from modals.projectInfo import ProjectInfo

class ProjectUpdate(QDialog):
    mainServer = pyqtSignal(str)

    def __init__(self, ProjectInfo) -> None:
        super(ProjectUpdate, self).__init__()
        self.ui = Ui_TaskJamProjectInfo()
        self.ui.setupUi(self)
        self.myProject = ProjectInfo
        self.db = db_Helper()
        self.window_fix()

        self.initUI()
    def initUI(self):
        self.buttonHandle()
        self.lineEditHandle()
    def buttonHandle(self):
        self.ui.exit_btn.clicked.connect(lambda : self.close())
        self.ui.project_add_btn.clicked.connect(lambda : self.updateProject())
        self.ui.project_dlete_btn.clicked.connect(lambda : self.deleteProject())

    def lineEditHandle(self) :
        self.ui.project_name_lineEdit.setText(self.myProject.projectName)
        self.ui.project_describe_lineEdit.setText(self.myProject.projectDescription)
        self.ui.starting_date_lineEdit.setText(self.myProject.startingDate)
        self.ui.ending_date_lineEdit.setText(self.myProject.endDate)

    def deleteProject(self):
        self.db.deleteProject(self.myProject.projectID)
        self.mainServer.emit("55 TAMM")
        self.close()

    def updateProject(self):
        projectName = self.ui.project_name_lineEdit.text()
        projectDescription = self.ui.project_describe_lineEdit.text()
        projectStartingDate = self.ui.starting_date_lineEdit.text()
        projectEndDate = self.ui.ending_date_lineEdit.text()

        startDate = datetime.datetime.strptime(projectStartingDate, '%d.%m.%Y')
        endDate = datetime.datetime.strptime(projectEndDate, '%d.%m.%Y')

        if(projectName == "" or projectDescription == "" or projectStartingDate == "" or endDate == ""):
            self.ui.status_label.setText("Boş bırakılamaz.")
            return
        elif(len(projectStartingDate.split(".")) != 3 or len(projectEndDate.split(".")) != 3 or len(projectStartingDate) != 10 or len(projectEndDate) != 10 ):
            self.ui.status_label.setText("lütfen tarih bilgilerinde formata uyunuz.")
            return
        elif startDate >= endDate :
            self.ui.status_label.setText("Başlangıç taihi bitiş tarihinden küçük olmamaz")
            pass
        else :
            self.db.updateProject(
                ProjectInfo(
                    projectID = self.myProject.projectID,
                    userID= None,
                    projectName= projectName,
                    projectDescription= projectDescription,
                    startingDate= projectStartingDate,
                    endDate= projectEndDate,
                    delayAmount= self.myProject.delayAmount
                ))
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