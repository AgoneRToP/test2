from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QMessageBox, QCheckBox, QRadioButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_lbl_cmb_lay = QHBoxLayout()

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()