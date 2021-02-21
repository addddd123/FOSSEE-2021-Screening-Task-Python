
import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import view
#from view import *

#from model import Model
#from main import Window


class Controller:
    
    
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui =view.Ui_mainWindow()
        ui.setupUi(mainWindow)
    
        mainWindow.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    c = Controller()
    






