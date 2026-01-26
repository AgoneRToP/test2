import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QMessageBox, QGridLayout, QHBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("name...")

        self.second = QLineEdit()
        self.second.setPlaceholderText("second...")

        self.age = QLineEdit()
        self.age.setPlaceholderText("age...")

        self.email = QLineEdit()
        self.email.setPlaceholderText("email...")

        self.r_m = QRadioButton("M")
        self.r_f = QRadioButton("F")
        self.r_m.setChecked(True)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.r_m)
        radio_layout.addWidget(self.r_f)

        self.cmb_shahar = QComboBox()
        self.cmb_shahar.addItems(["Tashkent", "Samarkand", "Bukhara"])

        self.cmb_tuman = QComboBox()
        self.cmb_tuman.addItems(["Yunusabad", "Chilonzor", "Mirzo Ulugbek"])

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.r_m)
        radio_layout.addWidget(self.r_f)

        btn_ok = QPushButton("OK")
        btn_reset = QPushButton("Reset")
        btn_exit = QPushButton("Exit")

        btn_ok.clicked.connect(self.show_data)
        btn_reset.clicked.connect(self.reset_form)
        btn_exit.clicked.connect(self.close)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_reset)
        btn_layout.addWidget(btn_ok)
        btn_layout.addWidget(btn_exit)

        layout = QGridLayout()
        layout.addWidget(QLabel("Name:"), 0, 0)
        layout.addWidget(self.name, 0, 1)
        
        layout.addWidget(QLabel("Surname:"), 1, 0)
        layout.addWidget(self.second, 1, 1)

        layout.addWidget(QLabel("Age:"), 2, 0)
        layout.addWidget(self.age, 2, 1)

        layout.addWidget(QLabel("Email:"), 3, 0)
        layout.addWidget(self.email, 3, 1)

        layout.addWidget(QLabel("Gender:"), 4, 0)
        layout.addLayout(radio_layout, 4, 1)

        layout.addWidget(QLabel("City:"), 5, 0)
        layout.addWidget(self.cmb_shahar, 5, 1)

        layout.addWidget(QLabel("District:"), 6, 0)
        layout.addWidget(self.cmb_tuman, 6, 1)

        layout.addLayout(btn_layout, 7, 0, 1, 2)

        self.setLayout(layout)

        btn_ok.clicked.connect(self.show_data)
        btn_reset.clicked.connect(self.reset_form)
        btn_exit.clicked.connect(self.close)

    def show_data(self):
        data = {
            "name": self.name.text(),
            "surname": self.second.text(),
            "age": self.age.text(),
            "email": self.email.text(),
            "gender": "M" if self.r_m.isChecked() else "F",
            "city": self.cmb_shahar.currentText(),
            "district": self.cmb_tuman.currentText()
        }

        if not data["name"] or not data["email"]:
            QMessageBox.warning(self, "Error", "Please fill in Name and Email!")
            return

        with open("user_data.json", "w") as f:
            json.dump(data, f, indent=4)

        QMessageBox.information(self, "Success", "Data saved to user_data.json")

    def reset_form(self):
        self.name.clear()
        self.second.clear()
        self.age.clear()
        self.email.clear()
        self.r_m.setChecked(True)
        self.cmb_shahar.setCurrentIndex(0)



if __name__ == "__main__":
    app = QApplication([])
    w = MyWindow()
    w.show()
    app.exec_()