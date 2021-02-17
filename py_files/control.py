
import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

import main

#from model import Model
#from main import Window


class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        #self._model = Model()
        #self._main = main.Window()


    def run(self):
        self.main.show()

        return self._app.exec_()


if __name__ == '__main__':
    c = Controller()
    sys.exit(c.run())







