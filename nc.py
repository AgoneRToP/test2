from PyQt5.QtWidgets import *
import json

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.NajotChat = QLabel("Najot chat")

        self.Username = QLineEdit()
        self.Username.setPlaceholderText("Username")

        self.Password = QLineEdit()
        self.Password.setPlaceholderText("Password")

        self.Login = QPushButton("LOGIN")
        self.Account = QPushButton("Creat new account")

        self.main_lay = QHBoxLayout()
        self.v_center = QVBoxLayout()

        lst = [self.NajotChat, self.Username, self.Password, self.Login, self.Account]

        self.v_center.addStretch()
        for i in lst:    
            self.v_center.addWidget(i)
        self.v_center.addStretch()

        self.main_lay.addStretch()
        self.main_lay.addLayout(self.v_center)
        self.main_lay.addStretch()

        self.setLayout(self.main_lay)

        self.Account.clicked.connect(self.open_register)
        self.Login.clicked.connect(self.handle_login)

    def open_register(self):
        self.reg = RegisterWindow()
        self.reg.show()
        self.close()

    def handle_login(self):
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except:
            users = {}

        name = self.Username.text()
        pwd = self.Password.text()

        if name in users and users[name]["password"] == pwd:
            self.dash = Dashboard(name, users[name])
            self.dash.show()
            self.close()
        else:
            QMessageBox.warning(self, "Xato", "Login yoki parol xato!")

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration")
        self.lay = QVBoxLayout(self)
        
        self.u = QLineEdit(placeholderText="Username")
        self.p = QLineEdit(placeholderText="Password")
        self.e = QLineEdit(placeholderText="Email")
        self.btn = QPushButton("Ro'yxatdan o'tish")
        
        for w in [self.u, self.p, self.e, self.btn]: self.lay.addWidget(w)
        self.btn.clicked.connect(self.save_and_exit)

    def save_and_exit(self):
        try:
            with open("users.json", "r") as f: data = json.load(f)
        except: data = {}

        data[self.u.text()] = {"password": self.p.text(), "email": self.e.text()}
        
        with open("users.json", "w") as f:
            json.dump(data, f, indent=4)
        
        self.back = MyWindow()
        self.back.show()
        self.close()

class Dashboard(QWidget):
    def __init__(self, name, info):
        super().__init__()
        self.setWindowTitle("Profil")
        lay = QVBoxLayout(self)
        lay.addWidget(QLabel(f"Foydalanuvchi: {name}"))
        lay.addWidget(QLabel(f"Email: {info['email']}"))
        btn = QPushButton("Chiqish")
        btn.clicked.connect(lambda: (MyWindow().show(), self.close()))
        lay.addWidget(btn)

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()