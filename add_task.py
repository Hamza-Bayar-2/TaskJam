import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QScrollArea, QVBoxLayout, QSlider, QLabel, QHBoxLayout,QPushButton, QDialog
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from database import db_Helper
from UI.add_task_ui import Ui_AddTask
from modals.projectInfo import ProjectInfo
from modals.userInfo import UserInfo
from modals.taskInfo import TaskInfo
from list_employee_window import ListEmployeeWindow
from database import db_Helper
from modals.employeeInfo import EmployeeInfo

class AddTask(QDialog):
    mainWindowSocket = pyqtSignal(str)

    def __init__(self, projectName) -> None:
        super(AddTask, self).__init__()
        self.ui = Ui_AddTask()
        self.ui.setupUi(self)
        self.db = db_Helper()
        self.window_fix()
        self.projectName = projectName
        self.myEmployee = None
        self.initUi() 

    def initUi(self):
        self.ui.will_add_project_label.setText(self.projectName)
        self.ui.exit_btn.clicked.connect(lambda : self.close())
        self.ui.task_add_btn.clicked.connect(lambda : self.taskAdd())
        self.ui.workers_list_btn.clicked.connect(lambda: self.openEmployeeList())
    
    def taskAdd(self) :
        #validet yap myEmployee geldi mi ?
        taskName = self.ui.task_name_lineEdit.text()
        taskDescription = self.ui.lineEdit_2.text()
        taskStartingDate = self.ui.starting_date_lineEdit.text()
        taskEndDate = self.ui.ending_datelineEdit.text()
        projectInfo = self.db.showProjectOnDetailPage(projectName=self.projectName)
        employeeID= self.myEmployee.employeeID

        newTask = TaskInfo(
            taskID= None,
            projectID= projectInfo.projectID,
            employeeID= employeeID,
            taskName= taskName,
            taskDescription= taskDescription,
            startingDate= taskStartingDate,
            endDate= taskEndDate,
            taskStatus= 0,
            delayAmount= 0
        )
        
        self.db.addNewTask(newTask)
        self.mainWindowSocket.emit("55 TAMM")
        self.close()


    def openEmployeeList(self):
        self.employeeList = ListEmployeeWindow()
        self.employeeList.connectMain.connect(lambda selectedEmployee : self.setEmployee(selectedEmployee) if(selectedEmployee != None) else print("zart") )

    def setEmployee(self, selectedEmp):
        self.myEmployee = selectedEmp
        self.ui.selected_worker_label.setText(selectedEmp.employeeName + " " + selectedEmp.employeeSurname)

    def window_fix(self) :
        self.setWindowTitle("TaskJam Login")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint |Qt.FramelessWindowHint)
        #self.ui.app_bar_widget.mauseMoveEvent = self.mauseMoveEvent

    def mauseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

