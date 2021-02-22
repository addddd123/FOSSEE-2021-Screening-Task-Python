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
        #######creating buttons on main window##########below fxn for that#######
    def create_button(self):
        self.groupbox=QGroupBox("Welcome to fossee steel design Gui",alignment=Qt.AlignHCenter)
        
        self.groupbox.setStyleSheet("color:green ; font-size:25px;")
        self.groupbox.setFont(QFont("sanserif",15))
        hbox=QHBoxLayout()
        self.btn1=QPushButton("Display")
        self.btn1.clicked.connect(lambda:self.on_pressed("display"))
        self.btn1.setIcon(QIcon("display.png"))
        self.btn1.setIconSize(QSize(33, 30))
        self.btn1.setStyleSheet("background-color:blue; color:black")
        hbox.addWidget(self.btn1)
        self.btn2=QPushButton("append")
        self.btn2.clicked.connect(lambda:self.on_pressed("append"))
        self.btn2.setIcon(QIcon("append.png")) 
        self.btn2.setIconSize(QSize(33, 30))
        # self.btn2.QSize(10, 10) 
        self.btn2.setStyleSheet("background-color:blue;color:black")
        
        hbox.addWidget(self.btn2)
        self.groupbox.setLayout(hbox)
        
######################## main windows button functions and genration of############################
# ##############another dialog which get radio inputs to select paticualr fxn################################
    def on_pressed(self,obj_btn_get):
        ######### passing argument above in order two which window which button pressed############
        print(obj_btn_get)
        dialog_box1 = QDialog()
        dialog_box1.setWindowTitle(obj_btn_get+ " menu")
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
        self.label2=QLabel("you have selected <b>"+obj_btn_get+"</b>")
        self.label2.setStyleSheet("background-color:white; color:blue; font-size:17px;")
        v_box1.addWidget(self.label2)
        self.channels_rad.toggled.connect(lambda: self.btn_state(self.channels_rad,obj_btn_get))
        self.beams_rad.toggled.connect(lambda: self.btn_state(self.beams_rad,obj_btn_get))
        self.angles_rad.toggled.connect(lambda: self.btn_state(self.angles_rad,obj_btn_get))
        
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
        if btn_state_main=="display":
            print(radio_state_dialog.text())
            db_exists=not os.path.exists('steel_sections.sqlite')
            print("db_exists->",db_exists)
            if db_exists==True:
                
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
                conn = sqlite3.connect('steel_sections.sqlite')
                cursor = conn.cursor()
                if radio_state_dialog.text()=="Beams" and radio_state_dialog.isChecked() == True:
                    rowcount2 = cursor.execute('''SELECT COUNT(*) FROM Beams''').fetchone()[0]
                    table_attributes=['Id', 'Designation', 'Mass', 'Area', 'D', 'B', 'tw', 'T', 'FlangeSlope', 'R1', 'R2', 'Iz', 'Iy',
                        'rz', 'ry', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source']
                    
                    tblTable = QTableWidget()

                    tableItem = QTableWidgetItem()
                    tblTable.setWindowTitle("Details")
                    tblTable.setRowCount(rowcount2)
                    tblTable.setColumnCount(20)
                    tblTable.setHorizontalHeaderLabels(table_attributes)
                    ##########below loop changes color of of table headers ##############
                    for i in range(0,21):
                        if i%2==0:
                            item1 = QtWidgets.QTableWidgetItem('green')
                            item1.setBackground(QtGui.QColor( 0,255, 0))
                            tblTable.setHorizontalHeaderItem(i,item1)
                        else:
                            item1 = QtWidgets.QTableWidgetItem('blue')
                            item1.setBackground(QtGui.QColor( 255,0, 0))
                            tblTable.setHorizontalHeaderItem(i,item1)

                    cursor.execute('''SELECT * FROM Beams''')

                    for row1, form1 in enumerate(cursor):
                        for column1, item1 in enumerate(form1):
                            tblTable.setItem(row1, column1, QTableWidgetItem(str(item1)))
                    tblTable.horizontalHeader().setStretchLastSection(True)
                    tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                    tblTable.show()
                    dialog = QDialog()
                    dialog.setWindowTitle("Data of "+radio_state_dialog.text()+" Section")
                    dialog.resize(600, 400)
                    dialog.setLayout(QVBoxLayout())
                    dialog.layout().addWidget(tblTable)
                    dialog.setStyleSheet("font-size:14px;"
                                                "color: black;"
                                                "background-color: white;"
                                                "font: SanSerif; "
                                                )
                    dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
                    dialog.exec_()
            
                elif radio_state_dialog.text()=="Channels" and radio_state_dialog.isChecked() == True:
                    rowcount_ = cursor.execute('''SELECT COUNT(*) FROM Beams''').fetchone()[0]
                    table_attributes_channels=['Id', 'Designation', 'Mass', 'Area', 'D', 'B', 'tw', 'T', 'FlangeSlope', 'R1', 'R2', 'Cy', 'Iz',
                     'Iy', 'rz', 'ry', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source']
                    
                    tblTable = QTableWidget()

                    tableItem = QTableWidgetItem()
                    tblTable.setWindowTitle("Details")
                    tblTable.setRowCount(rowcount_)
                    tblTable.setColumnCount(21)
                    for i in range(0,21):
                        if i%2==0:
                            item1 = QtWidgets.QTableWidgetItem('green')
                            item1.setBackground(QtGui.QColor( 0,255, 0))
                            tblTable.setHorizontalHeaderItem(i,item1)
                        else:
                            item1 = QtWidgets.QTableWidgetItem('blue')
                            item1.setBackground(QtGui.QColor( 255,0, 0))
                            tblTable.setHorizontalHeaderItem(i,item1)
                    tblTable.setHorizontalHeaderLabels(table_attributes_channels)

                    cursor.execute('''SELECT * FROM Channels''')

                    for row2, form2 in enumerate(cursor):
                        for column2, item2 in enumerate(form2):
                            tblTable.setItem(row2, column2, QTableWidgetItem(str(item2)))
                    tblTable.horizontalHeader().setStretchLastSection(True)
                    tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                    tblTable.show()
                    dialog = QDialog()
                    dialog.setWindowTitle("Data of "+radio_state_dialog.text()+" Section")
                    dialog.resize(600, 400)
                    dialog.setLayout(QVBoxLayout())
                    dialog.layout().addWidget(tblTable)
                    dialog.setStyleSheet("font-size:14px;"
                                                "color: black;"
                                                "background-color: white;"
                                                "font: SanSerif; "
                                                )
                    dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
                    dialog.exec_()
                elif radio_state_dialog.text()=="Angles" and radio_state_dialog.isChecked() == True:
                    rowcount3 = cursor.execute('''SELECT COUNT(*) FROM Angles ''').fetchone()[0]
                    table_attributes_angles=['Id', 'Designation', 'Mass', 'Area', 'AXB', 't', 'R1', 'R2', 'Cz', 'Cy', 'Tan?', 'Iz', 'Iy',
                        'Iu(max)', 'Iv(min)', 'rz', 'ry', 'ru(max)', 'rv(min)', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source']
                    tblTable = QTableWidget()

                    tableItem = QTableWidgetItem()
                    tblTable.setWindowTitle("Details")
                    tblTable.setRowCount(rowcount3)
                    tblTable.setColumnCount(24)
                    tblTable.setHorizontalHeaderLabels(
                        ['Id', 'Designation', 'Mass', 'Area', 'AXB', 't', 'R1', 'R2', 'Cz', 'Cy', 'Tan?', 'Iz', 'Iy',
                        'Iu(max)', 'Iv(min)', 'rz', 'ry', 'ru(max)', 'rv(min)', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source'])
                    cursor.execute('''SELECT * FROM Angles ''')

                    for row, form in enumerate(cursor):
                        for column, item in enumerate(form):
                            tblTable.setItem(row, column, QTableWidgetItem(str(item)))
                    tblTable.horizontalHeader().setStretchLastSection(False)
                    ##########below loop changes color of of table headers ##############
                    for i in range(0,25):
                        if i%2==0:
                            item1 = QtWidgets.QTableWidgetItem('green')
                            item1.setBackground(QtGui.QColor( 0,255, 0))
                            tblTable.setHorizontalHeaderItem(i,item1)
                        else:
                            item1 = QtWidgets.QTableWidgetItem('blue')
                            item1.setBackground(QtGui.QColor( 255,0, 0))
                            tblTable.setHorizontalHeaderItem(i,item1)

                    tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                    tblTable.show()

                    dialog = QDialog()
                    dialog.setWindowTitle("Data of "+radio_state_dialog.text()+" Section")
                    dialog.resize(600, 400)
                    dialog.setLayout(QVBoxLayout())
                    dialog.layout().addWidget(tblTable)
                    dialog.setStyleSheet("font-size:14px;"
                                        "color: black;"
                                        "background-color:white;"
                                        "font: SanSerif; "
                                        )
                    dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
                    dialog.exec()
                
    ########################display sec ended above ###############################################################
    ###########################################################################################################
    ##############################################################################################################
    ###############Appending code starts below##################################
                    
        elif btn_state_main=="append":
                    ##########not intrested in display then obviously intrested in appending data ##########
                    ##########appending into databse and its code willl go here#######
            
            pass
            
            
            
            
            ########below else used to pop up window if something bad happens on choosing radio button###############
        else:
            dg=QDialog()
            dg.setWindowTitle("warning message")
            dg.resize(170, 170)
            label__warn=QLabel("!!!!!Something bad happened")
            dg.setStyleSheet("font-size:32px;"
                                    "color: red;"
                                    "background-color: white;"
                                    "font: SanSerif; "
                                    )
                
            dg.setLayout(QVBoxLayout())
            dg.layout().addWidget(label__warn)
            dg.exec_()
        
        
        
        
app=QApplication(sys.argv)
window=window()
sys.exit(app.exec_())