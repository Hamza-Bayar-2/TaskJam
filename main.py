from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QScrollArea, QVBoxLayout, QSlider, QLabel, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from myui import Ui_MainWindow
from modals.taskInfo import TaskInfo

class MainWİndow(QMainWindow) :
    def __init__(self) :
        super(MainWİndow, self).__init__()
        self.ui = Ui_MainWindow()
        self.initUI()
    def initUI(self):
        self.ui.setupUi(self)
        self.setWindowTitle("TaskJam")
        self.showMaximized()

        self.verileri_guncelle()

    def verileri_guncelle(self):
        users = [
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
            TaskInfo(taskId=1,taskTitle="selam",adam_gun_deger= "1" , finishDate="11.01.2024", startDate="10.01.2024", isCompletedTime= True, lastTime = 1, projectId = 1 , status=True, workerId=1),
        ]
        self.lay1 = QVBoxLayout() #Tamamlanacaklar listesi için.s
        self.lay1.setAlignment(Qt.AlignTop)
        self.ui.will_done_scroll_area_content.setLayout(self.lay1)
        for i in users:
            a = QWidget(self)
            a.setMaximumSize(QSize(400,50))
            a.setMinimumSize(QSize(400,50))
            a.setStyleSheet("""
                    background-color: rgb(251, 255, 11);\n
                    color: rgb(0,0,255);\n
                    borderRadius : 1px;"""
            )            
            itemLayout = QHBoxLayout(self)
            a.setLayout(itemLayout)
            itemLayout.addWidget(QLabel(i.taskTitle))
            itemLayout.addWidget(QLabel(i.finishDate))
        
            self.lay1.addWidget(a)
        

def mainLOOP():
    fas = QApplication(sys.argv)
    win = MainWİndow()
    sys.exit(fas.exec_())

mainLOOP()