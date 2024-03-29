# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\ui_register.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 390)
        Dialog.setMinimumSize(QtCore.QSize(1000, 390))
        Dialog.setMaximumSize(QtCore.QSize(1000, 390))
        Dialog.setStyleSheet("*{\n"
"background-color: rgb(7, 26, 35);\n"
"color: rgb(255, 255, 255);\n"
"border : none ;\n"
"font: 11pt \"Montserrat\";\n"
"}")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 10, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.exit_btn = QtWidgets.QPushButton(self.frame_2)
        self.exit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Ellipse 5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout_3.addWidget(self.exit_btn, 0, QtCore.Qt.AlignRight)
        self.main_frame = QtWidgets.QFrame(self.frame_2)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.main_frame)
        self.frame.setMinimumSize(QtCore.QSize(100, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMaximumSize(QtCore.QSize(270, 90))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/image/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.logo_label.setWordWrap(False)
        self.logo_label.setIndent(-1)
        self.logo_label.setOpenExternalLinks(False)
        self.logo_label.setObjectName("logo_label")
        self.verticalLayout.addWidget(self.logo_label)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.login_open_btn = QtWidgets.QPushButton(self.frame)
        self.login_open_btn.setMinimumSize(QtCore.QSize(200, 35))
        self.login_open_btn.setMaximumSize(QtCore.QSize(15, 16777215))
        self.login_open_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(20, 66, 114);\n"
"border-radius : 5px ;\n"
"font: 600 12pt \"Montserrat\";\n"
"}\n"
":hover{\n"
"background-color: rgb(9, 33, 44);\n"
"}")
        self.login_open_btn.setObjectName("login_open_btn")
        self.verticalLayout.addWidget(self.login_open_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame)
        self.main_form_frame = QtWidgets.QFrame(self.main_frame)
        self.main_form_frame.setStyleSheet("QLineEdit{\n"
"border-radius : 5px;\n"
"background-color: rgb(20, 69, 93);\n"
"color:rgb(255, 255, 255);\n"
"padding:5px;\n"
"    font: 14pt \"Montserrat\";\n"
"}\n"
"QLabel{\n"
"font:45 14pt \"MS Shell Dlg 2\";\n"
"text-align: center;\n"
"}")
        self.main_form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_form_frame.setObjectName("main_form_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_form_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_frame = QtWidgets.QFrame(self.main_form_frame)
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.name_frame)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name_label = QtWidgets.QLabel(self.name_frame)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label, 0, QtCore.Qt.AlignHCenter)
        self.name_lineedit = QtWidgets.QLineEdit(self.name_frame)
        self.name_lineedit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.name_lineedit.setStyleSheet("")
        self.name_lineedit.setText("")
        self.name_lineedit.setObjectName("name_lineedit")
        self.horizontalLayout_2.addWidget(self.name_lineedit)
        self.verticalLayout_2.addWidget(self.name_frame)
        self.surname_frame = QtWidgets.QFrame(self.main_form_frame)
        self.surname_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surname_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.surname_frame.setObjectName("surname_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.surname_frame)
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.surname_label = QtWidgets.QLabel(self.surname_frame)
        self.surname_label.setObjectName("surname_label")
        self.horizontalLayout_3.addWidget(self.surname_label, 0, QtCore.Qt.AlignHCenter)
        self.surname_lineedit = QtWidgets.QLineEdit(self.surname_frame)
        self.surname_lineedit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.surname_lineedit.setText("")
        self.surname_lineedit.setObjectName("surname_lineedit")
        self.horizontalLayout_3.addWidget(self.surname_lineedit)
        self.verticalLayout_2.addWidget(self.surname_frame)
        self.eposta_frame = QtWidgets.QFrame(self.main_form_frame)
        self.eposta_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eposta_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eposta_frame.setObjectName("eposta_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.eposta_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.eposta_label = QtWidgets.QLabel(self.eposta_frame)
        self.eposta_label.setObjectName("eposta_label")
        self.horizontalLayout_5.addWidget(self.eposta_label, 0, QtCore.Qt.AlignHCenter)
        self.eposta_lineedit = QtWidgets.QLineEdit(self.eposta_frame)
        self.eposta_lineedit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.eposta_lineedit.setText("")
        self.eposta_lineedit.setObjectName("eposta_lineedit")
        self.horizontalLayout_5.addWidget(self.eposta_lineedit)
        self.verticalLayout_2.addWidget(self.eposta_frame)
        self.password_frame = QtWidgets.QFrame(self.main_form_frame)
        self.password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_frame.setObjectName("password_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.password_frame)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pasword_label = QtWidgets.QLabel(self.password_frame)
        self.pasword_label.setObjectName("pasword_label")
        self.horizontalLayout_4.addWidget(self.pasword_label, 0, QtCore.Qt.AlignHCenter)
        self.password_lineedit = QtWidgets.QLineEdit(self.password_frame)
        self.password_lineedit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.password_lineedit.setText("")
        self.password_lineedit.setObjectName("password_lineedit")
        self.horizontalLayout_4.addWidget(self.password_lineedit)
        self.verticalLayout_2.addWidget(self.password_frame)
        self.frame_3 = QtWidgets.QFrame(self.main_form_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.create_btn = QtWidgets.QPushButton(self.frame_3)
        self.create_btn.setMinimumSize(QtCore.QSize(200, 35))
        self.create_btn.setMaximumSize(QtCore.QSize(15, 16777215))
        self.create_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(33, 164, 62);\n"
"border-radius : 5px ;\n"
"font: 600 12pt \"Montserrat\";\n"
"}\n"
":hover{\n"
"background-color: rgb(25, 126, 47);\n"
"}")
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_6.addWidget(self.create_btn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.main_form_frame)
        self.verticalLayout_3.addWidget(self.main_frame)
        self.status_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setStyleSheet("color: rgb(158, 40, 40);")
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.verticalLayout_3.addWidget(self.status_label, 0, QtCore.Qt.AlignRight)
        self.designer_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.designer_label.sizePolicy().hasHeightForWidth())
        self.designer_label.setSizePolicy(sizePolicy)
        self.designer_label.setObjectName("designer_label")
        self.verticalLayout_3.addWidget(self.designer_label)
        self.horizontalLayout_10.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Bir hesabınız var ise\n"
"giriş yapın"))
        self.login_open_btn.setText(_translate("Dialog", "Giriş Yap"))
        self.name_label.setText(_translate("Dialog", "AD"))
        self.surname_label.setText(_translate("Dialog", "SOYAD"))
        self.eposta_label.setText(_translate("Dialog", "E-POSTA"))
        self.pasword_label.setText(_translate("Dialog", "ŞİFRE"))
        self.create_btn.setText(_translate("Dialog", "Hesap Oluştur"))
        self.designer_label.setText(_translate("Dialog", "                   Developed by FezaTech v1.0.0"))
import image_rc
