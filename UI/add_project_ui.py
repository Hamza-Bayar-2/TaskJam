# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\ui_add_project.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_project_add(object):
    def setupUi(self, project_add):
        project_add.setObjectName("project_add")
        project_add.resize(1000, 450)
        project_add.setMinimumSize(QtCore.QSize(1000, 450))
        project_add.setMaximumSize(QtCore.QSize(1000, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        project_add.setWindowIcon(icon)
        project_add.setStyleSheet("*{\n"
"background-color: rgb(25, 27, 42);\n"
"color: rgb(255, 255, 255);\n"
"border : none;\n"
"font: 100 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"width: 20px;\n"
"height: 30px;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"#main_frame{\n"
" border-style: solid;\n"
"border-radius :10px;\n"
"  border-width: 5px;\n"
"    border-color: rgb(168, 168, 168);\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(project_add)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(project_add)
        self.main_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_8.setContentsMargins(2, -1, -1, 27)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.header_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_label = QtWidgets.QLabel(self.header_frame)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.exit_btn = QtWidgets.QPushButton(self.header_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/Ellipse 5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon1)
        self.exit_btn.setIconSize(QtCore.QSize(16, 16))
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout.addWidget(self.exit_btn)
        self.verticalLayout_8.addWidget(self.header_frame)
        self.form_frame = QtWidgets.QFrame(self.main_frame)
        self.form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame.setObjectName("form_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.form_frame)
        self.horizontalLayout_3.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labels_frame = QtWidgets.QFrame(self.form_frame)
        self.labels_frame.setMinimumSize(QtCore.QSize(300, 0))
        self.labels_frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.labels_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labels_frame.setObjectName("labels_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.labels_frame)
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_2.setSpacing(55)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.project_name_label = QtWidgets.QLabel(self.labels_frame)
        self.project_name_label.setObjectName("project_name_label")
        self.verticalLayout_2.addWidget(self.project_name_label, 0, QtCore.Qt.AlignHCenter)
        self.project_describe_label = QtWidgets.QLabel(self.labels_frame)
        self.project_describe_label.setObjectName("project_describe_label")
        self.verticalLayout_2.addWidget(self.project_describe_label, 0, QtCore.Qt.AlignHCenter)
        self.start_day_label = QtWidgets.QLabel(self.labels_frame)
        self.start_day_label.setObjectName("start_day_label")
        self.verticalLayout_2.addWidget(self.start_day_label, 0, QtCore.Qt.AlignHCenter)
        self.finish_day_label = QtWidgets.QLabel(self.labels_frame)
        self.finish_day_label.setObjectName("finish_day_label")
        self.verticalLayout_2.addWidget(self.finish_day_label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.labels_frame, 0, QtCore.Qt.AlignTop)
        self.lineedits_frame = QtWidgets.QFrame(self.form_frame)
        self.lineedits_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lineedits_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lineedits_frame.setObjectName("lineedits_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lineedits_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 40, 0)
        self.verticalLayout_3.setSpacing(42)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.project_name_lineedit = QtWidgets.QLineEdit(self.lineedits_frame)
        self.project_name_lineedit.setMaximumSize(QtCore.QSize(215, 16777215))
        self.project_name_lineedit.setObjectName("project_name_lineedit")
        self.verticalLayout_3.addWidget(self.project_name_lineedit)
        self.project_describe_lineedit = QtWidgets.QLineEdit(self.lineedits_frame)
        self.project_describe_lineedit.setText("")
        self.project_describe_lineedit.setObjectName("project_describe_lineedit")
        self.verticalLayout_3.addWidget(self.project_describe_lineedit)
        self.frame_2 = QtWidgets.QFrame(self.lineedits_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(30)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.start_day_lineedit = QtWidgets.QLineEdit(self.frame_2)
        self.start_day_lineedit.setMaximumSize(QtCore.QSize(215, 16777215))
        self.start_day_lineedit.setObjectName("start_day_lineedit")
        self.horizontalLayout_14.addWidget(self.start_day_lineedit)
        self.format_2_label = QtWidgets.QLabel(self.frame_2)
        self.format_2_label.setObjectName("format_2_label")
        self.horizontalLayout_14.addWidget(self.format_2_label)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.lineedits_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(30)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.finish_day_lineedit = QtWidgets.QLineEdit(self.frame)
        self.finish_day_lineedit.setMaximumSize(QtCore.QSize(215, 16777215))
        self.finish_day_lineedit.setObjectName("finish_day_lineedit")
        self.horizontalLayout_13.addWidget(self.finish_day_lineedit)
        self.format1_label = QtWidgets.QLabel(self.frame)
        self.format1_label.setObjectName("format1_label")
        self.horizontalLayout_13.addWidget(self.format1_label)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_3.addWidget(self.lineedits_frame)
        self.verticalLayout_8.addWidget(self.form_frame)
        self.add_btn_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn_frame.sizePolicy().hasHeightForWidth())
        self.add_btn_frame.setSizePolicy(sizePolicy)
        self.add_btn_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.add_btn_frame.setStyleSheet("")
        self.add_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_btn_frame.setObjectName("add_btn_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.add_btn_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_add_btn = QtWidgets.QPushButton(self.add_btn_frame)
        self.project_add_btn.setMinimumSize(QtCore.QSize(220, 30))
        self.project_add_btn.setMaximumSize(QtCore.QSize(220, 30))
        self.project_add_btn.setStyleSheet("background-color: rgb(33, 164, 62);\n"
"border-radius : 10px ;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.project_add_btn.setObjectName("project_add_btn")
        self.horizontalLayout_2.addWidget(self.project_add_btn)
        self.verticalLayout_8.addWidget(self.add_btn_frame)
        self.status_label = QtWidgets.QLabel(self.main_frame)
        self.status_label.setStyleSheet("color: rgb(244, 61, 61);")
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.verticalLayout_8.addWidget(self.status_label, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.main_frame)

        self.retranslateUi(project_add)
        QtCore.QMetaObject.connectSlotsByName(project_add)

    def retranslateUi(self, project_add):
        _translate = QtCore.QCoreApplication.translate
        project_add.setWindowTitle(_translate("project_add", "Dialog"))
        self.title_label.setText(_translate("project_add", "YENi PROJE EKLE"))
        self.project_name_label.setText(_translate("project_add", "Proje Adı"))
        self.project_describe_label.setText(_translate("project_add", "Proje Açıklaması "))
        self.start_day_label.setText(_translate("project_add", "Başlangıç Tarihi"))
        self.finish_day_label.setText(_translate("project_add", "Bitiş Tarihi"))
        self.format_2_label.setText(_translate("project_add", "format : (gg.aa.yyyy)"))
        self.format1_label.setText(_translate("project_add", "format : (gg.aa.yyyy)"))
        self.project_add_btn.setText(_translate("project_add", "Ekle"))
import image_rc