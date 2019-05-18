import sys
import shutil
import json
from reading_data import *
from sign_in import SignIn
from register import Register
from main_window import *
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sign In')
        self.setFixedSize(220, 480)
        self.setWindowIcon(QtGui.QIcon('icons/money.png'))

        vbox = QtWidgets.QVBoxLayout(self)

        self.stacked = QtWidgets.QStackedWidget(self)

        # ---------- SIGN IN WINDOW ---------- #
        global sign_in
        sign_in = SignIn()
        self.stacked.addWidget(sign_in)

        sign_in.setStyleSheet(open('signIn-stylesheet.qss', 'r').read())

        sign_in.joinBtn.clicked.connect(self.signIn_registration)

        # ---------- REGISTER WINDOW ---------- #
        global register
        register = Register()
        self.stacked.addWidget(register)

        register.setStyleSheet(open('register-stylesheet.qss', 'r').read())

        register.signInBtn.clicked.connect(self.registration_signIn)

        # ---------- MAIN WINDOW ---------- #
        

        vbox.addWidget(self.stacked)

        self.show()

    def signIn_registration(self):
        self.setWindowTitle('Join Us')
        sign_in.usernameInput.setText('')
        sign_in.passwordInput.setText('')

        sign_in.usernameError.setText('')
        sign_in.passwordError.setText('')

        sign_in.passwordInput.setStyleSheet('border-color: #68B2A0;')
        sign_in.usernameInput.setStyleSheet('border-color: #68B2A0;')


        self.stacked.setCurrentIndex(1)

    def registration_signIn(self):
        self.setWindowTitle('Sign In')
        register.nameInput.setText('')
        register.usernameInput.setText('')
        register.passwordInput.setText('')

        register.usernameError.setText('')
        register.passwordError.setText('')

        register.nameInput.setStyleSheet('border-color: #68B2A0;')
        register.passwordInput.setStyleSheet('border-color: #68B2A0;')
        register.usernameInput.setStyleSheet('border-color: #68B2A0;')

        self.stacked.setCurrentIndex(0)

if __name__ == '__main__':
    shutil.move('signIn-stylesheet.css', 'signIn-stylesheet.qss')
    shutil.move('register-stylesheet.css', 'register-stylesheet.qss')
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    shutil.move('signIn-stylesheet.qss', 'signIn-stylesheet.css')
    shutil.move('register-stylesheet.qss', 'register-stylesheet.css')
    sys.exit(app.exec_())
