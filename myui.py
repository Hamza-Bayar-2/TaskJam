# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 733)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.app_bar_frame = QtWidgets.QFrame(self.centralwidget)
        self.app_bar_frame.setEnabled(True)
        self.app_bar_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.app_bar_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.app_bar_frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.app_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_bar_frame.setLineWidth(0)
        self.app_bar_frame.setObjectName("app_bar_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.app_bar_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.date_label = QtWidgets.QLabel(self.app_bar_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 0, 4);\n"
"}")
        self.date_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout_3.addWidget(self.date_label)
        self.app_name_label = QtWidgets.QLabel(self.app_bar_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.app_name_label.setFont(font)
        self.app_name_label.setStyleSheet("")
        self.app_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.app_name_label.setObjectName("app_name_label")
        self.horizontalLayout_3.addWidget(self.app_name_label)
        self.window_edit_frame = QtWidgets.QFrame(self.app_bar_frame)
        self.window_edit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window_edit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_edit_frame.setObjectName("window_edit_frame")
        self.horizontalLayout_3.addWidget(self.window_edit_frame)
        self.verticalLayout.addWidget(self.app_bar_frame)
        self.main_bar_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_bar_frame.setLineWidth(2)
        self.main_bar_frame.setObjectName("main_bar_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_bar_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_bar_frame = QtWidgets.QFrame(self.main_bar_frame)
        self.menu_bar_frame.setMinimumSize(QtCore.QSize(250, 0))
        self.menu_bar_frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.menu_bar_frame.setStyleSheet("background-color: rgb(35, 39, 79);")
        self.menu_bar_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_bar_frame.setObjectName("menu_bar_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_bar_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.avatar_box_widget = QtWidgets.QWidget(self.menu_bar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avatar_box_widget.sizePolicy().hasHeightForWidth())
        self.avatar_box_widget.setSizePolicy(sizePolicy)
        self.avatar_box_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.avatar_box_widget.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.avatar_box_widget.setFont(font)
        self.avatar_box_widget.setObjectName("avatar_box_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.avatar_box_widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.avatar_box_widget)
        self.label_4.setMinimumSize(QtCore.QSize(150, 100))
        self.label_4.setMaximumSize(QtCore.QSize(150, 150))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/image/profile-icon-9.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.avatar_box_widget, 0, QtCore.Qt.AlignTop)
        self.avatar_name = QtWidgets.QLabel(self.menu_bar_frame)
        self.avatar_name.setMinimumSize(QtCore.QSize(0, 20))
        self.avatar_name.setMaximumSize(QtCore.QSize(16777215, 20))
        self.avatar_name.setObjectName("avatar_name")
        self.verticalLayout_2.addWidget(self.avatar_name, 0, QtCore.Qt.AlignHCenter)
        self.main_page_btn = QtWidgets.QFrame(self.menu_bar_frame)
        self.main_page_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.main_page_btn.setMaximumSize(QtCore.QSize(16777215, 45))
        self.main_page_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 0), stop:1 rgba(0, 0 255, 0), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 0));")
        self.main_page_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_page_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_page_btn.setObjectName("main_page_btn")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_page_btn)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.main_page_btn)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.main_page_btn)
        self.profile_page_btn = QtWidgets.QFrame(self.menu_bar_frame)
        self.profile_page_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.profile_page_btn.setMaximumSize(QtCore.QSize(16777215, 45))
        self.profile_page_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 0), stop:1 rgba(0, 0 255, 0), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 0));")
        self.profile_page_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_page_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_page_btn.setObjectName("profile_page_btn")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.profile_page_btn)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.profile_page_btn)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.profile_page_btn, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.footer_label = QtWidgets.QLabel(self.menu_bar_frame)
        self.footer_label.setMinimumSize(QtCore.QSize(0, 20))
        self.footer_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.footer_label.setObjectName("footer_label")
        self.verticalLayout_2.addWidget(self.footer_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.menu_bar_frame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_bar_frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.home_page)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_body_frame_ = QtWidgets.QFrame(self.home_page)
        self.main_body_frame_.setStyleSheet("background-color: rgb(25, 27, 43);")
        self.main_body_frame_.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_frame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_frame_.setObjectName("main_body_frame_")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.main_body_frame_)
        self.verticalLayout_9.setContentsMargins(12, 12, 15, 15)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.main_top_bar_frame = QtWidgets.QFrame(self.main_body_frame_)
        self.main_top_bar_frame.setMinimumSize(QtCore.QSize(0, 200))
        self.main_top_bar_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.main_top_bar_frame.setStyleSheet("background-color: rgb(10, 10, 10);\n"
"border-radius: 16px;")
        self.main_top_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_top_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_top_bar_frame.setObjectName("main_top_bar_frame")
        self.verticalLayout_9.addWidget(self.main_top_bar_frame)
        self.main_bottom_bar_frame = QtWidgets.QFrame(self.main_body_frame_)
        self.main_bottom_bar_frame.setStyleSheet("background-color: rgb(10, 10, 10);\n"
"border-radius: 16px;")
        self.main_bottom_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_bottom_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_bottom_bar_frame.setObjectName("main_bottom_bar_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.main_bottom_bar_frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.main_bottom_bar_TO_frame = QtWidgets.QFrame(self.main_bottom_bar_frame)
        self.main_bottom_bar_TO_frame.setMinimumSize(QtCore.QSize(700, 0))
        self.main_bottom_bar_TO_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.main_bottom_bar_TO_frame.setFont(font)
        self.main_bottom_bar_TO_frame.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.main_bottom_bar_TO_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_bottom_bar_TO_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_bottom_bar_TO_frame.setObjectName("main_bottom_bar_TO_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.main_bottom_bar_TO_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.waiting_label = QtWidgets.QLabel(self.main_bottom_bar_TO_frame)
        self.waiting_label.setObjectName("waiting_label")
        self.horizontalLayout_7.addWidget(self.waiting_label, 0, QtCore.Qt.AlignHCenter)
        self.working_label = QtWidgets.QLabel(self.main_bottom_bar_TO_frame)
        self.working_label.setObjectName("working_label")
        self.horizontalLayout_7.addWidget(self.working_label, 0, QtCore.Qt.AlignHCenter)
        self.done_label = QtWidgets.QLabel(self.main_bottom_bar_TO_frame)
        self.done_label.setObjectName("done_label")
        self.horizontalLayout_7.addWidget(self.done_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.main_bottom_bar_TO_frame)
        self.main_bottom_bar_botttom_frame = QtWidgets.QFrame(self.main_bottom_bar_frame)
        self.main_bottom_bar_botttom_frame.setStyleSheet("\n"
"")
        self.main_bottom_bar_botttom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_bottom_bar_botttom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_bottom_bar_botttom_frame.setObjectName("main_bottom_bar_botttom_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.main_bottom_bar_botttom_frame)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.waiting_frame = QtWidgets.QFrame(self.main_bottom_bar_botttom_frame)
        self.waiting_frame.setStyleSheet("background-color: rgb(25, 27, 42);\n"
"borderRadius : 12px;")
        self.waiting_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.waiting_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.waiting_frame.setObjectName("waiting_frame")
        self.horizontalLayout_6.addWidget(self.waiting_frame)
        self.working_frame = QtWidgets.QFrame(self.main_bottom_bar_botttom_frame)
        self.working_frame.setStyleSheet("background-color: rgb(25, 27, 42);\n"
"borderRadius : 12px;")
        self.working_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.working_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.working_frame.setObjectName("working_frame")
        self.horizontalLayout_6.addWidget(self.working_frame)
        self.done_frame = QtWidgets.QFrame(self.main_bottom_bar_botttom_frame)
        self.done_frame.setStyleSheet("background-color: rgb(25, 27, 42);\n"
"borderRadius : 12px;")
        self.done_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.done_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.done_frame.setObjectName("done_frame")
        self.horizontalLayout_6.addWidget(self.done_frame)
        self.verticalLayout_10.addWidget(self.main_bottom_bar_botttom_frame)
        self.verticalLayout_9.addWidget(self.main_bottom_bar_frame)
        self.horizontalLayout_2.addWidget(self.main_body_frame_)
        self.stackedWidget.addWidget(self.home_page)
        self.profile_page = QtWidgets.QWidget()
        self.profile_page.setObjectName("profile_page")
        self.stackedWidget.addWidget(self.profile_page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.main_bar_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.date_label.setText(_translate("MainWindow", "09.01.2024"))
        self.app_name_label.setText(_translate("MainWindow", "TaskJam"))
        self.avatar_name.setText(_translate("MainWindow", "Avata_Name"))
        self.label_2.setText(_translate("MainWindow", "           Ana Sayfa"))
        self.label_3.setText(_translate("MainWindow", "             Profilim"))
        self.footer_label.setText(_translate("MainWindow", "Desing by Fezaitech v1.0.0"))
        self.waiting_label.setText(_translate("MainWindow", "TAMAMLANACAK"))
        self.working_label.setText(_translate("MainWindow", "TAMAMLANIYOR"))
        self.done_label.setText(_translate("MainWindow", "TAMAMLANIYOR"))
import image_rc
