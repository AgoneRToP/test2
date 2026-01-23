from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.display = QLineEdit()

        self.lbl_natija = QLabel()

        btn = QPushButton("Посчитать")
        btn.clicked.connect(self.calc)

        self.lbl_cat = QLabel("""
                 ／＞　 フ
　　 　　　   | 　_　 _| 
　 　 　  　／`ミ _x 彡 
　 　 　   /　　　 　   | 
　 　　   /　   ヽ　　 ﾉ  
 　／￣|　　 |　|　|  
　| (￣ヽ＿_ヽ_)_) 
 　＼二つ
""")
        
        layout.addWidget(self.display)
        layout.addWidget(self.lbl_natija)
        layout.addWidget(btn)
        layout.addWidget(self.lbl_cat)


        self.setLayout(layout)

    def calc(self):
        try:
            res = eval(self.display.text())
            self.lbl_natija.setText(str(res))
        except:
            self.display.setText("Ошибка")



app = QApplication([])
win = MyWindow()
win.show()
app.exec_()