import sys
import json
from reading_data import *
from PyQt5 import QtWidgets, QtGui, QtCore


class SignIn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.vbox = QtWidgets.QVBoxLayout()

        spacer1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed)
        spacer2 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Fixed)
        spacer3 = QtWidgets.QSpacerItem(0, 80, QtWidgets.QSizePolicy.Fixed)


        # --------------- USERNAME ----------------#

        self.usernameInput = QtWidgets.QLineEdit()
        self.usernameInput.setPlaceholderText('Username')
        self.usernameInput.setObjectName('usernameInput')

        self.usernameError = QtWidgets.QLabel()
        self.usernameError.setObjectName('errorMensage')

        # --------------- PASSWORD ---------------#

        self.passwordInput = QtWidgets.QLineEdit()
        self.passwordInput.setPlaceholderText('Password')
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName('passwordInput')

        self.passwordError = QtWidgets.QLabel()
        self.passwordError.setObjectName('errorMensage')


        self.showPasswordBtn = QtWidgets.QPushButton()
        self.showPasswordBtn.setObjectName('showPasswordBtn')

        self.showPasswordBtn.setIcon(QtGui.QIcon('icons/show.png'))
        self.showPasswordBtn.clicked.connect(self.showPassword)

        self.showInputHbox = QtWidgets.QHBoxLayout()

        self.showInputHbox.addWidget(self.passwordInput)
        self.showInputHbox.addWidget(self.showPasswordBtn)
        self.showInputHbox.setAlignment(self.showPasswordBtn, QtCore.Qt.AlignRight)

        # -------------- SIGN IN BUTTON ------------- #
        self.signInBtn = QtWidgets.QPushButton('Sign in')
        self.signInBtn.setObjectName('signInBtn')
        self.signInBtn.clicked.connect(self.onPressed)

        # -------------- JOIN BUTTON ----------------#
        self.joinBtn = QtWidgets.QPushButton('Join us')
        self.joinBtn.setObjectName('joinBtn')

        self.joinLabel = QtWidgets.QLabel('New here? ')
        self.joinLabel.setAlignment(QtCore.Qt.AlignRight)

        self.hbox = QtWidgets.QHBoxLayout()

        self.hbox.addWidget(self.joinLabel)
        self.hbox.addWidget(self.joinBtn)


        # ---------- ARRANGING THE WIDGETS --------- #
        self.vbox.addItem(spacer3)
        self.vbox.addItem(spacer2)
        self.vbox.addWidget(self.usernameInput)
        self.vbox.addWidget(self.usernameError)
        self.vbox.addLayout(self.showInputHbox)
        self.vbox.addWidget(self.passwordError)
        self.vbox.addItem(spacer2)
        self.vbox.addWidget(self.signInBtn)
        self.vbox.addItem(spacer2)
        self.vbox.addLayout(self.hbox)
        self.vbox.addItem(spacer3)

        self.setLayout(self.vbox)

        self.show()

    def onPressed(self):
        self.usernameError.setText('')
        self.passwordError.setText('')

        self.passwordInput.setStyleSheet('border-color: #68B2A0;')
        self.usernameInput.setStyleSheet('border-color: #68B2A0;')

        username = self.usernameInput.text()
        password = self.passwordInput.text()
        users = {
                'username': [],
                'password': []
                }

        # Decrypting the password
        enkPassword = list()

        for letter in password:
            enkPassword.append(ord(letter)+7)

        if username != '':
            if password != '':
                data = load()
                
                for accounts in data['users']:
                    users['username'].append(accounts['username'])
                    users['password'].append(accounts['password'])

                # 404 password or username not found!
                if username not in users['username']:
                    self.usernameError.setText("This username doesn't exists")
                    self.usernameInput.setStyleSheet('border-color: red;')
                    return False

                elif enkPassword not in users['password']:
                    self.passwordError.setText("Wrong password")
                    self.passwordInput.setStyleSheet('border-color: red;')
                    return False

                else:
                    return True

            else:
                self.passwordError.setText('Please enter a password')
                self.passwordInput.setStyleSheet('border-color: red;')

        else:
            self.usernameError.setText('Please enter a username')
            self.usernameInput.setStyleSheet('border-color: red;')

            if password == '':
                self.passwordError.setText('Please enter a password')
                self.passwordInput.setStyleSheet('border-color: red;')



    def showPassword(self):
        if self.passwordInput.echoMode() == QtWidgets.QLineEdit.Normal:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

            self.showPasswordBtn.setIcon(QtGui.QIcon('icons/show.png'))

        else:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Normal)

            self.showPasswordBtn.setIcon(QtGui.QIcon('icons/hide.png'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = SignIn()
    sys.exit(app.exec_())
