# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    border : none;\n"
"    color : #ffffff;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #040f13;\n"
"}\n"
"QPushButton{\n"
"    padding : 8px;\n"
"    background-color: #040f13;\n"
"    border-radius: 5px;\n"
"}\n"
"#slide_menu{\n"
"    border-radius : 10px;\n"
"    background-color: #071e26;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Header = QtWidgets.QFrame(self.centralwidget)
        self.Header.setMinimumSize(QtCore.QSize(0, 40))
        self.Header.setMaximumSize(QtCore.QSize(16777215, 55))
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Menu = QtWidgets.QFrame(self.Header)
        self.Menu.setMinimumSize(QtCore.QSize(30, 40))
        self.Menu.setStyleSheet("background-color: #ffff;")
        self.Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu.setObjectName("Menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Menu)
        self.horizontalLayout_4.setContentsMargins(10, 10, 0, 5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.Menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(20, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/feather (1)/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.Menu, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Title = QtWidgets.QFrame(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("")
        self.Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title.setObjectName("Title")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Title)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.Title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.Title)
        self.verticalLayout_2.addWidget(self.Header)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slide_menu = QtWidgets.QFrame(self.frame_2)
        self.slide_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.slide_menu)
        self.frame_5.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setContentsMargins(9, 10, 9, 9)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.photoButton = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.photoButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/feather (1)/camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photoButton.setIcon(icon1)
        self.photoButton.setIconSize(QtCore.QSize(25, 25))
        self.photoButton.setObjectName("photoButton")
        self.verticalLayout.addWidget(self.photoButton)
        self.recordButton = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recordButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/feather (1)/video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordButton.setIcon(icon2)
        self.recordButton.setIconSize(QtCore.QSize(25, 25))
        self.recordButton.setObjectName("recordButton")
        self.verticalLayout.addWidget(self.recordButton)
        self.controlButton = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.controlButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/feather (1)/move.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.controlButton.setIcon(icon3)
        self.controlButton.setIconSize(QtCore.QSize(25, 25))
        self.controlButton.setObjectName("controlButton")
        self.verticalLayout.addWidget(self.controlButton)
        self.zoomInButton = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zoomInButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/feather (1)/zoom-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomInButton.setIcon(icon4)
        self.zoomInButton.setIconSize(QtCore.QSize(25, 25))
        self.zoomInButton.setObjectName("zoomInButton")
        self.verticalLayout.addWidget(self.zoomInButton)
        self.zoomOutButton = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zoomOutButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/feather (1)/zoom-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomOutButton.setIcon(icon5)
        self.zoomOutButton.setIconSize(QtCore.QSize(25, 25))
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.verticalLayout.addWidget(self.zoomOutButton)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zoomX = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomX.sizePolicy().hasHeightForWidth())
        self.zoomX.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zoomX.setFont(font)
        self.zoomX.setObjectName("zoomX")
        self.horizontalLayout_3.addWidget(self.zoomX)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setMinimumSize(QtCore.QSize(30, 40))
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(30, 40))
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(119, 118, 123);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_3.addWidget(self.plainTextEdit_2)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame = QtWidgets.QFrame(self.slide_menu)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/feather (1)/refresh-cw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.settingButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.settingButton.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/feather (1)/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingButton.setIcon(icon7)
        self.settingButton.setIconSize(QtCore.QSize(25, 25))
        self.settingButton.setObjectName("settingButton")
        self.verticalLayout_4.addWidget(self.settingButton)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.slide_menu)
        self.body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setStyleSheet("background-color: #071e26;\n"
"border-radius : 10px;")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.body)
        self.label_2.setStyleSheet("border-radius: 10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.body)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_6.setStyleSheet("background-color: #071e26;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_6)
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_7.addWidget(self.plainTextEdit)
        self.verticalLayout_2.addWidget(self.frame_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera"))
        self.pushButton.setText(_translate("MainWindow", "MENU"))
        self.label.setText(_translate("MainWindow", "CAMERA ZR10 SIYI"))
        self.photoButton.setText(_translate("MainWindow", " PHOTO"))
        self.recordButton.setText(_translate("MainWindow", " RECORD"))
        self.controlButton.setText(_translate("MainWindow", " CONTROL"))
        self.zoomInButton.setText(_translate("MainWindow", " ZOOM +"))
        self.zoomOutButton.setText(_translate("MainWindow", "ZOOM -"))
        self.zoomX.setText(_translate("MainWindow", "ZOOM x"))
        self.pushButton_7.setText(_translate("MainWindow", " REFRESH"))
        self.settingButton.setText(_translate("MainWindow", " SETTING"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
