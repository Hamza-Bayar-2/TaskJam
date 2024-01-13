# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\ui_task_will.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaskWill(object):
    def setupUi(self, TaskWill):
        TaskWill.setObjectName("TaskWill")
        TaskWill.resize(532, 195)
        TaskWill.setMaximumSize(QtCore.QSize(532, 195))
        self.horizontalLayout = QtWidgets.QHBoxLayout(TaskWill)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_frame = QtWidgets.QFrame(TaskWill)
        self.main_frame.setStyleSheet("QFrame#main_frame{\n"
"background-color: rgb(9, 38, 53);\n"
"border-raius : 5px;\n"
"\n"
"border : 2px outset rgb(16, 16, 16);\n"
"}\n"
"*{\n"
"color: rgb(255, 255, 255);\n"
"font: 600 9pt \"Montserrat\";\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(10, 7, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pointer_label = QtWidgets.QLabel(self.header_frame)
        self.pointer_label.setMinimumSize(QtCore.QSize(15, 15))
        self.pointer_label.setMaximumSize(QtCore.QSize(15, 15))
        self.pointer_label.setText("")
        self.pointer_label.setPixmap(QtGui.QPixmap(":/icons/icons/Ellipse 5.png"))
        self.pointer_label.setScaledContents(True)
        self.pointer_label.setObjectName("pointer_label")
        self.horizontalLayout_2.addWidget(self.pointer_label)
        self.taskname_label = QtWidgets.QLabel(self.header_frame)
        self.taskname_label.setObjectName("taskname_label")
        self.horizontalLayout_2.addWidget(self.taskname_label)
        self.header_right_frame = QtWidgets.QFrame(self.header_frame)
        self.header_right_frame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.header_right_frame.setStyleSheet("\n"
"")
        self.header_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_right_frame.setObjectName("header_right_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.header_right_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.last_day_result_label = QtWidgets.QLabel(self.header_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.last_day_result_label.sizePolicy().hasHeightForWidth())
        self.last_day_result_label.setSizePolicy(sizePolicy)
        self.last_day_result_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.last_day_result_label.setObjectName("last_day_result_label")
        self.verticalLayout_2.addWidget(self.last_day_result_label, 0, QtCore.Qt.AlignRight)
        self.text_label = QtWidgets.QLabel(self.header_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_label.sizePolicy().hasHeightForWidth())
        self.text_label.setSizePolicy(sizePolicy)
        self.text_label.setStyleSheet("font: 9pt \"Montserrat\";")
        self.text_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_label.setObjectName("text_label")
        self.verticalLayout_2.addWidget(self.text_label, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addWidget(self.header_right_frame)
        self.label = QtWidgets.QLabel(self.header_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/yellow_set.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.header_frame)
        self.describe_label = QtWidgets.QLabel(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.describe_label.sizePolicy().hasHeightForWidth())
        self.describe_label.setSizePolicy(sizePolicy)
        self.describe_label.setObjectName("describe_label")
        self.verticalLayout.addWidget(self.describe_label)
        self.employee_label = QtWidgets.QLabel(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employee_label.sizePolicy().hasHeightForWidth())
        self.employee_label.setSizePolicy(sizePolicy)
        self.employee_label.setObjectName("employee_label")
        self.verticalLayout.addWidget(self.employee_label)
        self.date_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_frame.sizePolicy().hasHeightForWidth())
        self.date_frame.setSizePolicy(sizePolicy)
        self.date_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.date_frame.setObjectName("date_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.date_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.starting_date_frame = QtWidgets.QFrame(self.date_frame)
        self.starting_date_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.starting_date_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.starting_date_frame.setObjectName("starting_date_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.starting_date_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.date_title = QtWidgets.QLabel(self.starting_date_frame)
        self.date_title.setStyleSheet("font: 9pt \"Montserrat\";")
        self.date_title.setAlignment(QtCore.Qt.AlignCenter)
        self.date_title.setObjectName("date_title")
        self.verticalLayout_3.addWidget(self.date_title)
        self.starting_date_label = QtWidgets.QLabel(self.starting_date_frame)
        self.starting_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.starting_date_label.setObjectName("starting_date_label")
        self.verticalLayout_3.addWidget(self.starting_date_label)
        self.horizontalLayout_3.addWidget(self.starting_date_frame)
        self.end_date_frame = QtWidgets.QFrame(self.date_frame)
        self.end_date_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.end_date_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.end_date_frame.setObjectName("end_date_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.end_date_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.date_title_2 = QtWidgets.QLabel(self.end_date_frame)
        self.date_title_2.setStyleSheet("font: 9pt \"Montserrat\";")
        self.date_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.date_title_2.setObjectName("date_title_2")
        self.verticalLayout_4.addWidget(self.date_title_2)
        self.starting_date_label_2 = QtWidgets.QLabel(self.end_date_frame)
        self.starting_date_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.starting_date_label_2.setObjectName("starting_date_label_2")
        self.verticalLayout_4.addWidget(self.starting_date_label_2)
        self.horizontalLayout_3.addWidget(self.end_date_frame)
        self.verticalLayout.addWidget(self.date_frame)
        self.footer_frame = QtWidgets.QFrame(self.main_frame)
        self.footer_frame.setStyleSheet("border:none ;\n"
"padding : 5px;")
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.delete_btn = QtWidgets.QPushButton(self.footer_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        self.delete_btn.setStyleSheet("*{\n"
"background-color: rgb(193, 0, 0);\n"
"border-radius : 5px;\n"
"}\n"
":hover{\n"
"background-color: rgb(135, 0, 0);\n"
"}")
        self.delete_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/garbage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon)
        self.delete_btn.setIconSize(QtCore.QSize(22, 22))
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_4.addWidget(self.delete_btn)
        self.text_label_2 = QtWidgets.QLabel(self.footer_frame)
        self.text_label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.text_label_2.setObjectName("text_label_2")
        self.horizontalLayout_4.addWidget(self.text_label_2)
        self.show_btn = QtWidgets.QPushButton(self.footer_frame)
        self.show_btn.setStyleSheet("*{\n"
"background-color: rgb(7, 26, 35);\n"
"border-radius : 5px;\n"
"}\n"
":hover{\n"
"background-color: rgb(21, 79, 106);\n"
"}")
        self.show_btn.setObjectName("show_btn")
        self.horizontalLayout_4.addWidget(self.show_btn)
        self.text_label_3 = QtWidgets.QLabel(self.footer_frame)
        self.text_label_3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.text_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_label_3.setObjectName("text_label_3")
        self.horizontalLayout_4.addWidget(self.text_label_3)
        self.resume_btn = QtWidgets.QPushButton(self.footer_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resume_btn.sizePolicy().hasHeightForWidth())
        self.resume_btn.setSizePolicy(sizePolicy)
        self.resume_btn.setStyleSheet("*{\n"
"background-color: rgb(33, 164, 62);\n"
"border-radius : 5px;\n"
"}\n"
":hover{\n"
"background-color: rgb(24, 120, 44);\n"
"}")
        self.resume_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/resume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resume_btn.setIcon(icon1)
        self.resume_btn.setIconSize(QtCore.QSize(23, 23))
        self.resume_btn.setObjectName("resume_btn")
        self.horizontalLayout_4.addWidget(self.resume_btn)
        self.verticalLayout.addWidget(self.footer_frame)
        self.horizontalLayout.addWidget(self.main_frame)

        self.retranslateUi(TaskWill)
        QtCore.QMetaObject.connectSlotsByName(TaskWill)

    def retranslateUi(self, TaskWill):
        _translate = QtCore.QCoreApplication.translate
        TaskWill.setWindowTitle(_translate("TaskWill", "Form"))
        self.taskname_label.setText(_translate("TaskWill", "TaskName"))
        self.last_day_result_label.setText(_translate("TaskWill", "1 GÜn İçinde"))
        self.text_label.setText(_translate("TaskWill", "Bitmesi Gerekiyor"))
        self.describe_label.setText(_translate("TaskWill", "Burada görev açıklaması yer almaktadır."))
        self.employee_label.setText(_translate("TaskWill", "employeeName"))
        self.date_title.setText(_translate("TaskWill", "Planlanan Başlangıç"))
        self.starting_date_label.setText(_translate("TaskWill", "startingDate"))
        self.date_title_2.setText(_translate("TaskWill", "Planlanan Bİtiş"))
        self.starting_date_label_2.setText(_translate("TaskWill", "startingDate"))
        self.text_label_2.setText(_translate("TaskWill", "Görevi\n"
"Sil"))
        self.show_btn.setText(_translate("TaskWill", "Şu an da işlem bekliyor. Detay görüntüle"))
        self.text_label_3.setText(_translate("TaskWill", "Göreve\n"
"Başla"))
import image_rc
