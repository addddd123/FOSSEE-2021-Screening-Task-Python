from PyQt5.QtWidgets import QApplication,QWidget ,QDialog ,  QMainWindow ,QLabel, QPushButton ,QVBoxLayout ,QHBoxLayout ,QGridLayout ,QGroupBox,QRadioButton
import sys
from PyQt5.QtGui import QIcon , QFont 
from PyQt5.QtCore import QSize
import view
class control():
    def __init__(self):
        self._app = QApplication(sys.argv)
        self._view = view.window()
    def run(self):
        self._view.show()
        return self._app.exec_()

    
if __name__=="__main__":
    obj=control()
    obj.run()