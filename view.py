from PyQt5.QtWidgets import QApplication,QWidget ,QDialog , QTableWidget, QTableWidgetItem, QMainWindow ,QLabel, QPushButton ,QVBoxLayout ,QHBoxLayout ,QGridLayout ,QGroupBox,QRadioButton
import sys
import model
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon , QFont ,QPixmap 
from PyQt5.QtCore import QSize , Qt ,QRect,QMetaObject,QCoreApplication
import sqlite3
import os # used to check if db_exists in path
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(80,100,400,400)
        self.setWindowTitle(" Fossee simple app")
        self.setWindowOpacity(1)
        self.setStyleSheet("background-color:white ")
        self.create_button()
        # self.setLayout(grid)
        vbox=QVBoxLayout()
        self.label_image=QLabel(self)
        vbox.addWidget(self.label_image,alignment=Qt.AlignHCenter)
        self.pixmap = QPixmap('steel tubes.jpg')
        self.label_image.setPixmap(self.pixmap.scaled(500,200)) 
        self.label_image.setScaledContents(True)
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
        
        self.btn3=QPushButton("Delete")
        self.btn3.clicked.connect(lambda:self.on_pressed("delete"))
        self.btn3.setIcon(QIcon("append.png")) 
        self.btn3.setIconSize(QSize(33, 30))
        # self.btn2.QSize(10, 10) 
        self.btn3.setStyleSheet("background-color:blue;color:black")
        hbox.addWidget(self.btn3)
        
        self.groupbox.setLayout(hbox)
        
