from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QScrollArea, QVBoxLayout, QSlider, QLabel, QHBoxLayout,QPushButton, QDialog
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from UI.list_employee_window_ui import Ui_ListEmployee_Window
from UI.employee_list_widget_small_ui import Ui_smal_row_Widget
from database import db_Helper
from modals.employeeInfo import EmployeeInfo

class ListEmployeeWindow(QDialog):
    connectMain = pyqtSignal(EmployeeInfo)

    def __init__(self) -> None:
        super(ListEmployeeWindow, self).__init__()
        self.ui = Ui_ListEmployee_Window()
        self.ui.setupUi(self) 
        self.db = db_Helper()
        self.window_fix()
        self.initUI()

    def initUI(self):
        self.buttonHandle()
        self.uploadEmployees()
        self.show()

    def buttonHandle(self):
        self.ui.exit_btn.clicked.connect(lambda :self.close())
        pass

    def uploadEmployees(self):
        employeeList = self.db.showEmployeeInformation()
        print(len(employeeList))
        for item in employeeList:
            widget = QWidget()
            employeeListWidget = Ui_smal_row_Widget()
            employeeListWidget.setupUi(widget)
            employeeListWidget.user_name_label.setText(item.employeeName + " " + item.employeeSurname)
            employeeListWidget.user_mail_label.setText(item.employeeMail)
            employeeListWidget.selected_btn.clicked.connect(lambda _, selectedEmployee = item : self.setEmployee(selectedEmployee))
            self.ui.employee_List_widget_layout.addWidget(widget)

    def setEmployee(self, selectedEmployee):
        self.connectMain.emit(selectedEmployee)
        self.close()


    def window_fix(self) :
        self.setWindowTitle("TaskJam Employee List")
        # self.setGeometry(1200,630,550,400)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint |Qt.FramelessWindowHint)
        self.ui.header_frame.mauseMoveEvent = self.mauseMoveEvent

    def mauseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
    def wheelEvent(self, event):
    # Tekerlek olayını yakala ve scroll işlemi yap
        if self.ui.employee_list_scrollArea.rect().contains(event.pos()) :
            delta = event.angleDelta().y() / 120  # Tekerleği kaydırma miktarını al
            self.ui.employee_list_scrollArea.verticalScrollBar().setValue(self.ui.employee_list_scrollArea.verticalScrollBar().value() - int(delta * 40))  # 20 birimlik bir kaydırma yap