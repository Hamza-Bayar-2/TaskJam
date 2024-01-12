from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout,QPushButton, QFrame
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import datetime
from UI.my_ui import Ui_MainWindow
from modals.taskInfo import TaskInfo
from database import db_Helper
from modals.userInfo import UserInfo
from add_project import AddProjectWindow
from UI.project_widget_ui import Ui_ProjectWindow

class MainWİndow(QMainWindow) :
    def __init__(self, userInfo) :
        super(MainWİndow, self).__init__()
        self.user = userInfo
        self.ui = Ui_MainWindow()
        self.db = db_Helper()
        
        self.window_fix()
        self.initUI()
    def initUI(self):
        self.ui.setupUi(self)
        self.setWindowTitle("TaskJam")
        # self.showMaximized() 
        self.buttonSetting()
        self.layoutSetting()
        self.labelSetting()
        self.setState()

    def setState(self):
        self.projectRowUpdate()
        self.verileri_guncelle()

    def buttonSetting(self):
        self.ui.exit_btn.clicked.connect(lambda : self.close())
        self.ui.bottom_line_btn.clicked.connect(lambda : self.showMinimized())
        self.ui.restore_btn.clicked.connect(lambda : self.WindowSize())
        self.ui.task_add_btn.clicked.connect(lambda : self.verileri_guncelle())
        self.ui.workers_page_btn.clicked.connect(lambda : self.changePage(1))
        self.ui.home_page_btn.clicked.connect(lambda : self.changePage(0))
        self.ui.signout_btn.clicked.connect(lambda : self.close())  # login ekranına yönlendirilebilir.
        self.ui.project_add_btn.clicked.connect(lambda : self.projectAdd())
    
    def projectAdd(self):
        self.projectAddWindow = AddProjectWindow(self.user)
        self.projectAddWindow.show()
        self.projectAddWindow.mainServer.connect(lambda veri : self.setState() if veri == "55 TAMM" else print("zort"))
            

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
        self.ui.user_name_label.setText(self.user.userName + " " + self.user.userSurname)
        self.ui.user_email_label.setText(self.user.userMail)

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

    def projectRowUpdate(self):
        self.clear_layout(self.ui.projects_scroll_content_layout)
        projects = self.db.showAllProjects(self.user.userID)
        for item in projects :
            widget = QWidget()
            projectWidget  =  Ui_ProjectWindow()
            projectWidget.setupUi(widget)
            projectWidget.project_name.setText(item.projectName)
            projectWidget.date_label.setText(f"{item.startingDate} - {item.endDate}")
            projectWidget.project_describe.setText(item.projectDescription)
            projectWidget.amount_label_2.setText('ihi')
            self.ui.projects_scroll_content_layout.addWidget(widget)


    def verileri_guncelle(self):
        users = [
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=2,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=3,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=4,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
        ]
        self.clear_layout(self.ui.will_done_scroll_area_content_layout)  #layout içerisindeki widgetları siliyoruz. ve yeniden dolduruyoruz.

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

    def wheelEvent(self, event):
    # Tekerlek olayını yakala ve scroll işlemi yap
        if self.ui.my_projects_frame.rect().contains(event.pos()):
            delta = event.angleDelta().y() / 120  # Tekerleği kaydırma miktarını al
            self.ui.projects_scroll.horizontalScrollBar().setValue(self.ui.projects_scroll.horizontalScrollBar().value() - int(delta * 20))  # 20 birimlik bir kaydırma yap
    
"""   projectRowUpdate a aittir...
 projectWidget = QWidget()
project_name_label = QLabel(item.projectName)
project_date_row_label = QLabel(f"{item.startingDate} - {item.endDate}") 
projectWidget.setMinimumHeight(100)
projectWidget.setStyleSheet(
    background-color: rgb(35, 39, 79);
    color: rgb(255, 255, 255);     
    border-radius : 10px;
)
projectWidgetLayout = QVBoxLayout(projectWidget)
projectWidgetTopLayout = QHBoxLayout(QFrame(projectWidget))
project_describe_label = QLabel(item.projectDescription)
projectWidgetLayout.addWidget(project_describe_label)
projectWidgetBottomLayout = QHBoxLayout(QFrame(projectWidget))
self.ui.projects_scroll_content_layout.setSpacing(20)
projectWidgetTopLayout.addWidget(project_name_label)
projectWidgetTopLayout.addWidget(project_date_row_label)
projectWidgetTopLayout.setAlignment(Qt.AlignTop)

self.ui.projects_scroll_content_layout.addWidget(projectWidget)
"""