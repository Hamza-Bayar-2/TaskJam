from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QScrollArea, QVBoxLayout, QSlider, QLabel, QHBoxLayout,QPushButton
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import datetime
from UI.myui import Ui_MainWindow
from modals.taskInfo import TaskInfo

class MainWİndow(QMainWindow) :
    def __init__(self) :
        super(MainWİndow, self).__init__()
        self.ui = Ui_MainWindow()
        self.window_fix()
        self.initUI()
    def initUI(self):
        self.ui.setupUi(self)
        self.setWindowTitle("TaskJam")
        # self.showMaximized() 
        self.buttonSetting()
        self.layoutSetting()
        self.labelSetting()
        self.verileri_guncelle()

    def buttonSetting(self):
        self.ui.exit_btn.clicked.connect(lambda : self.close())
        self.ui.bottom_line_btn.clicked.connect(lambda : self.showMinimized())
        self.ui.restore_btn.clicked.connect(lambda : self.WindowSize())
        self.ui.task_add_btn.clicked.connect(lambda : self.verileri_guncelle())
        self.ui.workers_page_btn.clicked.connect(lambda : self.changePage(1))
        self.ui.home_page_btn.clicked.connect(lambda : self.changePage(0))
    
    def changePage(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        if index == 1:
            self.ui.workers_pointer.setPixmap(QPixmap(":/icons/icons/Ellipse 5.png"))
            self.ui.home_Pointer.clear()
        else :
            self.ui.home_Pointer.setPixmap(QPixmap(":/icons/icons/Ellipse 5.png"))
            self.ui.workers_pointer.clear()

    def labelSetting(self):
        now = datetime.datetime.now()
        nowdate = now.strftime('%d.%m.%Y')
        self.ui.date_label.setText(nowdate)

    def layoutSetting(self):
        self.ui.working_scroll_area_content_layout.setAlignment(Qt.AlignTop |Qt.AlignHCenter)
        self.ui.will_done_scroll_area_content_layout.setAlignment(Qt.AlignTop |Qt.AlignHCenter)
        self.ui.projects_scroll_content_layout.setAlignment(Qt.AlignLeft |Qt.AlignVCenter)
    

    def clear_layout(self, layout):
        # Layout içindeki tüm widgetları temizle
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def verileri_guncelle(self):
        users = [
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=2,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=3,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=4,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
        ]
        # self.clear_layout(self.ui.will_done_scroll_area_content_layout)  #layout içerisindeki widgetları siliyoruz. ve yeniden dolduruyoruz.

        for i in users:
            a = QWidget(self)
            a.setMinimumHeight(50)
            a.setMinimumWidth(500)
            a.setStyleSheet("""
                background-color: rgb(35, 39, 79);\n
                color: rgb(255, 255, 255);\n
                border-radius : 10px;"""
            )            
            itemLayout = QHBoxLayout(self)
            a.setLayout(itemLayout)
            itemLayout.addWidget(QLabel(i.taskTitle))
            itemLayout.addWidget(QLabel(i.finishDate))
            itemLayout.addWidget(QPushButton("Seç", clicked=lambda _, task = i : print(task.taskId)))
            self.ui.will_done_scroll_area_content_layout.addWidget(a)

    def WindowSize(self):
        if self.isMaximized:
              self.showNormal()
        else:
             self.showMaximized()
    def window_fix(self) :
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
            #self.ui.app_bar_widget.mauseMoveEvent = self.mauseMoveEvent
    def mauseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
