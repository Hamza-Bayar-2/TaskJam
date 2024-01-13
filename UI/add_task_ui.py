# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\ui_add_task.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTask(object):
    def setupUi(self, AddTask):
        AddTask.setObjectName("AddTask")
        AddTask.resize(910, 400)
        AddTask.setMinimumSize(QtCore.QSize(910, 400))
        AddTask.setMaximumSize(QtCore.QSize(910, 400))
        AddTask.setStyleSheet("*{\n"
"font: 1000 12pt \"Montserrat\";\n"
"border : none ;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QWidget#AddTask{\n"
"background-color: rgb(7, 26, 35);\n"
"border-radius : 5px;\n"
"box-shadow: 15px 15px 15px 15px rgb(0, 0, 0);\n"
"border : 2px outset rgb(16, 16, 16);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(20, 69, 93);\n"
"border-radius : 5px;\n"
"padding : 3px;\n"
"box-shadow: 15px 15px 15px 15px rgb(0, 0, 0);\n"
"border : 2px outset rgb(16, 16, 16);\n"
"}\n"
"QPushButton{\n"
"box-shadow: 15px 15px 15px 15px rgb(0, 0, 0);\n"
"border : 2px outset rgb(16, 16, 16);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(AddTask)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(AddTask)
        self.main_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.main_frame.setStyleSheet("QFrame#main_frame{\n"
"background-color: rgb(7, 26, 35);\n"
"border-radius : 5px;\n"
"box-shadow: 15px 15px 15px 15px rgb(0, 0, 0);\n"
"border : 2px outset rgb(120, 120, 120);\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.addTask_header_freame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTask_header_freame.sizePolicy().hasHeightForWidth())
        self.addTask_header_freame.setSizePolicy(sizePolicy)
        self.addTask_header_freame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addTask_header_freame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addTask_header_freame.setObjectName("addTask_header_freame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.addTask_header_freame)
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_label = QtWidgets.QLabel(self.addTask_header_freame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QtCore.QSize(150, 0))
        self.title_label.setStyleSheet("color: rgb(229, 189, 48);\n"
"background-color: rgb(9, 38, 53);\n"
"border-radius : 5px;\n"
"padding : 6px;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label)
        self.winow_btn_frame = QtWidgets.QFrame(self.addTask_header_freame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winow_btn_frame.sizePolicy().hasHeightForWidth())
        self.winow_btn_frame.setSizePolicy(sizePolicy)
        self.winow_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.winow_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.winow_btn_frame.setObjectName("winow_btn_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.winow_btn_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exit_btn = QtWidgets.QPushButton(self.winow_btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setStyleSheet("border:none;")
        self.exit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Ellipse 5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_2.addWidget(self.exit_btn)
        self.horizontalLayout.addWidget(self.winow_btn_frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.addTask_header_freame, 0, QtCore.Qt.AlignTop)
        self.addTask_name_frame = QtWidgets.QFrame(self.main_frame)
        self.addTask_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addTask_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addTask_name_frame.setObjectName("addTask_name_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.addTask_name_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 22)
        self.horizontalLayout_9.setSpacing(25)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.task_name_label = QtWidgets.QLabel(self.addTask_name_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_name_label.sizePolicy().hasHeightForWidth())
        self.task_name_label.setSizePolicy(sizePolicy)
        self.task_name_label.setMinimumSize(QtCore.QSize(170, 0))
        self.task_name_label.setMaximumSize(QtCore.QSize(170, 16777215))
        self.task_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.task_name_label.setObjectName("task_name_label")
        self.horizontalLayout_9.addWidget(self.task_name_label, 0, QtCore.Qt.AlignLeft)
        self.task_name_lineEdit = QtWidgets.QLineEdit(self.addTask_name_frame)
        self.task_name_lineEdit.setMinimumSize(QtCore.QSize(240, 0))
        self.task_name_lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.task_name_lineEdit.setObjectName("task_name_lineEdit")
        self.horizontalLayout_9.addWidget(self.task_name_lineEdit, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addWidget(self.addTask_name_frame, 0, QtCore.Qt.AlignLeft)
        self.addTask_describe_frame = QtWidgets.QFrame(self.main_frame)
        self.addTask_describe_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addTask_describe_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addTask_describe_frame.setObjectName("addTask_describe_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.addTask_describe_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 29)
        self.horizontalLayout_4.setSpacing(24)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.task_describe_title = QtWidgets.QLabel(self.addTask_describe_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_describe_title.sizePolicy().hasHeightForWidth())
        self.task_describe_title.setSizePolicy(sizePolicy)
        self.task_describe_title.setMinimumSize(QtCore.QSize(170, 0))
        self.task_describe_title.setMaximumSize(QtCore.QSize(170, 16777215))
        self.task_describe_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.task_describe_title.setObjectName("task_describe_title")
        self.horizontalLayout_4.addWidget(self.task_describe_title, 0, QtCore.Qt.AlignLeft)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.addTask_describe_frame)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addWidget(self.addTask_describe_frame)
        self.addTask_date_row_frame = QtWidgets.QFrame(self.main_frame)
        self.addTask_date_row_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addTask_date_row_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addTask_date_row_frame.setObjectName("addTask_date_row_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.addTask_date_row_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.start_date_label = QtWidgets.QLabel(self.addTask_date_row_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_date_label.sizePolicy().hasHeightForWidth())
        self.start_date_label.setSizePolicy(sizePolicy)
        self.start_date_label.setMinimumSize(QtCore.QSize(170, 0))
        self.start_date_label.setMaximumSize(QtCore.QSize(170, 16777215))
        self.start_date_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_date_label.setObjectName("start_date_label")
        self.horizontalLayout_5.addWidget(self.start_date_label, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.addTask_date_row_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(7, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.starting_date_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.starting_date_lineEdit.setMinimumSize(QtCore.QSize(240, 0))
        self.starting_date_lineEdit.setMaximumSize(QtCore.QSize(240, 16777215))
        self.starting_date_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.starting_date_lineEdit.setObjectName("starting_date_lineEdit")
        self.verticalLayout_3.addWidget(self.starting_date_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.format_1 = QtWidgets.QLabel(self.frame_2)
        self.format_1.setStyleSheet("font: 10pt \"Montserrat\";")
        self.format_1.setObjectName("format_1")
        self.verticalLayout_3.addWidget(self.format_1, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.end_date_label = QtWidgets.QLabel(self.addTask_date_row_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_date_label.sizePolicy().hasHeightForWidth())
        self.end_date_label.setSizePolicy(sizePolicy)
        self.end_date_label.setMinimumSize(QtCore.QSize(150, 0))
        self.end_date_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.end_date_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.end_date_label.setObjectName("end_date_label")
        self.horizontalLayout_5.addWidget(self.end_date_label, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.addTask_date_row_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ending_datelineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.ending_datelineEdit.setMinimumSize(QtCore.QSize(240, 0))
        self.ending_datelineEdit.setMaximumSize(QtCore.QSize(240, 16777215))
        self.ending_datelineEdit.setText("")
        self.ending_datelineEdit.setObjectName("ending_datelineEdit")
        self.verticalLayout_2.addWidget(self.ending_datelineEdit, 0, QtCore.Qt.AlignRight)
        self.format_2 = QtWidgets.QLabel(self.frame_3)
        self.format_2.setStyleSheet("font: 10pt \"Montserrat\";")
        self.format_2.setObjectName("format_2")
        self.verticalLayout_2.addWidget(self.format_2, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_4.addWidget(self.addTask_date_row_frame)
        self.addTask_workers_row_frame = QtWidgets.QFrame(self.main_frame)
        self.addTask_workers_row_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addTask_workers_row_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addTask_workers_row_frame.setObjectName("addTask_workers_row_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.addTask_workers_row_frame)
        self.horizontalLayout_10.setSpacing(45)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.task_worker_label = QtWidgets.QLabel(self.addTask_workers_row_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_worker_label.sizePolicy().hasHeightForWidth())
        self.task_worker_label.setSizePolicy(sizePolicy)
        self.task_worker_label.setMinimumSize(QtCore.QSize(170, 0))
        self.task_worker_label.setMaximumSize(QtCore.QSize(170, 16777215))
        self.task_worker_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.task_worker_label.setObjectName("task_worker_label")
        self.horizontalLayout_10.addWidget(self.task_worker_label)
        self.select_there_label = QtWidgets.QLabel(self.addTask_workers_row_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_there_label.sizePolicy().hasHeightForWidth())
        self.select_there_label.setSizePolicy(sizePolicy)
        self.select_there_label.setMinimumSize(QtCore.QSize(170, 0))
        self.select_there_label.setMaximumSize(QtCore.QSize(170, 16777215))
        self.select_there_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.select_there_label.setObjectName("select_there_label")
        self.horizontalLayout_10.addWidget(self.select_there_label)
        self.workers_list_btn = QtWidgets.QPushButton(self.addTask_workers_row_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workers_list_btn.sizePolicy().hasHeightForWidth())
        self.workers_list_btn.setSizePolicy(sizePolicy)
        self.workers_list_btn.setStyleSheet("QPushButton{\n"
"padding : 6px;\n"
"background-color: rgb(20, 66, 114);\n"
"border-radius:5px;\n"
"font: 11pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: #2980b9; /* Fare üzerine gelindiğinde arkaplan rengi \n"
" }")
        self.workers_list_btn.setObjectName("workers_list_btn")
        self.horizontalLayout_10.addWidget(self.workers_list_btn)
        self.selected_worker_label = QtWidgets.QLabel(self.addTask_workers_row_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_worker_label.sizePolicy().hasHeightForWidth())
        self.selected_worker_label.setSizePolicy(sizePolicy)
        self.selected_worker_label.setStyleSheet("padding : 6px;\n"
"background-color: rgb(20, 69, 93);\n"
"border-radius:5px;\n"
"font: 11pt \"Montserrat\";\n"
"box-shadow: 15px 15px 15px 15px rgb(0, 0, 0);\n"
"border : 2px outset rgb(16, 16, 16);")
        self.selected_worker_label.setObjectName("selected_worker_label")
        self.horizontalLayout_10.addWidget(self.selected_worker_label, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.addTask_workers_row_frame)
        self.addTask_footer_frame = QtWidgets.QFrame(self.main_frame)
        self.addTask_footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addTask_footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addTask_footer_frame.setObjectName("addTask_footer_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.addTask_footer_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.project_dlete_btn = QtWidgets.QPushButton(self.addTask_footer_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_dlete_btn.sizePolicy().hasHeightForWidth())
        self.project_dlete_btn.setSizePolicy(sizePolicy)
        self.project_dlete_btn.setStyleSheet("*{\n"
"background-color: rgb(20, 66, 114);\n"
"border-radius : 5px ;\n"
"font: 600 12pt \"Montserrat\";\n"
"padding : 4px;\n"
"}\n"
":hover{\n"
"background-color: rgb(9, 33, 44);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/garbage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.project_dlete_btn.setIcon(icon1)
        self.project_dlete_btn.setIconSize(QtCore.QSize(20, 20))
        self.project_dlete_btn.setObjectName("project_dlete_btn")
        self.horizontalLayout_3.addWidget(self.project_dlete_btn)
        self.teher_project_label = QtWidgets.QLabel(self.addTask_footer_frame)
        self.teher_project_label.setObjectName("teher_project_label")
        self.horizontalLayout_3.addWidget(self.teher_project_label, 0, QtCore.Qt.AlignRight)
        self.will_add_project_label = QtWidgets.QLabel(self.addTask_footer_frame)
        self.will_add_project_label.setObjectName("will_add_project_label")
        self.horizontalLayout_3.addWidget(self.will_add_project_label, 0, QtCore.Qt.AlignHCenter)
        self.task_add_btn = QtWidgets.QPushButton(self.addTask_footer_frame)
        self.task_add_btn.setMinimumSize(QtCore.QSize(211, 0))
        self.task_add_btn.setMaximumSize(QtCore.QSize(211, 16777215))
        self.task_add_btn.setStyleSheet("QPushButton{\n"
"padding : 6px;\n"
"    background-color: rgb(33, 164, 62);\n"
"border-radius:5px;\n"
"font: 11pt \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 132, 28);\n"
" }")
        self.task_add_btn.setObjectName("task_add_btn")
        self.horizontalLayout_3.addWidget(self.task_add_btn)
        self.verticalLayout_4.addWidget(self.addTask_footer_frame)
        self.verticalLayout.addWidget(self.main_frame)

        self.retranslateUi(AddTask)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        _translate = QtCore.QCoreApplication.translate
        AddTask.setWindowTitle(_translate("AddTask", "Form"))
        self.title_label.setText(_translate("AddTask", "GÖREV EKLE"))
        self.task_name_label.setText(_translate("AddTask", "Görev Adı :"))
        self.task_describe_title.setText(_translate("AddTask", "Görev Açıklaması : "))
        self.start_date_label.setText(_translate("AddTask", "Başlangıç Tarihi :"))
        self.starting_date_lineEdit.setText(_translate("AddTask", "as"))
        self.format_1.setText(_translate("AddTask", "format : (gg.aa.yyyy)           "))
        self.end_date_label.setText(_translate("AddTask", "Bitiş Tarihi :"))
        self.format_2.setText(_translate("AddTask", "format : (gg.aa.yyyy)"))
        self.task_worker_label.setText(_translate("AddTask", "Görev Çalışanı :"))
        self.select_there_label.setText(_translate("AddTask", "Şuradan Seç"))
        self.workers_list_btn.setText(_translate("AddTask", "Çalışanlar Listesi"))
        self.selected_worker_label.setText(_translate("AddTask", "UserName"))
        self.project_dlete_btn.setText(_translate("AddTask", "Projeyi Sil"))
        self.teher_project_label.setText(_translate("AddTask", "Şu Projeye:"))
        self.will_add_project_label.setText(_translate("AddTask", "${Eklenecek Proje Adı"))
        self.task_add_btn.setText(_translate("AddTask", "PushButton"))
import image_rc
