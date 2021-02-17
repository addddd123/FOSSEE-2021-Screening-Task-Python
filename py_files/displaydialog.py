# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'disp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 290)
        Dialog.setAccessibleName("")
        Dialog.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 255, 255);")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 150, 441, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 4, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 431, 81))
        self.label.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(35, 0, 107);")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        var="mmmmmmmmm"
        Dialog.setWindowTitle(_translate("Dialog", var))
        self.radioButton_3.setText(_translate("Dialog", "Beams"))
        self.radioButton_2.setText(_translate("Dialog", "Channels"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.radioButton.setText(_translate("Dialog", "Angles"))
        self.label.setText(_translate("Dialog", "            Select a Table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

