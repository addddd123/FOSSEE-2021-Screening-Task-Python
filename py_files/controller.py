
import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

from main import *

#from model import Model
#from main import Window


class Controller:
    
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui = Ui_mainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    c = Controller()
    sys.exit(c.run())