######################## main windows button functions and genration of############################
# ##############another dialog which get radio inputs to select paticualr fxn################################
    def on_pressed(self,obj_btn_get):
        ######### passing argument above in order two which window which button pressed############
        dialog_box1 = QDialog()
        dialog_box1.setWindowTitle(obj_btn_get+ " menu")
        #label_btn_selected=QLabel("")
        dialog_box1.resize(250, 300)
        
        h_box1 = QHBoxLayout()
        v_box1 = QVBoxLayout()
        h_box1.addStretch()
        self.label_image=QLabel(self)
        v_box1.addWidget(self.label_image,alignment=Qt.AlignHCenter)
        
        if obj_btn_get=="display":###this if else sets images on dialog acc to button pressed
            self.pixmap = QPixmap('display.png') 
        elif obj_btn_get=="append":
            self.pixmap = QPixmap('append.jpg') 
        else:
            print("deleteeee")
            self.label_delete=QtWidgets.QLabel(" enter id of table to delete ")
            self.line_delete=QtWidgets.QLineEdit(self)
        self.label_image.setPixmap(self.pixmap.scaled(100,100)) 
        self.label_image.setScaledContents(True)
        
        self.channels_rad = QRadioButton("Channels")
        self.channels_rad.setStyleSheet("background-color:powderblue; color:black")
        self.beams_rad = QRadioButton("Beams")
        self.beams_rad.setStyleSheet("background-color:powderblue; color:black")
        self.angles_rad = QRadioButton("Angles")
        self.angles_rad.setStyleSheet("background-color:powderblue; color:black")
        self.label1 = QLabel("Select A Table to "+obj_btn_get)
        v_box1.addWidget(self.label1, alignment=Qt.AlignHCenter)
        self.label1.setStyleSheet("color:green ; font-size:17px;")
        if obj_btn_get=="delete":
            v_box1.addWidget(self.label_delete)
            v_box1.addWidget(self.line_delete)
            h_box1.addLayout(h_box1)
        h_box1.addWidget(self.channels_rad,alignment=Qt.AlignHCenter)

        h_box1.addWidget(self.beams_rad,alignment=Qt.AlignHCenter)
        h_box1.addWidget(self.angles_rad,alignment=Qt.AlignHCenter)
        h_box1.addStretch()
        
        
        v_box1.addLayout(h_box1)
        
        self.label2=QLabel("<b>"+obj_btn_get+"</b> "+"chosen by you")
        self.label2.setStyleSheet("background-color:white; color:blue; font-size:17px;")
        
        v_box1.addWidget(self.label2)
        if obj_btn_get!="delete":
            self.channels_rad.toggled.connect(lambda: self.btn_state(self.channels_rad,obj_btn_get))
            self.beams_rad.toggled.connect(lambda: self.btn_state(self.beams_rad,obj_btn_get))
            self.angles_rad.toggled.connect(lambda: self.btn_state(self.angles_rad,obj_btn_get))
        else:   
            ob=model.model1()
            print("jjjjjjjjjjjjjjjjj ",self.channels_rad.text(),self.angles_rad.text(),self.beams_rad.text())
            
            # if self.channels_rad.text()=="Channels" and  self.channels_rad.isChecked() == True:
            #     print(" true channel")
            self.channels_rad.toggled.connect(lambda:ob.delete_start(self.line_delete.text(),"channels"))
            # elif self.angles_rad.text() =="Angles" and  self.angles_rad.isChecked() == True:
            #     print(" tru angle")
            self.angles_rad.toggled.connect(lambda:ob.delete_start(self.line_delete.text(),"beams"))
            # elif self.beams_rad.text()=="Beams" and  self.beams_rad.isChecked() == True:
            #     print(" beam tru")
            self.beams_rad.toggled.connect(lambda:ob.delete_start(self.line_delete.text(),"beamss"))
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
            #print(radio_state_dialog.text())
            db_exists=not os.path.exists('steel_sections.sqlite')
            #print("db_exists->",db_exists)
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
                    tblTable.setHorizontalHeaderLabels(table_attributes)
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
                    rowcount_ = cursor.execute('''SELECT COUNT(*) FROM Channels''').fetchone()[0]
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
                    
                    for i in range(0,25):
                        if i%2==0:
                            item1 = QtWidgets.QTableWidgetItem('green')
                            item1.setBackground(QtGui.QColor( 0,255, 0))
                            tblTable.setHorizontalHeaderItem(i,item1)
                        else:
                            item1 = QtWidgets.QTableWidgetItem('blue')
                            item1.setBackground(QtGui.QColor( 255,0, 0))
                            tblTable.setHorizontalHeaderItem(i,item1)
                    tblTable.setHorizontalHeaderLabels(table_attributes_angles)
                    cursor.execute('''SELECT * FROM Angles ''')

                    for row, form in enumerate(cursor):
                        for column, item in enumerate(form):
                            tblTable.setItem(row, column, QTableWidgetItem(str(item)))
                    tblTable.horizontalHeader().setStretchLastSection(False)
                    ##########below loop changes color of of table headers ##############
                    
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
            def append_data_into_channel_or_beams_dialog(self,radio_state_know):
                Dialog1=QDialog()
                Dialog1.setObjectName("Dialog")
                Dialog1.resize(373, 384)
                Dialog1.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.formLayoutWidget = QtWidgets.QWidget(Dialog1)
                self.formLayoutWidget.setGeometry(QRect(20, 40, 171, 331))
                self.formLayoutWidget.setObjectName("formLayoutWidget")
                self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
                self.formLayout.setContentsMargins(0, 0, 0, 0)
                self.formLayout.setObjectName("formLayout")
                self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_2.setObjectName("label_2")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
                self.channel_Designation = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.channel_Designation.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "")
                self.channel_Designation.setObjectName("channel_Designation")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_Designation)
                self.label = QtWidgets.QLabel(self.formLayoutWidget)
                self.label.setObjectName("label")
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
                self.channel_Mass = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.channel_Mass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "\n"
                "")
                self.channel_Mass.setObjectName("channel_Mass")
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.channel_Mass)
                self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_3.setObjectName("label_3")
                self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
                self.Area = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.Area.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.Area.setObjectName("Area")
                self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Area)
                self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_4.setObjectName("label_4")
                self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
                self.channel_D = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.channel_D.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "\n"
                "")
                self.channel_D.setObjectName("channel_D")
                self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.channel_D)
                self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_15.setObjectName("label_15")
                self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
                self.channel_B = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.channel_B.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "")
                self.channel_B.setObjectName("channel_B")
                self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.channel_B)
                self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_14.setObjectName("label_14")
                self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
                self.channel_tw = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.channel_tw.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_tw.setObjectName("channel_tw")
                self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.channel_tw)
                self.channel_T = QtWidgets.QLabel(self.formLayoutWidget)
                self.channel_T.setObjectName("channel_T")
                self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.channel_T)
                self.lineEdit_15 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "")
                self.lineEdit_15.setObjectName("lineEdit_15")
                self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
                self.channel_FlangeSlope = QtWidgets.QLabel(self.formLayoutWidget)
                self.channel_FlangeSlope.setObjectName("channel_FlangeSlope")
                self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.channel_FlangeSlope)
                self.lineEdit_16 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_16.setObjectName("lineEdit_16")
                self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)
                self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_17.setObjectName("label_17")
                self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_17)
                self.channel_R1 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.channel_R1.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_R1.setObjectName("channel_R1")
                self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.channel_R1)
                self.channel_R2 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.channel_R2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "")
                self.channel_R2.setObjectName("channel_R2")
                self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.channel_R2)
                self.label_27 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_27.setObjectName("label_27")
                self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_27)
                self.label_37 = QtWidgets.QLabel(Dialog1)
                self.label_37.setGeometry(QRect(20, 10, 241, 20))
                self.label_37.setStyleSheet("color: rgb(0, 170, 0);\n"
                "font: 75 12pt \"MS Shell Dlg 2\";")
                self.label_37.setObjectName("label_37")
                self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog1)
                self.formLayoutWidget_2.setGeometry(QRect(210, 40, 151, 331))
                self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
                self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
                self.formLayout_2.setContentsMargins(0, 0, 0, 0)
                self.formLayout_2.setObjectName("formLayout_2")
                self.label_28 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_28.setObjectName("label_28")
                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_28)
                self.channel_Iz = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_Iz.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_Iz.setObjectName("channel_Iz")
                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_Iz)
                self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_29.setObjectName("label_29")
                self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_29)
                self.channel_Iy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_Iy.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_Iy.setObjectName("channel_Iy")
                self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.channel_Iy)
                self.label_30 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_30.setObjectName("label_30")
                self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_30)
                self.channel_rz = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_rz.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_rz.setObjectName("channel_rz")
                self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.channel_rz)
                self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_31.setObjectName("label_31")
                self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_31)
                self.channel_ry = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_ry.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_ry.setObjectName("channel_ry")
                self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.channel_ry)
                self.label_32 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_32.setObjectName("label_32")
                self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_32)
                self.channel_zz = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_zz.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_zz.setObjectName("channel_zz")
                self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.channel_zz)
                self.label_33 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_33.setObjectName("label_33")
                self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_33)
                self.channel_Zy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_Zy.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_Zy.setObjectName("channel_Zy")
                self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.channel_Zy)
                self.label_34 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_34.setObjectName("label_34")
                self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_34)
                self.channel_Zpz = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_Zpz.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_Zpz.setObjectName("channel_Zpz")
                self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.channel_Zpz)
                self.label_35 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_35.setObjectName("label_35")
                self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_35)
                self.channel_Zpy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_Zpy.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_Zpy.setObjectName("channel_Zpy")
                self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.channel_Zpy)
                self.label_36 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_36.setObjectName("label_36")
                self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_36)
                self.channel_Source = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.channel_Source.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.channel_Source.setObjectName("channel_Source")
                self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.channel_Source)
                spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.formLayout_2.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem)
                self.channel_push_submit = QtWidgets.QPushButton(self.formLayoutWidget_2)
                self.channel_push_submit.setStyleSheet("background-color: rgb(0, 0, 255);")
                self.channel_push_submit.setObjectName("channel_push_submit")
                self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.channel_push_submit)
                
                QMetaObject.connectSlotsByName(Dialog1)
                def get_data_from_beams_or_Channel_form(get):
                    obj=model.model1()
                    if radio_state_know=="Channels":
                        
                        obj.append_in_channel_database(get)
                    else:
                       
                        obj.append_in_beams_database(get)        
                
                self.channel_push_submit.clicked.connect(lambda:get_data_from_beams_or_Channel_form([self.channel_Designation.text(),
                                                                    self.channel_Mass.text(),self.Area.text()
                                                                   ,self.channel_D.text(),self.channel_B.text()
                                                                   ,self.channel_tw.text()
                                                                   ,self.lineEdit_15.text(),self.lineEdit_16.text()
                                                                   ,self.channel_R1.text(),self.channel_R2.text(),self.channel_Iz.text()
                                                                   ,self.channel_Iy.text(),self.channel_rz.text(),self.channel_ry.text()
                                                                   ,self.channel_zz.text(),self.channel_Zy.text(),self.channel_Zpz.text()
                                                                   ,self.channel_Zpy.text(),self.channel_Source.text() ] ))
                QMetaObject.connectSlotsByName(Dialog1)
                def retranslateUi1(self, Dialog1):
                    _translate = QCoreApplication.translate
                    Dialog1.setWindowTitle(_translate("Dialog", radio_state_know+" form"))
                    self.label_2.setText(_translate("Dialog", "Designation"))
                    self.label.setText(_translate("Dialog", "Mass"))
                    self.label_3.setText(_translate("Dialog", "Area"))
                    self.label_4.setText(_translate("Dialog", "D"))
                    self.label_15.setText(_translate("Dialog", "B"))
                    self.label_14.setText(_translate("Dialog", "tw"))
                    self.channel_T.setText(_translate("Dialog", "T"))
                    self.channel_FlangeSlope.setText(_translate("Dialog", "FlangeSlope"))
                    self.label_17.setText(_translate("Dialog", "R1"))
                    self.label_27.setText(_translate("Dialog", "R2"))
                    
                    self.label_37.setText(_translate("Dialog", "Enter "+radio_state_know+" details "))
                    self.label_28.setText(_translate("Dialog", "Iz"))
                    self.label_29.setText(_translate("Dialog", "Iy"))
                    self.label_30.setText(_translate("Dialog", "rz"))
                    self.label_31.setText(_translate("Dialog", "ry"))
                    self.label_32.setText(_translate("Dialog", "Zz"))
                    self.label_33.setText(_translate("Dialog", "Zy"))
                    self.label_34.setText(_translate("Dialog", "Zpz"))
                    self.label_35.setText(_translate("Dialog", "Zpy"))
                    self.label_36.setText(_translate("Dialog", "Source"))
                    self.channel_push_submit.setText(_translate("Dialog", "Submit"))
                retranslateUi1(self,Dialog1)
                
                Dialog1.exec_()
               
            #####################################################################################################
            ##############################end above fxn insert into beams or angles###########   
            def append_data_into_angels_dialog(self):
                Dialog1=QDialog()
                Dialog1.setObjectName("Dialog")
                Dialog1.resize(373, 384)
                Dialog1.setObjectName("Dialog")
                Dialog1.resize(373, 387)
                Dialog1.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.formLayoutWidget = QtWidgets.QWidget(Dialog1)
                self.formLayoutWidget.setGeometry(QRect(20, 40, 171, 333))
                self.formLayoutWidget.setObjectName("formLayoutWidget")
                self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
                self.formLayout.setContentsMargins(0, 0, 0, 0)
                self.formLayout.setObjectName("formLayout")
                self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_2.setObjectName("label_2")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
                self.angle_Designation = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.angle_Designation.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "")
                self.angle_Designation.setObjectName("angle_Designation")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.angle_Designation)##
                self.label = QtWidgets.QLabel(self.formLayoutWidget)
                self.label.setObjectName("label")
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
                self.angle_Mass = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.angle_Mass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "\n"
                "")
                self.angle_Mass.setObjectName("angle_Mass")
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.angle_Mass)##
                self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_3.setObjectName("label_3")
                self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
                self.Area = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.Area.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.Area.setObjectName("Area")
                self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Area)##
                self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_4.setObjectName("label_4")
                self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
                self.angle_D = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.angle_D.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "\n"
                "")
                self.angle_D.setObjectName("angle_D")
                self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.angle_D)
                self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_15.setObjectName("label_15")
                self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
                self.angle_B = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.angle_B.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "")
                self.angle_B.setObjectName("angle_B")
                self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.angle_B)
                self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_14.setObjectName("label_14")
                self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
                self.angle_tw = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.angle_tw.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_tw.setObjectName("angle_tw")
                self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.angle_tw)
                self.angle_T = QtWidgets.QLabel(self.formLayoutWidget)
                self.angle_T.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_T.setObjectName("angle_T")
                self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.angle_T)
                self.lineEdit_15 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "")
                self.lineEdit_15.setObjectName("lineEdit_15")
                self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
                self.angle_FlangeSlope = QtWidgets.QLabel(self.formLayoutWidget)
                self.angle_FlangeSlope.setObjectName("angle_FlangeSlope")
                self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.angle_FlangeSlope)
                self.lineEdit_16 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_16.setObjectName("lineEdit_16")
                self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)
                self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_17.setObjectName("label_17")
                self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_17)
                self.angle_R1 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.angle_R1.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_R1.setObjectName("angle_R1")
                self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.angle_R1)
                self.label_27 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_27.setObjectName("label_27")
                self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_27)
                self.angle_R2 = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.angle_R2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "")
                self.angle_R2.setObjectName("angle_R2")
                self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.angle_R2)
                self.label_28 = QtWidgets.QLabel(self.formLayoutWidget)
                self.label_28.setObjectName("label_28")
                self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_28)
                self.angle_Iz = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.angle_Iz.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_Iz.setObjectName("angle_Iz")
                self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.angle_Iz)
                self.label_37 = QtWidgets.QLabel(Dialog1)
                self.label_37.setGeometry(QRect(20, 10, 241, 20))
                self.label_37.setStyleSheet("color: rgb(0, 170, 0);\n"
                "font: 75 12pt \"MS Shell Dlg 2\";")
                self.label_37.setObjectName("label_37")
                self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog1)
                self.formLayoutWidget_2.setGeometry(QRect(200, 40, 151, 331))
                self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
                self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
                self.formLayout_2.setContentsMargins(0, 0, 0, 0)
                self.formLayout_2.setObjectName("formLayout_2")
                self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_29.setObjectName("label_29")
                self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_29)
                self.angle_Iy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_Iy.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_Iy.setObjectName("angle_Iy")
                self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.angle_Iy)
                self.label_30 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_30.setObjectName("label_30")
                self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_30)
                self.angle_rz = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_rz.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_rz.setObjectName("angle_rz")
                self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.angle_rz)
                self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_31.setObjectName("label_31")
                self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_31)
                self.angle_ry = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_ry.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_ry.setObjectName("angle_ry")
                self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.angle_ry)
                self.label_32 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_32.setObjectName("label_32")
                self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_32)
                self.angle_zz = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_zz.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_zz.setObjectName("angle_zz")
                self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.angle_zz)
                self.label_33 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_33.setObjectName("label_33")
                self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_33)
                self.angle_Zy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_Zy.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_Zy.setObjectName("angle_Zy")
                self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.angle_Zy)
                self.label_34 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_34.setObjectName("label_34")
                self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_34)
                self.angle_Zpz = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_Zpz.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_Zpz.setObjectName("angle_Zpz")
                self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.angle_Zpz)
                self.label_35 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_35.setObjectName("label_35")
                self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_35)
                self.angle_Zpy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_Zpy.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_Zpy.setObjectName("angle_Zpy")
                self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.angle_Zpy)
                self.label_36 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_36.setObjectName("label_36")
                self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_36)
                self.angle_Source = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_Source.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_Source.setObjectName("angle_Source")
                self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.angle_Source)
                self.label_38 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_38.setObjectName("label_38")
                self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_38)
                self.angle_Source_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_Source_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_Source_2.setObjectName("angle_Source_2")
                self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.angle_Source_2)
                self.angle_Source_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
                self.angle_Source_3.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.angle_Source_3.setObjectName("angle_Source_3")
                self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.angle_Source_3)
                self.label_39 = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.label_39.setObjectName("label_39")
                self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_39)
                self.angle_push_submit = QPushButton(self.formLayoutWidget_2)
                self.angle_push_submit.setStyleSheet("background-color: rgb(0, 0, 255);")
                self.angle_push_submit.setObjectName("angle_push_submit")
                self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.angle_push_submit)
                
                def get_data_from_Angle_form(get):
                           obj1=model.model1()
                          
                           obj1.append_in_angle_database(get)           
                #self.angle_push_submit.clicked.connect(lambda:abc(self.label.text()))
                self.angle_push_submit.clicked.connect(lambda:get_data_from_Angle_form([self.angle_Designation.text(),
                                                                    self.angle_Mass.text(),self.Area.text()
                                                                   ,self.angle_D.text(),self.angle_B.text()
                                                                   ,self.angle_tw.text(),self.angle_T.text()
                                                                   ,self.lineEdit_15.text(),self.angle_FlangeSlope.text(),self.lineEdit_16.text()
                                                                   ,self.angle_R1.text(),self.angle_R2.text(),self.angle_Iz.text()
                                                                   ,self.angle_Iy.text(),self.angle_rz.text(),self.angle_ry.text()
                                                                   ,self.angle_zz.text(),self.angle_Zy.text(),self.angle_Zpz.text()
                                                                   ,self.angle_Zpy.text(),self.angle_Source.text(),self.angle_Source_2.text()
                                                                   ,self.angle_Source_3.text() ] ))
                #QMetaObject.connectSlotsByName(Dialog1)

                def retranslateUi2(self, Dialog1):
                    _translate = QCoreApplication.translate
                    Dialog1.setWindowTitle(_translate("Dialog", "Angles Form"))
                    self.label_2.setText(_translate("Dialog", "Designation")) #
                    self.label.setText(_translate("Dialog", "Mass"))#
                    self.label_3.setText(_translate("Dialog", "t"))#
                    self.label_4.setText(_translate("Dialog", "R1"))#
                    self.label_15.setText(_translate("Dialog", "R2"))#
                    self.label_14.setText(_translate("Dialog", "Cz"))#
                    self.angle_T.setText(_translate("Dialog", "Cy"))
                    self.angle_FlangeSlope.setText(_translate("Dialog", "Tan?"))#
                    self.label_17.setText(_translate("Dialog", "Iz"))
                    self.label_27.setText(_translate("Dialog", "Iy"))#
                    self.label_28.setText(_translate("Dialog", "Iu(max)"))
                    self.label_37.setText(_translate("Dialog", "Enter Angle details"))
                    self.label_29.setText(_translate("Dialog", "Iv(min)"))
                    self.label_30.setText(_translate("Dialog", "rz"))
                    self.label_31.setText(_translate("Dialog", "ry"))
                    self.label_32.setText(_translate("Dialog", "ru(max)"))
                    self.label_33.setText(_translate("Dialog", "rv(min)"))
                    self.label_34.setText(_translate("Dialog", "Zz"))
                    self.label_35.setText(_translate("Dialog", "Zy"))
                    self.label_36.setText(_translate("Dialog", "Zpz"))
                    self.label_38.setText(_translate("Dialog", "Zpy"))
                    self.label_39.setText(_translate("Dialog", "Source"))
                    self.angle_push_submit.setText(_translate("Dialog", "Submit"))
                
                retranslateUi2(self,Dialog1)
                
                Dialog1.exec_()
            
            if (radio_state_dialog.text()=="Channels" or radio_state_dialog.text()=="Beams") and radio_state_dialog.isChecked() == True:
                append_data_into_channel_or_beams_dialog(self,radio_state_dialog.text())
            elif radio_state_dialog.text()=="Angles" and radio_state_dialog.isChecked() == True:
                append_data_into_angels_dialog(self)
                
                
                ########below else used to pop up window if something bad happens on choosing radio button###############
        
        else:
            dg=QDialog()
            dg.setWindowTitle("warning message")
            dg.resize(170, 170)
            label__warn=QLabel("!!!!!Something bad happened")
            s=QtWidgets.QLineEdit(self)
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