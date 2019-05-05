import sys
import json
from reading_data import *
from sign_in import SignIn
from register import Register
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Registration')
        self.setFixedSize(220, 480)
        self.setWindowIcon(QtGui.QIcon('money.png'))

        vbox = QtWidgets.QVBoxLayout(self)

        self.stacked = QtWidgets.QStackedWidget(self)

        global sign_in
        sign_in = SignIn()
        self.stacked.addWidget(sign_in)

        sign_in.setStyleSheet(open('signIn-stylesheet.qss', 'r').read())

        sign_in.joinBtn.clicked.connect(self.signIn_registration)

        global register
        register = Register()
        self.stacked.addWidget(register)

        register.setStyleSheet(open('register-stylesheet.qss', 'r').read())

        register.signInBtn.clicked.connect(self.registration_signIn)

        vbox.addWidget(self.stacked)

        self.show()

    def signIn_registration(self):
        sign_in.usernameInput.setText('')
        sign_in.passwordInput.setText('')

        sign_in.usernameError.setText('')
        sign_in.passwordError.setText('')

        self.stacked.setCurrentIndex(1)

    def registration_signIn(self):
        register.nameInput.setText('')
        register.usernameInput.setText('')
        register.passwordInput.setText('')
        register.confirmationInput.setText('')

        register.usernameError.setText('')
        register.passwordError.setText('')

        self.stacked.setCurrentIndex(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
