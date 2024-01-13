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
from list_employee_window import ListEmployeeWindow

class AddTask(QDialog):
    def __init__(self) -> None:
        super(AddTask, self).__init__()
        self.ui = Ui_AddTask()
        self.ui.setupUi(self)
        self.window_fix()
        self.myEmployee = None
        self.initUi() 

    def initUi(self):
        self.ui.exit_btn.clicked.connect(lambda : self.close())
        self.ui.task_add_btn.clicked.connect(lambda : self.taskAdd())
        self.ui.workers_list_btn.clicked.connect(lambda: self.openEmployeeList())
    
    def taskAdd(self) :
        #validet yap myEmployee geldi mi ?
        pass
    
    def openEmployeeList(self):
        self.employeeList = ListEmployeeWindow()
        self.employeeList.connectMain.connect(lambda selectedEmployee : self.setEmployee(selectedEmployee) if(selectedEmployee != None) else print("zart") )
        self.employeeList.show()

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

