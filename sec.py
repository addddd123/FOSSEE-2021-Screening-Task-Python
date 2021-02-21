from PyQt5.QtWidgets import QApplication,QWidget ,QDialog ,  QMainWindow ,QLabel, QPushButton ,QVBoxLayout ,QHBoxLayout ,QGridLayout ,QGroupBox,QRadioButton
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon , QFont 
from PyQt5.QtCore import QSize , Qt


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(80,100,400,400)
        self.setWindowTitle(" Fossee simple app")
        
        self.setWindowIcon(QIcon('pexels-pixabay-46167.jpg'))
        self.setWindowOpacity(1)
        self.setStyleSheet("background-color:white ")
        self.create_button()
        # self.setLayout(grid)
        vbox=QVBoxLayout()
        grid=QGridLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)
        self.show()
    def create_button(self):
        self.groupbox=QGroupBox("Welcome to fossee steel design Gui",alignment=Qt.AlignHCenter)
        
        self.groupbox.setStyleSheet("color:green ; font-size:25px;")
        self.groupbox.setFont(QFont("sanserif",15))
        hbox=QHBoxLayout()
        self.btn1=QPushButton("Display")
        self.btn1.clicked.connect(self.on_pressed)
        self.btn1.setIcon(QIcon("download.png"))
        self.btn1.setStyleSheet("background-color:blue; color:black")
        hbox.addWidget(self.btn1)
        self.btn2=QPushButton("append")
        self.btn2.clicked.connect(self.on_pressed)
        self.btn2.setIcon(QIcon("download.png")) 
        self.btn2.setStyleSheet("background-color:blue;color:black")
        
        hbox.addWidget(self.btn2)
        self.groupbox.setLayout(hbox)
        
########################################################
    def on_pressed(self):
        
        dialog_box1 = QDialog()
        dialog_box1.setWindowTitle("Search")
        dialog_box1.resize(170, 170)
        h_box1 = QHBoxLayout()
        #h_box1.addStretch()
        self.channels_rad = QRadioButton("Channels")
        self.channels_rad.setStyleSheet("background-color:powderblue; color:black")
        self.channels_beams = QRadioButton("Beams")
        self.channels_beams.setStyleSheet("background-color:powderblue; color:black")
        self.channels_angles = QRadioButton("Angles")
        self.channels_angles.setStyleSheet("background-color:powderblue; color:black")
        self.label1 = QLabel("Select A Table")
        self.label1.setStyleSheet("color:green ; font-size:25px;")
        h_box1.addWidget(self.channels_rad)

        h_box1.addWidget(self.channels_beams)
        h_box1.addWidget(self.channels_angles)
        h_box1.addStretch()
        v_box1 = QVBoxLayout()
        v_box1.addWidget(self.label1, alignment=Qt.AlignHCenter)
        v_box1.addLayout(h_box1)
        self.label2=QLabel("")
        v_box1.addWidget(self.label2)
        # self.channels_rad.toggled.connect(lambda: self.btnstate2(self.channels_rad))
        # self.channels_beams.toggled.connect(lambda: self.btnstate2(self.channels_beams))
        # self.channels_angles.toggled.connect(lambda: self.btnstate2(self.channels_angles))

        dialog_box1.setLayout(v_box1)
        dialog_box1.setStyleSheet("font-size:14px;"
                                  "color: black;"
                                  "background-color: white;"
                                  "font: SanSerif; "
                                  )
        dialog_box1.setWindowIcon(QtGui.QIcon("abc.png"))

        dialog_box1.exec_()
        
        
        
        
        
        
        
        
        
        
        
app=QApplication(sys.argv)
window=window()
sys.exit(app.exec_())