# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import  QToolTip
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(object):
    def setupUi(self, mainWindow):
    #def __init__(self):
        #super().__init__()
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(792, 573)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setStyleSheet("background-color:rgb(157, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.push_main_2 = QtWidgets.QPushButton(self.centralwidget)
        self.push_main_2.setStyleSheet("QPushButton{\n"
                                                        "    font: 75 36pt \"MS Shell Dlg 2\";\n"
                                                        "    \n"
                                                        "    color: rgb(0, 0, 0);\n"
                                                        "    background-color: rgb(255, 255, 112);\n"
                                                        "border-radius:20px\n"
                                                        "\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "color: rgb(85, 0, 255);\n"
                                                        "    \n"
                                                        "    ;\n"
                                                        "    background-color: rgb(255, 0, 0);\n"
                                                        "\n"
                                                        "}\n"
                                                        "QPushButton{\n"
                                                        "color: rgb(0, 0, 0);\n"
                                                        "    background-color: rgb(195, 188, 200);\n"
                                                        "\n"
                                                        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../qrc/download (2)..png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_main_2.setIcon(icon)
        self.push_main_2.setIconSize(QtCore.QSize(70, 50))
        self.push_main_2.setObjectName("push_main_2")
        self.push_main_2.setToolTip('<b>This buton used to  append in a database</b>')
        
        self.gridLayout.addWidget(self.push_main_2, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.push_main_1 = QtWidgets.QPushButton(self.centralwidget)
        self.push_main_1.setStyleSheet("QPushButton{\n"
                                                        "    font: 75 36pt \"MS Shell Dlg 2\";\n"
                                                        "    \n"
                                                        "    color: rgb(0, 0, 0);\n"
                                                        "    background-color: rgb(255, 255, 112);\n"
                                                        "border-radius:20px\n"
                                                        "\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "color: rgb(85, 0, 255);\n"
                                                        "    \n"
                                                        "    ;\n"
                                                        "    background-color: rgb(255, 0, 0);\n"
                                                        "\n"
                                                        "}\n"
                                                        "QPushButton{\n"
                                                        "color: rgb(0, 0, 0);\n"
                                                        "    background-color: rgb(195, 188, 200);\n"
                                                        "\n"
                                                        "}")
       
       
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../qrc/download (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_main_1.setIcon(icon1)
        self.push_main_1.setIconSize(QtCore.QSize(80, 50))
        self.push_main_1.setObjectName("push_main_1")
        self.push_main_1.setToolTip('<b>This  buton is used to  display the data in the dtabase</b>')
        
        self.verticalLayout.addWidget(self.push_main_1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.push_main_3 = QtWidgets.QPushButton(self.centralwidget)
        self.push_main_3.setStyleSheet("QPushButton{\n"
                                                        "    font: 75 36pt \"MS Shell Dlg 2\";\n"
                                                        "    \n"
                                                        "    color: rgb(0, 0, 0);\n"
                                                        "    background-color: rgb(255, 255, 112);\n"
                                                        "border-radius:20px\n"
                                                        "\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "color: rgb(85, 0, 255);\n"
                                                        "    \n"
                                                        "    ;\n"
                                                        "    background-color: rgb(255, 0, 0);\n"
                                                        "\n"
                                                        "}\n"
                                                        "QPushButton{\n"
                                                        "color: rgb(0, 0, 0);\n"
                                                        "    background-color: rgb(195, 188, 200);\n"
                                                        "\n"
                                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../qrc/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_main_3.setIcon(icon2)
        self.push_main_3.setIconSize(QtCore.QSize(70, 50))
        self.push_main_3.setObjectName("push_main_3")
        self.push_main_3.setToolTip('<b>This is buton used to  search in a dtabase</b>')
        
        self.gridLayout.addWidget(self.push_main_3, 0, 2, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "fossee-osdag"))
        self.push_main_2.setText(_translate("mainWindow", "Append"))
        self.push_main_1.setText(_translate("mainWindow", "Display"))
        self.push_main_3.setText(_translate("mainWindow", "Search"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     mainWindow = QtWidgets.QMainWindow()
#     ui = Ui_mainWindow()
#     #ui.setupUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())

