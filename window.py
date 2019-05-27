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

        signIn_stylesheet = self.load_css('signIn-stylesheet.css')
        register_stylesheet = self.load_css('register-stylesheet.css')
        mainWindow_stylesheet = self.load_css('mainWindow-stylesheet.css')

        self.setWindowTitle('Sign In')
        self.setFixedSize(220, 480)
        self.setWindowIcon(QtGui.QIcon('icons/money.png'))

        vbox = QtWidgets.QVBoxLayout(self)

        self.stacked = QtWidgets.QStackedWidget(self)

        # ---------- SIGN IN WINDOW ---------- #
        global sign_in
        sign_in = SignIn()
        self.stacked.addWidget(sign_in)

        sign_in.setStyleSheet(signIn_stylesheet)

        # Change to the register window
        sign_in.joinBtn.clicked.connect(self.signIn_registration)

        sign_in.signInBtn.clicked.connect(self.signIn_mainWindow)

        # ---------- REGISTER WINDOW ---------- #
        global register
        register = Register()
        self.stacked.addWidget(register)

        register.setStyleSheet(register_stylesheet)

        register.signInBtn.clicked.connect(self.registration_signIn)

        # ---------- MAIN WINDOW ---------- #
        global main_window
        main_window = MainWindow()

        self.stacked.addWidget(main_window)

        main_window.setStyleSheet(mainWindow_stylesheet)

        vbox.addWidget(self.stacked)

        self.show()

    def load_css(self, css_filename):
        qss_filename = css_filename.split('.')[0] + '.qss'

        shutil.move(css_filename, qss_filename)

        with open(qss_filename, 'r') as f:
            stylesheet = f.read()

        shutil.move(qss_filename, css_filename)

        return stylesheet


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

    def signIn_mainWindow(self):

        if sign_in.onPressed() == True:
            self.setWindowTitle('My Money')
            self.setFixedSize(640, 480)
            self.move(350, 145)

            self.stacked.setCurrentIndex(2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
