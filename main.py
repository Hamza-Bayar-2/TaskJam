from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout,QPushButton, QFrame, QSizePolicy
from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
from UI.my_ui import Ui_MainWindow
from modals.taskInfo import TaskInfo
from modals.employeeInfo import EmployeeInfo
from database import db_Helper
from add_project import AddProjectWindow
from UI.project_widget_ui import Ui_ProjectWindow
from UI.employee_list_widget_ui import Ui_Form
from UI.task_will_ui import Ui_TaskWill
from UI.task_done_widget_ui import Ui_DoneWidget
from UI.employee_info_widget_ui import Ui_inof_emp
from UI.employee_list_widget_small_ui import Ui_smal_row_Widget
from UI.task_edit_ui import Ui_TaskEdit
from UI.task_info_ui import Ui_TaskInfo
from project_update import  ProjectUpdate

class MainWİndow(QMainWindow) :
    def __init__(self, userInfo) :
        super(MainWİndow, self).__init__()
        self.user = userInfo
        self.ui = Ui_MainWindow()
        self.db = db_Helper()
        self.myProject = None
        self.myEmployee = None
        self.myTaskEmployee = None
        self.window_fix()
        self.initUI()

    def initUI(self):
        self.ui.setupUi(self)
        self.setWindowTitle("TaskJam")
        self.setWindowIcon(QIcon(':/image/officalLogo.png'))
        
        self.buttonSetting()
        self.layoutSetting()
        self.labelSetting()
        self.setState()

    def setState(self):
        self.projectRowUpdate()
        self.tasksTableUpdateAll() if(self.myProject !=None) else print("proje yok")
        self.employeeListWidgetUpdate()
        self.resetPageViewIndex()
        print("SetState Gerçekleşti")

    def resetPageViewIndex(self):
        self.ui.working_pageView.setCurrentIndex(0)
        self.ui.waiting_pageView.setCurrentIndex(0)
        self.ui.done_pageView.setCurrentIndex(0)

    def buttonSetting(self):
        self.ui.exit_btn.clicked.connect(lambda : self.close())
        self.ui.bottom_line_btn.clicked.connect(lambda : self.showMinimized())
        self.ui.restore_btn.clicked.connect(lambda : self.WindowSize())
        self.ui.task_add_btn.clicked.connect(lambda : self.taskAdd() if self.myProject != None else print("viyh"))
        self.ui.workers_page_btn.clicked.connect(lambda : self.changePage(1))
        self.ui.home_page_btn.clicked.connect(lambda : self.changePage(0))
        self.ui.signout_btn.clicked.connect(lambda : self.close())  # login ekranına yönlendirilebilir.
        self.ui.project_add_btn.clicked.connect(lambda : self.projectAdd())
        self.ui.emp_add_btn.clicked.connect(lambda : self.employeeAdd())

    def employeeListWidgetUpdate(self):
        self.clear_layout(self.ui.employee_list_scroll_area_content_layout)  #layout içerisindeki widgetları siliyoruz. ve yeniden dolduruyoruz.
        employeeList = self.db.showEmployeeInformation()
        self.ui.employee_amount_label.setText(str(len(employeeList)))
        for item in employeeList:
            mywidgets = QWidget()
            employeeListWidget = Ui_Form()
            employeeListWidget.setupUi(mywidgets)
            employeeListWidget.employee_name_label.setText(item.employeeName + " " + item.employeeSurname)
            employeeListWidget.employee_mail_label.setText(item.employeeMail)
            employeeListWidget.select_btn.clicked.connect(lambda _, selectedEmpployee = item : self.setEmployee(selectedEmpployee))
            self.ui.employee_list_scroll_area_content_layout.addWidget(mywidgets)
            if(self.myEmployee != None and self.myEmployee.employeeID == item.employeeID ):
                mywidgets.setStyleSheet("""
                    #Form{
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y1:0, stop:0 rgb(20, 66, 114), stop:0.6 rgb(7, 26, 35), stop:1 rgb(7, 26, 35));
                    }
                """)

    def setEmployee(self, selectedEmpployee):
        self.clear_layout(self.ui.willl_task_emp_inf_scrollArea_4)
        self.clear_layout(self.ui.willl_task_emp_inf_scrollArea_12)
        self.clear_layout(self.ui.willl_task_emp_inf_scrollArea_14)
        self.db.updateEmployeeAmountOfTasksCompletedOnTimeAndNotOnTime(selectedEmpployee.employeeID)
        listForEmployeInfo = self.db.showTasksBasedOnStatusAndEmployeeID(selectedEmpployee.employeeID)
        selectedEmp =  self.db.showSelectedEmployeeInfomation(selectedEmpployee.employeeID)

        self.myEmployee = selectedEmpployee
        self.ui.employee_detail_stackwidget.setCurrentIndex(1)
        self.ui.emp_name_detail_label_2.setText(self.myEmployee.employeeName)
        self.ui.emp_surname_detail_label_2.setText(self.myEmployee.employeeMail)
        self.ui.workers_delete_btn_2.clicked.connect(lambda : self.deleteEmployee())

        self.ui.completed_success_count_label_3.setText(str(selectedEmp.AmountOfTasksCompletedOnTime))
        self.ui.completed_unsucces_count_label_2.setText(str(selectedEmp.AmountOfTasksNotCompletedOnTime))

        self.ui.label_29.setText(str(len(listForEmployeInfo[0])))
        self.ui.label_33.setText(str(len(listForEmployeInfo[1])))
        self.ui.label_37.setText(str(len(listForEmployeInfo[2])))
        for item in listForEmployeInfo[0]:
            mywidget = QWidget()
            emplInfoWidget = Ui_inof_emp()
            emplInfoWidget.setupUi(mywidget)
            self.ui.willl_task_emp_inf_scrollArea_4.addWidget(mywidget)
            emplInfoWidget.startingDate.setText(item.startingDate)
            emplInfoWidget.endDAte.setText(item.endDate)
            emplInfoWidget.taskName.setText(item.taskName)

        for item in listForEmployeInfo[1]:
            mywidget = QWidget()
            emplInfoWidget = Ui_inof_emp()
            emplInfoWidget.setupUi(mywidget)
            self.ui.willl_task_emp_inf_scrollArea_12.addWidget(mywidget)
            emplInfoWidget.startingDate.setText(item.startingDate)
            emplInfoWidget.endDAte.setText(item.endDate)
            emplInfoWidget.taskName.setText(item.taskName)
            # emplInfoWidget.info_btn.clicked.connect(lambda:  )

        for item in listForEmployeInfo[2]:
            mywidget = QWidget()
            emplInfoWidget = Ui_inof_emp()
            emplInfoWidget.setupUi(mywidget)
            self.ui.willl_task_emp_inf_scrollArea_14.addWidget(mywidget)
            emplInfoWidget.startingDate.setText(item.startingDate)
            emplInfoWidget.endDAte.setText(item.endDate)
            emplInfoWidget.taskName.setText(item.taskName)


        self.setState()

    def deleteEmployee(self):
        self.ui.employee_detail_stackwidget.setCurrentIndex(0)
        self.db.deleteTasksWhenEmployeeDeleted(self.myEmployee.employeeID)
        self.db.deleteEmployeeID(self.myEmployee.employeeID)
        self.setState()

    def employeeAdd(self):
        empName = self.ui.emp_name_lineEdit.text()
        empSurname = self.ui.emp_surname_lineEdit.text()
        empMail = self.ui.emp_mail_lineEdit.text()

        if(0):
            self.ui.status_label.setText("aynı maile sahip zaten bir çalışan var")
            return
        elif(empMail == "" or empSurname == "" or empMail == ""):
            self.ui.status_label.setText("Boş bırakılamaz")
            return
        elif((empMail.find("@") == -1 ) or (empMail.find(".") == -1)):
            self.ui.status_label.setText("Email'i doğru biçimde giriniz.")
            return
        #validete yap cnm
        self.db.addNewEmployee(
            EmployeeInfo(
                userID = self.user.userID,
                employeeName= empName,
                employeeMail= empMail,
                employeeSurname= empSurname,
                employeeID=None,
                AmountOfTasksCompletedOnTime=None,
                AmountOfTasksNotCompletedOnTime=None,
            )
        )
        self.ui.emp_name_lineEdit.setText("")
        self.ui.emp_surname_lineEdit.setText("")
        self.ui.emp_mail_lineEdit.setText("")

        self.setState()

    def taskAdd(self):
        #proje seçiliyken tıklanmamsı gerekiyor.
        layout = self.ui.waiting_task_edit_page_layout
        page = self.ui.waiting_pageView
        page.setCurrentIndex(2)
        self.clear_layout(layout)
        myWidget = QWidget(self)
        taskAddWindow = Ui_TaskEdit()
        taskAddWindow.setupUi(myWidget)
        taskAddWindow.taskdt_name_label.setText("Görev Oluştur")
        taskAddWindow.taskdt_done_btn.setText("GÖREV EKLE")
        taskAddWindow.taskdt_exit_btn.clicked.connect(lambda : page.setCurrentIndex(0))
        taskAddWindow.taskdt_back_btn.clicked.connect(lambda : self.taskAdd())
        taskAddWindow.task_edit_emp_select_btn.clicked.connect(lambda : self.empTable(taskAddWindow))
        taskAddWindow.verticalLayout.addWidget(QLabel("Şu Projeye >>" + str(self.myProject.projectName)))
        taskAddWindow.task_edit_start_date_lineedit.setText(datetime.datetime.now().strftime('%d.%m.%Y'))
        taskAddWindow.taskdt_done_btn.clicked.connect(lambda : self.validateAndAddTask(taskAddWindow))
        layout.addWidget(myWidget)
        
    def validateAndAddTask(self, window):
        taskName = window.task_edit_name_lineedit.text()
        taskDesc = window.task_edit_desc_lineedit.text()
        taskStartDate = window.task_edit_start_date_lineedit.text()
        taskEndDate = window.task_edit_end_date_lineedit.text()
        taskEmployeeID = self.myTaskEmployee

        if(taskName == "" or taskDesc == "" or taskStartDate == "" or taskEndDate == "" or taskEmployeeID == None):
            window.working_edit_status_label.setText("Boş Bırakılamaz")
        elif(self.validateDate(taskStartDate, taskEndDate)):
            window.working_edit_status_label.setText("Tarih Formatı (gg.aa.yyyy) olmalıdır.")
        elif(self.dateNow > self.dateLater):
            window.working_edit_status_label.setText("Başlangıç Tarihi Bitiş Tarihinden Önce olamaz")
        else:
            self.db.addNewTask(TaskInfo(
                taskID= None,
                employeeID= self.myTaskEmployee.employeeID,
                projectID= self.myProject.projectID,
                taskName= taskName,
                taskDescription= taskDesc,
                startingDate= taskStartDate,
                endDate= taskEndDate,
                delayAmount=0,
                taskStatus=0
            ))
            self.setState()

    def projectAdd(self):
        self.projectAddWindow = AddProjectWindow(self.user)
        self.projectAddWindow.show()
        self.projectAddWindow.mainServer.connect(lambda veri : self.setState() if veri == "55 TAMM" else print("zort"))

    def changePage(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        if index == 1:
            self.ui.workers_pointer.setPixmap(QPixmap(":/icons/icons/Ellipse 5.png"))
            self.ui.workers_page_btn.setStyleSheet("""
                background: rgba(76, 175, 80, 0);
                font: 2000 9pt "Montserrat";
                color : rgb(229, 189, 48);
                """)
            self.ui.home_page_btn.setStyleSheet("""
                background: rgba(76, 175, 80, 0);
                font: 2000 9pt "Montserrat";
                """)
            self.ui.home_Pointer.clear()
        else :
            self.ui.home_page_btn.setStyleSheet("""
                background: rgba(76, 175, 80, 0);
                font: 2000 9pt "Montserrat";
                color : rgb(229, 189, 48);
                """)
            self.ui.workers_page_btn.setStyleSheet("""
                background: rgba(76, 175, 80, 0);
                font: 2000 9pt "Montserrat";
                """)
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
        self.ui.will_done_scroll_area_content_layout_2.setAlignment(Qt.AlignTop |Qt.AlignHCenter)
        self.ui.projects_scroll_content_widget_layout.setAlignment(Qt.AlignLeft |Qt.AlignVCenter)

    def clear_layout(self, layout):
        # Layout içindeki tüm widgetları temizle
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def projectRowUpdate(self):
        self.clear_layout(self.ui.projects_scroll_content_widget_layout)
        projects = self.db.showAllProjects(self.user.userID)
        self.ui.project_count_label.setText(str(self.db.activeProjectsAmount()) + "\nAktif") # aktiflik kontrolunu yapmamız lazım
        for item in projects :
            widget = QWidget()
            projectWidget  =  Ui_ProjectWindow()
            projectWidget.setupUi(widget)
            projectWidget.project_name.setText(item.projectName)
            projectWidget.date_label.setText(f"{item.startingDate} - {item.endDate}")
            projectWidget.project_describe.setText(item.projectDescription)
            projectWidget.amount_label_2.setText(str(self.db.showTotalNumberOfEmployeesInTheProject(item.projectID)))
            self.ui.projects_scroll_content_widget_layout.addWidget(widget)
            projectWidget.select_btn_2.clicked.connect(lambda _, project = item: self.setMyProject(project))
            projectWidget.show_btn_2.clicked.connect(lambda _, selectedProject = item : self.editProject(selectedProject))
            if(self.myProject == None or self.myProject.projectID == item.projectID):
                if(self.myProject == None):
                    self.myProject = item
                widget.setStyleSheet(
                    """*{
                        border : none ;
                        border-radius : 5px;
                        color: rgb(255, 255, 255);
                        font: 11pt "Montserrat";
                    }
                    QWidget#ProjectWindow{
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(20, 69, 93), stop:1 rgb(9, 38, 53));
                        border : 2px outset rgb(16, 16, 16);
                    }
                """)
                projectWidget.select_btn_2.deleteLater()

    def editProject(self, selectedProject):
        updateProject = ProjectUpdate(selectedProject)
        updateProject.show()
        updateProject.mainServer.connect(lambda veri : self.setState() if veri == "55 TAMM" else print("zort"))
        print(self.db.showAllProjects(self.user.userID))

    def setMyProject(self, item):
        self.myProject = item
        self.setState()

    def tasksTableUpdateAll(self):
        #layout içerisindeki widgetları siliyoruz. ve yeniden dolduruyoruz.
        self.clear_layout(self.ui.done_scroll_area_cotent_layout_2)
        self.clear_layout(self.ui.working_scroll_area_content_layout)
        self.clear_layout(self.ui.will_done_scroll_area_content_layout_2)

        listOfAllTasks = self.db.showTasksBasedOnStatusAndProjectID(projectID= self.myProject.projectID)
        # users = self.db.
        self.loadWillTask(listOfAllTasks[0])
        self.loadWorkingTask(listOfAllTasks[1])
        self.loadDoneTask(listOfAllTasks[2])

    def loadDoneTask(self, listOfAllTasks):
        if(len(listOfAllTasks) == 0):
            notInfo = QLabel(self.ui.done_scroll_area_frame_2)
            notInfo.setPixmap(QPixmap(":/image/icons/astronot_waiting_roket.png"))
            notInfo.setScaledContents(True)
            notInfo.setAlignment(Qt.AlignCenter)
            notInfo.setMaximumSize(QSize(100, 110))
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            notInfo.setStyleSheet(
                """
                padding : 15px;
                border-radius :25px;
                background-color: rgb(9, 38, 53);
                """)
            yazi = QLabel("Veri Yok")
            self.ui.done_scroll_area_frame_2.setSizePolicy(sizePolicy)
            yazi.setStyleSheet("""
                padding : 10px;
                border-radius :15px;
                background-color: rgb(9, 38, 53);
            """)
            self.ui.done_scroll_area_cotent_layout_2.addWidget(notInfo,Qt.AlignCenter)
        else:
            for item in listOfAllTasks: #TAMAMLANACAK BÖLGESİ İÇİN
                fark = (datetime.datetime.now() - self.convertDateFromStr(item.endDate)).days
                widget = QWidget(self)
                taskWillWidget =  Ui_DoneWidget()
                taskWillWidget.setupUi(widget)
                taskWillWidget.last_day_result_label.deleteLater()
                taskWillWidget.text_label.deleteLater()
                print("my Dleay amounT= " + str(item.delayAmount))
                if(fark > 0 and item.delayAmount != 0 ):
                    taskWillWidget.label.setPixmap(QPixmap(":/icons/icons/red_set.png"))
                    label = QLabel("Geç Teslim")
                else:
                    taskWillWidget.label.setPixmap(QPixmap(":/icons/icons/green_set.png"))
                    label = QLabel("Zamanında Teslim")
                taskWillWidget.verticalLayout_2.addWidget(label)
                self.ui.done_scroll_area_cotent_layout_2.addWidget(widget)
                taskWillWidget.taskname_label.setText(item.taskName)
                taskWillWidget.describe_label.setText(item.taskDescription)
                #gecikme olduğuunu kontrol ett
                taskWillWidget.employee_label.setText(self.db.showSelectedEmployeeInfomation(employeeID=item.employeeID).employeeName + " " + self.db.showSelectedEmployeeInfomation(employeeID=item.employeeID).employeeSurname)
                #belirlenen sürede tamamlandı mı ??
                # taskWillWidget.delete_btn.clicked.connect(lambda _, task = item : self.db.deleteTask(item.taskID))
                taskWillWidget.delete_btn.clicked.connect(lambda _, task = item : self.changeStatusTask(task,1))
                taskWillWidget.delete_btn.clicked.connect(lambda: self.setState())
                taskWillWidget.show_btn.clicked.connect(lambda _, task = item : self.openTasskInfo(task, 2))

    def loadWorkingTask(self, listOfAllTasks):
        if(len(listOfAllTasks) == 0):
            notInfo = QLabel(self.ui.working_scroll_area_content)
            notInfo.setPixmap(QPixmap(":/image/icons/astronot_not_knowing.png"))
            notInfo.setScaledContents(True)
            notInfo.setAlignment(Qt.AlignCenter)
            notInfo.setMaximumSize(QSize(100, 85))
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            notInfo.setStyleSheet(
                """
                padding : 15px;
                border-radius :25px;
                background-color: rgb(9, 38, 53);
                """)
            yazi = QLabel("Veri Yok")

            yazi.setStyleSheet("""
                padding : 10px;
                border-radius :15px;
                background-color: rgb(9, 38, 53);
            """)
            self.ui.working_scroll_area_content.setSizePolicy(sizePolicy)
            self.ui.working_scroll_area_content_layout.addWidget(notInfo,Qt.AlignCenter)
            self.ui.working_scroll_area_content_layout.addWidget(yazi,Qt.AlignCenter)
        else:
            for item in listOfAllTasks: #TAMAMLANACAK BÖLGESİ İÇİN
                fark = (datetime.datetime.now() - self.convertDateFromStr(item.endDate)).days
                widget = QWidget(self)
                taskWillWidget =  Ui_TaskWill()
                taskWillWidget.setupUi(widget)
                self.ui.working_scroll_area_content_layout.addWidget(widget)
                taskWillWidget.taskname_label.setText(item.taskName)
                taskWillWidget.describe_label.setText(item.taskDescription)
                icon1 = QIcon()
                icon1.addPixmap(QPixmap(":/icons/icons/tick.png"),QIcon.Normal, QIcon.Off)
                taskWillWidget.resume_btn.setIcon(icon1)
                taskWillWidget.text_label_3.setText("Görevi\nTamamla")
                if (fark > 0 and item.delayAmount == 0 ):
                    taskWillWidget.end_date_label.setText(datetime.datetime.strftime(datetime.datetime.now(),"%d.%m.%Y"))
                    # taskWillWidget.end_date_frame.deleteLater()
                    # taskWillWidget.starting_date_frame.deleteLater()
                    taskWillWidget.label.setPixmap(QPixmap(":/icons/icons/red_set.png"))
                    taskWillWidget.last_day_result_label.setText(str(fark) + " Gün gecikti")
                    taskWillWidget.text_label.setText("En kısa zamanda bitirin")
                    # otherTAsk = QFrame(myFrame)
                    # otherTAsk.setLayout(QHBoxLayout("myLayout"))
                    # otherTAsk.myLayout.addWidget(QLabel("Görev"))
                else :
                    if(fark == 0):
                        taskWillWidget.last_day_result_label.setText("Bugün içerisinde")
                    else:
                        taskWillWidget.last_day_result_label.setText(str(abs(fark)) + "  Gün içinde")
                    taskWillWidget.text_label.setText("Bitmesi Gerekiyor")
                    taskWillWidget.end_date_label.setText(item.endDate)
                taskWillWidget.show_btn.setStyleSheet("""
                    *{
                        background-color: rgb(229, 189, 48);
                        border-radius : 5px;
                        color : rgb(0,0,0);
                    }
                    :hover{
                        background-color: rgb(175, 143, 36);
                    }""")
                taskWillWidget.show_btn.setText("Şu an da İşlem Görüyor. Detay Görüntüle")
                taskWillWidget.starting_date_label.setText(item.startingDate)
                taskWillWidget.employee_label.setText(self.db.showSelectedEmployeeInfomation(employeeID=item.employeeID).employeeName + " " + self.db.showSelectedEmployeeInfomation(employeeID=item.employeeID).employeeSurname)
                # taskWillWidget.delete_btn.clicked.connect(lambda _, task = item : self.db.deleteTask(item.taskID))
                taskWillWidget.delete_btn.clicked.connect(lambda _, task = item : self.changeStatusTask(task, 0))
                taskWillWidget.delete_btn.clicked.connect(lambda: self.setState())
                taskWillWidget.resume_btn.clicked.connect(lambda _, task2 = item : self.changeStatusTask(task2, 2))
                taskWillWidget.resume_btn.clicked.connect(lambda : self.setState())
                taskWillWidget.show_btn.clicked.connect(lambda _, task = item: self.openTasskInfo(task, 1))

    def loadWillTask(self, listOfAllTasks):
        if(len(listOfAllTasks) == 0):
            notInfo = QLabel(self.ui.will_done_scroll_area_content_2)
            notInfo.setPixmap(QPixmap(":/image/icons/astronot_waiting_wall.png"))
            notInfo.setScaledContents(True)
            notInfo.setAlignment(Qt.AlignCenter)
            notInfo.setMaximumSize(QSize(80, 110))
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            notInfo.setStyleSheet(
                """
                padding : 15px;
                border-radius :25px;
                background-color: rgb(9, 38, 53);
                """)
            yazi = QLabel("Veri Yok")

            yazi.setStyleSheet("""
                padding : 10px;
                border-radius :15px;
                background-color: rgb(9, 38, 53);
            """)
            self.ui.will_done_scroll_area_content_2.setSizePolicy(sizePolicy)
            self.ui.will_done_scroll_area_content_layout_2.addWidget(notInfo,Qt.AlignCenter)
            self.ui.will_done_scroll_area_content_layout_2.addWidget(yazi,Qt.AlignCenter)
        else:
            for item in listOfAllTasks: #TAMAMLANACAK BÖLGESİ İÇİN
                fark = (datetime.datetime.now() - self.convertDateFromStr(item.endDate)).days
                widget = QWidget(self)
                taskWillWidget =  Ui_TaskWill()
                taskWillWidget.setupUi(widget)
                self.ui.will_done_scroll_area_content_layout_2.addWidget(widget)
                taskWillWidget.taskname_label.setText(item.taskName)
                taskWillWidget.describe_label.setText(item.taskDescription)
                if (fark > 0 and item.delayAmount == 0 ):
                    taskWillWidget.end_date_label.setText(datetime.datetime.strftime(datetime.datetime.now(),"%d.%m.%Y"))
                    taskWillWidget.label.setPixmap(QPixmap(":/icons/icons/red_set.png"))
                    taskWillWidget.last_day_result_label.setText(str(fark) + " Gün gecikti")
                    taskWillWidget.text_label.setText("En kısa zamanda bitirin")
                else :
                    if(fark == 0):
                        taskWillWidget.last_day_result_label.setText("Bugün içerisinde")
                    else:
                        taskWillWidget.last_day_result_label.setText(str(abs(fark)) + "  Gün içinde")
                    taskWillWidget.text_label.setText("Bitmesi Gerekiyor")
                    taskWillWidget.end_date_label.setText(item.endDate)
                taskWillWidget.starting_date_label.setText(item.startingDate)
                taskWillWidget.employee_label.setText(self.db.showSelectedEmployeeInfomation(employeeID=item.employeeID).employeeName + " " + self.db.showSelectedEmployeeInfomation(employeeID=item.employeeID).employeeSurname)
                # taskWillWidget.delete_btn.clicked.connect(lambda _, task = item : self.db.deleteTask(item.taskID))
                taskWillWidget.delete_btn.clicked.connect(lambda _, task = item : self.db.deleteTask(task.taskID))
                taskWillWidget.delete_btn.clicked.connect(lambda: self.setState())
                taskWillWidget.resume_btn.clicked.connect(lambda _, task2 = item : self.changeStatusTask(task2, 1))
                taskWillWidget.resume_btn.clicked.connect(lambda : self.setState())
                taskWillWidget.show_btn.clicked.connect(lambda _, task = item: self.openTasskInfo(task, 0))

    def openTasskInfo(self, item, slot):
        if slot == 1 :
            page = self.ui.working_pageView
            layout = self.ui.working_task_detail_show_page_layout
        elif slot == 0:
            page = self.ui.waiting_pageView
            layout = self.ui.waiting_task_detail_page_layoout
        else :
            page = self.ui.done_pageView
            layout = self.ui.done_task_detail_page_layout
        page.setCurrentIndex(1)
        self.clear_layout(layout)
        myWidget = QWidget(self)
        infoWindow = Ui_TaskInfo()
        infoWindow.setupUi(myWidget)
        layout.addWidget(myWidget)
        infoWindow.taskdt_exit_btn.clicked.connect(lambda : page.setCurrentIndex(0))

        fark = (datetime.datetime.now() - self.convertDateFromStr(item.endDate)).days #geçme süresi
        if (fark > 0 and item.delayAmount == 0):
            infoWindow.taskdt_end_Dare_label.setText(datetime.datetime.strftime(datetime.datetime.now(),"%d.%m.%Y"))
            infoWindow.label_6.deleteLater()
            infoWindow.las_day_for_end.deleteLater()
            Label = QLabel()
            Label.setMaximumSize(QSize(15, 15))
            Label.setPixmap(QPixmap(":/icons/icons/rect_attention.png"))

            Label2 = QLabel(" Görev ")
            Label3 = QLabel(str(fark) + "Gün Gecikti ")
            Label3.setStyleSheet('''
                    font: 600 10pt"Montserrat";
                    ''')
            Label4 = QLabel("bitmesi Gerekiyordu")
            myFrame = QFrame()
            myLayout= QHBoxLayout()
            myFrame.setLayout(myLayout)
            infoWindow.verticalLayout_22.addWidget(myFrame)
            myLayout.addWidget(Label)
            myLayout.addWidget(Label2)
            myLayout.addWidget(Label3)
            myLayout.addWidget(Label4)
            sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            myFrame.setContentsMargins(5,0,5,0)
            myFrame.setSizePolicy(sizePolicy)
        else:
            infoWindow.taskdt_end_Dare_label.setText(item.endDate)
            if(fark > 0 and item.delayAmount != 0):
                infoWindow.label_2.setPixmap(QPixmap(":/icons/icons/red_set_big.png"))
                infoWindow.label_6.setText(str(item.delayAmount) + " Gün")
                infoWindow.las_day_for_end.setText("Geç Teslim edilmiş")
            elif(fark <= 0 and item.taskStatus == 2):
                infoWindow.label_3.setPixmap(QPixmap(":/icons/icons/green_set_horizantal_big.png"))
                infoWindow.label_2.setPixmap(QPixmap(":/icons/icons/green_set_big.png"))
                infoWindow.label_6.setText("Harika")
                infoWindow.las_day_for_end.setText("Tam zamanında Teslim Edildi")
            else:
                infoWindow.label_3.setPixmap(QPixmap(":/icons/icons/yellow_set_horizantal_big.png"))
                if fark == 0 :
                    infoWindow.label_6.setText("Bugün İçerisinde")
                    infoWindow.las_day_for_end.setText("Bitmesi Gerekiyor.")
                else:       
                    infoWindow.las_day_for_end.setText(str(abs(fark)) + " Gün Kaldı")
                    infoWindow.taskdt_end_Dare_label.setText(item.endDate)
        if item.taskStatus == 0:
            infoWindow.taskdt_done_btn.setText("Görevi\nBaşlat")
            infoWindow.taskdt_done_btn.setIcon(QIcon(":/icons/icons/resume.png"))
        elif item.taskStatus == 2:
            infoWindow.taskdt_done_btn.deleteLater()
    
        infoWindow.taskdt_name_label.setText(item.taskName)
        infoWindow.taskdt_desk_labell.setText(item.taskDescription)
        infoWindow.taskdt_starting_date_label.setText(item.startingDate)
        infoWindow.taskdt_emp_name_label.setText(self.db.showSelectedEmployeeInfomation(employeeID=item.employeeID).employeeName + " " + self.db.showSelectedEmployeeInfomation(employeeID=item.employeeID).employeeSurname)
        infoWindow.taskdt_delete_btn.clicked.connect(lambda :self.db.deleteTask(item.taskID))
        infoWindow.taskdt_done_btn.clicked.connect(lambda : self.changeStatusTask(item, 2))
        infoWindow.taskdt_exit_btn.clicked.connect(lambda : page.setCurrentIndex(0))
        infoWindow.taskdt_edit_btn.clicked.connect(lambda : self.openTaskEdit(item, slot))
        infoWindow.taskdt_delete_btn.clicked.connect(lambda _, task = item: self.db.deleteTask(task.taskID))
        infoWindow.taskdt_delete_btn.clicked.connect(lambda : self.setState())

    def openTaskEdit(self, item, slot):
        if slot == 1 :
            page = self.ui.working_pageView
            layout = self.ui.working_task_edit_page_layout
        elif slot == 0:
            page = self.ui.waiting_pageView
            layout = self.ui.waiting_task_edit_page_layout
        else :
            page = self.ui.done_pageView
            layout = self.ui.done_task_edit_page_layout
        page.setCurrentIndex(2)
        self.clear_layout(layout)
        myWidget = QWidget(self)
        self.editWindow = Ui_TaskEdit()
        self.editWindow.setupUi(myWidget)
        self.editWindow.taskdt_name_label.setText(item.taskName)
        self.editWindow.task_edit_name_lineedit.setText(item.taskName)
        self.editWindow.task_edit_desc_lineedit.setText(item.taskDescription)
        self.editWindow.task_edit_start_date_lineedit.setText(item.startingDate)
        self.editWindow.task_edit_end_date_lineedit.setText(item.endDate)
        self.editWindow.task_edit_emp_name_label.setText(self.db.showSelectedEmployeeInfomation(item.employeeID).employeeName + " " + self.db.showSelectedEmployeeInfomation(item.employeeID).employeeSurname)
        self.editWindow.task_edit_emp_select_btn.clicked.connect(lambda : self.empTable(self.editWindow))
        self.editWindow.taskdt_exit_btn.clicked.connect(lambda : page.setCurrentIndex(0))
        self.editWindow.taskdt_back_btn.clicked.connect(lambda : self.openTaskEdit(item, slot))
        self.editWindow.taskdt_done_btn.clicked.connect(lambda : self.saveTask(item, page)) 
        layout.addWidget(myWidget)

    def saveTask(self, task, page):
        taskName = self.editWindow.task_edit_name_lineedit.text()
        taskDesc = self.editWindow.task_edit_desc_lineedit.text()
        taskStartDate = self.editWindow.task_edit_start_date_lineedit.text()
        taskEndDate = self.editWindow.task_edit_end_date_lineedit.text()
        taskEmployeeId = self.myTaskEmployee

        
        if(taskName == "" or taskDesc == "" or taskStartDate == "" or taskEndDate == ""):
            self.editWindow.working_edit_status_label.setText("Boş Bırakılamaz")
        elif(self.validateDate(taskStartDate, taskEndDate)):
            self.editWindow.working_edit_status_label.setText("Tarih Formatı (gg.aa.yyyy) olmalıdır.")
        elif(self.dateNow > self.dateLater):
            self.editWindow.working_edit_status_label.setText("Başlangıç Tarihi Bitiş Tarihinden Önce olamaz")
        else:
            if(taskEmployeeId == None):
                taskEmployeeId = task
            self.db.updateTask(
                taskID= task.taskID,
                employeeID= taskEmployeeId.employeeID,
                taskName= taskName,
                taskDescription= taskDesc,
                startingDate= taskStartDate,
                endDate= taskEndDate
            )
            page.setCurrentIndex
            self.setState()
    def validateDate(self, taskStartDate, taskEndDate):
        try:
            self.dateNow = datetime.datetime.strptime(taskStartDate, "%d.%m.%Y")
            self.dateLater = datetime.datetime.strptime(taskEndDate, "%d.%m.%Y")
            return False
        except ValueError:
            return True
       
    def empTable(self,window):
        liste = self.db.showEmployeeInformation()
        self.clear_layout(window.emp_list_scroll_frame_layout)
        window.task_edit_pageView.setCurrentIndex(1)
        for index in liste :
            widget = QWidget()
            item = Ui_smal_row_Widget()
            item.setupUi(widget)
            item.user_name_label.setText(index.employeeName)
            item.user_mail_label.setText(index.employeeMail)
            item.selected_btn.clicked.connect(lambda _,i = index : self.setMyTaskEmployee(i, window))
            window.emp_list_scroll_frame_layout.addWidget(widget)

    def setMyTaskEmployee(self, employee, window):
        self.myTaskEmployee = employee
        window.task_edit_pageView.setCurrentIndex(0)
        window.task_edit_emp_name_label.setText(employee.employeeName + " " + employee.employeeSurname)

    def convertDateFromStr(self, strDate):
        today = datetime.datetime.strptime(strDate,"%d.%m.%Y")
        return today

    def changeStatusTask(self, task, statusMode):
        if(statusMode == 2):
            fark = (datetime.datetime.now() - self.convertDateFromStr(task.endDate)).days
            if fark > 0 :
                self.db.updateTaskDelayAmount(task.taskID)
        else:
            self.db.changeTaskDelayAmount(task.taskID,0)
        self.db.updateTaskStatus(statusMode, task.taskID)
        self.setState()
        

    def WindowSize(self):
        if self.isMaximized():  # Eğer pencere küçültülmüşse
            self.showNormal()    # Normal boyutta göster
        else:
            self.showMaximized()
    def window_fix(self) :
            # self.ui.app_bar_frame.mauseMoveEvent = self.mauseMoveEvent
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
            #self.ui.app_bar_widget.mauseMoveEvent = self.mauseMoveEvent
    def mauseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    def mausePressEvent(self, event):
        self.oldPos = event.globalPos()
    def wheelEvent(self, event):
    # Tekerlek olayını yakala ve scroll işlemi yap

        if self.ui.main_top_right_frame.rect().contains(event.pos()) or self.ui.main_top_bar_frame.rect().contains(event.pos()):
            delta = event.angleDelta().y() / 120  # Tekerleği kaydırma miktarını al
            self.ui.projects_scroll.horizontalScrollBar().setValue(self.ui.projects_scroll.horizontalScrollBar().value() - int(delta * 40))  # 20 birimlik bir kaydırma yap
        elif(self.ui.employee_list_scroll_area.rect().contains(event.pos())):
            delta = event.angleDelta().y() / 120  # Tekerleği kaydırma miktarını al
            self.ui.employee_list_scroll_area.verticalScrollBar().setValue(self.ui.employee_list_scroll_area.verticalScrollBar().value() - int(delta * 40))
        elif(self.ui.working_pageView.currentIndex == 2 or self.ui.waiting_pageView.currentIndex == 2 or self.ui.done_pageView.currentIndex == 2):
            if(self.editWindow is not None and self.editWindow.emp_list_window_scrolArea.rect().contains(event.pos())):
                delta = event.angleDelta().y() / 120  # Tekerleği kaydırma miktarını al
                self.editWindow.emp_list_window_scrolArea.verticalScrollBar().setValue(self.editWindow.emp_list_window_scrolArea.verticalScrollBar().value() - int(delta * 40))
