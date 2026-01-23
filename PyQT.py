from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

# app = QApplication([])
# win = QWidget()

# ism, fam, yosh = "Azimxon", "Yo'ldoshev", 20 # qatta ma'lumot chiqarish kere?

# v_main_lay = QVBoxLayout()

# lbl_name = QLabel(f"Имя: {ism}")
# lbl_sur = QLabel(f"Фамилия: {fam}")
# lbl_year = QLabel(f"Год: {yosh}")

# v_main_lay.addWidget(lbl_name)
# v_main_lay.addWidget(lbl_sur)
# v_main_lay.addWidget(lbl_year)

# win.setLayout(v_main_lay)


# win.show()
# app.exec_()



# name, sur, year = input("Имя: "), input("Фамилия: "), int(input("Год: "))

# class MyWindow(QWidget):
#     def __init__(self, name, sur, year):
#         super().__init__()

#         self.v_main_lay = QVBoxLayout()

#         self.lbl_name = QLabel(f"Имя: {name}")
#         self.lbl_sur = QLabel(f"Фамилия: {sur}")
#         self.lbl_year = QLabel(f"Год: {year}")

#         self.v_main_lay.addWidget(self.lbl_name)
#         self.v_main_lay.addWidget(self.lbl_sur)
#         self.v_main_lay.addWidget(self.lbl_year)

#         self.setLayout(self.v_main_lay)

# app = QApplication([])
# win = MyWindow(name, sur, year)
# win.show()
# app.exec_()



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.lbl_year = QLabel("Введите год рождения:")
        self.edit_year = QLineEdit()
        self.btn_year = QPushButton("OK")

        self.btn_year.clicked.connect(self.click)

        self.layout.addWidget(self.lbl_year)
        self.layout.addWidget(self.edit_year)
        self.layout.addWidget(self.btn_year)

        self.setLayout(self.layout)

    def click(self):
        year_text = self.edit_year.text()

        if year_text.isdigit():
            birth_year = int(year_text)
            current_year = 2026
            age = current_year - birth_year
            
            print(f"Ему {age} лет")
        else:
            print("Ошибка: введите корректный год цифрами!")




app = QApplication([])
win = MyWindow()
win.show()
app.exec_()