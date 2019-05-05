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
        self.usernameLabel = QtWidgets.QLabel('Username')
        self.usernameLabel.setAlignment(QtCore.Qt.AlignBottom)

        self.usernameInput = QtWidgets.QLineEdit()

        self.usernameError = QtWidgets.QLabel()
        self.usernameError.setObjectName('errorMensage')

        # --------------- PASSWORD ---------------#
        self.passwordLabel = QtWidgets.QLabel('Password')
        self.passwordLabel.setAlignment(QtCore.Qt.AlignBottom)

        self.passwordInput = QtWidgets.QLineEdit()
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.passwordError = QtWidgets.QLabel()
        self.passwordError.setObjectName('errorMensage')


        self.showPasswordBtn = QtWidgets.QPushButton()
        self.showPasswordBtn.setObjectName('showPasswordBtn')

        self.showPasswordBtn.setIcon(QtGui.QIcon('icons/show.png'))
        self.showPasswordBtn.clicked.connect(self.showPassword)

        self.showErrorHBox = QtWidgets.QHBoxLayout()

        self.showErrorHBox.addWidget(self.passwordError)
        self.showErrorHBox.addWidget(self.showPasswordBtn)
        self.showErrorHBox.setAlignment(self.showPasswordBtn, QtCore.Qt.AlignRight)

        # ------------ ENTER BUTTON --------------#
        self.signInBtn = QtWidgets.QPushButton('Sign in')
        self.signInBtn.setObjectName('signInBtn')
        self.signInBtn.clicked.connect(self.onPressed)

        # ------------ JOIN BUTTON  --------------#
        self.joinBtn = QtWidgets.QPushButton('Join us')
        self.joinBtn.setObjectName('joinBtn')

        self.joinLabel = QtWidgets.QLabel('New here? ')
        self.joinLabel.setAlignment(QtCore.Qt.AlignRight)

        self.hbox = QtWidgets.QHBoxLayout()

        self.hbox.addWidget(self.joinLabel)
        self.hbox.addWidget(self.joinBtn)

        self.vbox.addItem(spacer3)
        self.vbox.addWidget(self.usernameLabel)
        self.vbox.addWidget(self.usernameInput)
        self.vbox.addWidget(self.usernameError)
        self.vbox.addWidget(self.passwordLabel)
        self.vbox.addWidget(self.passwordInput)
        self.vbox.addLayout(self.showErrorHBox)
        self.vbox.addWidget(self.signInBtn)
        self.vbox.addItem(spacer2)
        self.vbox.addLayout(self.hbox)
        self.vbox.addItem(spacer3)

        self.setLayout(self.vbox)

        self.show()

    def onPressed(self):
        self.usernameError.setText('')
        self.passwordError.setText('')

        username = self.usernameInput.text()
        password = self.passwordInput.text()
        users = list()

        enkPassword = list()

        for letter in password:
            enkPassword.append(ord(letter)+7)

        if username != '':
            if password != '':
                data = load()
                
                for account in data['users']:
                    users.append((account[1], account[2]))

                if (username, enkPassword) not in users:
                    print('nem tenta')
                else:
                    print('pode entrar')

            else: self.passwordError.setText('Please enter a password')

        else:
            self.usernameError.setText('Please enter a username')
            if password == '':
                self.passwordError.setText('Please enter a password')



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
