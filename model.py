from PyQt5.QtWidgets import QApplication,QWidget ,QDialog ,  QMainWindow ,QLabel, QPushButton ,QVBoxLayout ,QHBoxLayout ,QGridLayout ,QGroupBox,QRadioButton
class model1:
    def genrate_msg(self):
        dg1=QDialog()
        dg1.setWindowTitle("Database message")
        dg1.resize(170, 170)
        label__warn=QLabel("Data inserted at position")
        dg1.setStyleSheet("font-size:32px;"
                                    "color: red;"
                                    "background-color: white;"
                                    "font: SanSerif; "
                                    )
                
        dg1.setLayout(QVBoxLayout())
        dg1.layout().addWidget(label__warn)
        dg1.exec_()
    def append_in_channel_database(self,get_data):
        self.genrate_msg()
        
    def append_in_beams_database(self,get_data):
        self.genrate_msg()
    def append_in_angle_database(self,get_data):
        self.genrate_msg()