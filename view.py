from PyQt5.QtWidgets import QApplication,QWidget ,QDialog , QTableWidget, QTableWidgetItem, QMainWindow ,QLabel, QPushButton ,QVBoxLayout ,QHBoxLayout ,QGridLayout ,QGroupBox,QRadioButton
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon , QFont 
from PyQt5.QtCore import QSize , Qt
import sqlite3
import os # used to check if db_exists in path
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
        
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)
        self.show()
    def create_button(self):
        self.groupbox=QGroupBox("Welcome to fossee steel design Gui",alignment=Qt.AlignHCenter)
        
        self.groupbox.setStyleSheet("color:green ; font-size:25px;")
        self.groupbox.setFont(QFont("sanserif",15))
        hbox=QHBoxLayout()
        self.btn1=QPushButton("Display")
        self.btn1.clicked.connect(lambda:self.on_pressed("display"))
        self.btn1.setIcon(QIcon("download.png"))
        self.btn1.setStyleSheet("background-color:blue; color:black")
        hbox.addWidget(self.btn1)
        self.btn2=QPushButton("append")
        self.btn2.clicked.connect(lambda:self.on_pressed("append"))
        self.btn2.setIcon(QIcon("download.png")) 
        self.btn2.setStyleSheet("background-color:blue;color:black")
        
        hbox.addWidget(self.btn2)
        self.groupbox.setLayout(hbox)
        
######################## main windows button functions and genration of############################
# ##############another dialog which get radio inputs to select paticualr fxn################################
    def on_pressed(self,obj_btn_get):
        ######### passing argument above in order two which window which button pressed############
        
        dialog_box1 = QDialog()
        dialog_box1.setWindowTitle("Search")
        #label_btn_selected=QLabel("")
        dialog_box1.resize(170, 170)
        
        h_box1 = QHBoxLayout()
        #h_box1.addStretch()
        self.channels_rad = QRadioButton("Channels")
        self.channels_rad.setStyleSheet("background-color:powderblue; color:black")
        self.beams_rad = QRadioButton("Beams")
        self.beams_rad.setStyleSheet("background-color:powderblue; color:black")
        self.angles_rad = QRadioButton("Angles")
        self.angles_rad.setStyleSheet("background-color:powderblue; color:black")
        self.label1 = QLabel("Select A Table")
        self.label1.setStyleSheet("color:green ; font-size:25px;")
        h_box1.addWidget(self.channels_rad)

        h_box1.addWidget(self.beams_rad)
        h_box1.addWidget(self.angles_rad)
        h_box1.addStretch()
        v_box1 = QVBoxLayout()
        v_box1.addWidget(self.label1, alignment=Qt.AlignHCenter)
        v_box1.addLayout(h_box1)
        self.label2=QLabel(obj_btn_get+" mode selected in main")
        v_box1.addWidget(self.label2)
        self.channels_rad.toggled.connect(lambda: self.btn_state(self.channels_rad,obj_btn_get))
        self.beams_rad.toggled.connect(lambda: self.btn_state(self.beams_rad,obj_btn_get))
        self.angles_rad.toggled.connect(lambda: self.btn_state(self.channels_rad,obj_btn_get))
        
        dialog_box1.setLayout(v_box1)
        dialog_box1.setStyleSheet("font-size:14px;"
                                  "color: black;"
                                  "background-color: white;"
                                  "font: SanSerif; "
                                  )
        dialog_box1.setWindowIcon(QtGui.QIcon("abc.png"))

        dialog_box1.exec_()
        
        ###############radio button functions of second windows #################
    def btn_state(self,radio_state_dialog,btn_state_main):
        conn = sqlite3.connect('steel_sections.sqlite')
        db_exists=os.path.exists('steel_sections.sqlite')
        print("db_exists->",db_exists)
        if not db_exists:
            dg=QDialog()
            dg.setWindowTitle("warning message")
            dg.resize(170, 170)
            label__warn=QLabel("!!!!!no database in path")
            dg.setStyleSheet("font-size:32px;"
                                  "color: red;"
                                  "background-color: white;"
                                  "font: SanSerif; "
                                  )
            
            dg.setLayout(QVBoxLayout())
            dg.layout().addWidget(label__warn)
            dg.exec_()
        else:
            cursor = conn.cursor()
            rowcount2 = cursor.execute('''SELECT COUNT(*) FROM Beams''').fetchone()[0]
            tblTable = QTableWidget()

            tableItem = QTableWidgetItem()
            tblTable.setWindowTitle("Details")
            tblTable.setRowCount(rowcount2)
            tblTable.setColumnCount(20)
            tblTable.setHorizontalHeaderLabels(
                    ['Id', 'Designation', 'Mass', 'Area', 'D', 'B', 'tw', 'T', 'FlangeSlope', 'R1', 'R2', 'Iz', 'Iy',
                     'rz', 'ry', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source'])

            cursor.execute('''SELECT * FROM Beams''')

            for row, form in enumerate(cursor):
                for column, item in enumerate(form):
                    tblTable.setItem(row, column, QTableWidgetItem(str(item)))
            tblTable.horizontalHeader().setStretchLastSection(True)
            tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            tblTable.show()
            dialog = QDialog()
            dialog.setWindowTitle("Data of Beams Section")
            dialog.resize(600, 400)
            dialog.setLayout(QVBoxLayout())
            dialog.layout().addWidget(tblTable)
            dialog.setStyleSheet("font-size:14px;"
                                          "color: black;"
                                          "background-color: #A9A9A9;"
                                          "font: SanSerif; "
                                          )
            dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
            dialog.exec()
        #print(btn_state_main,radio_state_dialog.text()) #rwo args to know which bu
        if radio_state_dialog.text()=="Channels" and btn_state_main=="display":
            print("happpy")
            
          
        
        
        
        
        
        
        
app=QApplication(sys.argv)
window=window()
sys.exit(app.exec_())