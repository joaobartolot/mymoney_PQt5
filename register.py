import json
import sys
from reading_data import *
from PyQt5 import QtWidgets, QtGui, QtCore

class Register(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        self.vbox = QtWidgets.QVBoxLayout()

        spacer1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed)
        spacer2 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Fixed)
        spacer3 = QtWidgets.QSpacerItem(0, 80, QtWidgets.QSizePolicy.Fixed)

        # --------------- Name ---------------- #
        self.nameLabel = QtWidgets.QLabel('Name')
        self.nameInput = QtWidgets.QLineEdit()

        # -------------- USERNAME ------------- #
        self.usernameLabel = QtWidgets.QLabel('Username')
        self.usernameInput = QtWidgets.QLineEdit()
        self.usernameError = QtWidgets.QLabel('')
        self.usernameError.setObjectName('errorMensage')

        # -------------- PASSWORD ------------- #
        self.passwordLabel = QtWidgets.QLabel('Password')
        self.passwordInput = QtWidgets.QLineEdit()
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordError = QtWidgets.QLabel('')
        self.passwordError.setObjectName('errorMensage')


        self.showPasswordBtn = QtWidgets.QPushButton()
        self.showPasswordBtn.setObjectName('showPasswordBtn')

        self.showPasswordBtn.setIcon(QtGui.QIcon('icons/show.png'))
        self.showPasswordBtn.clicked.connect(self.showPassword)

        self.showErrorHBox = QtWidgets.QHBoxLayout()

        self.showErrorHBox.addWidget(self.passwordError)
        self.showErrorHBox.addWidget(self.showPasswordBtn)
        self.showErrorHBox.setAlignment(self.showPasswordBtn, QtCore.Qt.AlignRight)

        # -------------- CONFIRMATION ------------- #
        self.confirmationLabel = QtWidgets.QLabel('Confirm your password')
        self.confirmationInput = QtWidgets.QLineEdit()
        self.confirmationInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.confirmationError = QtWidgets.QLabel('')
        self.confirmationError.setObjectName('errorMensage')

        # -------------- JOIN BUTTON ----------------#
        self.joinBtn = QtWidgets.QPushButton('Join')
        self.joinBtn.setObjectName('joinBtn')
        self.joinBtn.clicked.connect(self.sign_up)

        # -------------- SIGN IN BUTTON ------------- #
        self.signInHBox = QtWidgets.QHBoxLayout()

        self.signInBtn = QtWidgets.QPushButton('Sign in')
        self.signInBtn.setObjectName('signInBtn')

        self.signInLabel = QtWidgets.QLabel('Have an account?')

        self.signInHBox.addWidget(self.signInLabel)
        self.signInHBox.addWidget(self.signInBtn)

        self.vbox.addItem(spacer1)
        self.vbox.addWidget(self.nameLabel)
        self.vbox.addWidget(self.nameInput)
        self.vbox.addItem(spacer1)
        self.vbox.addWidget(self.usernameLabel)
        self.vbox.addWidget(self.usernameInput)
        self.vbox.addWidget(self.usernameError)
        self.vbox.addWidget(self.passwordLabel)
        self.vbox.addWidget(self.passwordInput)
        self.vbox.addLayout(self.showErrorHBox)
        self.vbox.addWidget(self.confirmationLabel)
        self.vbox.addWidget(self.confirmationInput)
        self.vbox.addWidget(self.confirmationError)
        self.vbox.addItem(spacer1)
        self.vbox.addWidget(self.joinBtn)
        self.vbox.addItem(spacer2)
        self.vbox.addLayout(self.signInHBox)
        self.vbox.addItem(spacer2)
 
        self.setLayout(self.vbox)

        self.show()

    def sign_up(self):
        self.usernameError.setText('')
        self.passwordError.setText('')
        self.confirmationError.setText('')

        name = self.nameInput.text()
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        confirmation = self.confirmationInput.text()
        usernamesDB = list()


        enkPassword = list()

        for letter in self.passwordInput.text():
            enkPassword.append(ord(letter)+7)


        if username != '':
            if password != '':
                data = load()

                if data['users'] == []:
                    # checking if the password and the confirmation is the same
                    if password == confirmation:
                        register(name, username, enkPassword)
                    else: self.confirmatioError.setText('Check your confirmation')

                else:
                    for accounts in data['users']:
                        # adding the usernames to a list
                        usernamesDB.append(accounts[1])

                    # checking if the username already exists in the database
                    if username not in usernamesDB:
                        # checking if the password and the confirmation is the same
                        if password == confirmation:
                            register(name, username, enkPassword)
                        else: self.confirmationError.setText('Check your confirmation')

                    else:
                        self.usernameError.setText('Username already exists')

                        if password != confirmation:
                            self.confirmationError.setText('Check your confirmation')
            else:
                self.passwordError.setText('You have to put a password')
        else:
            self.usernameError.setText('You have to put a username')
            if password == '':
                self.passwordError.setText('You have to put a password')

    def showPassword(self):
        if self.passwordInput.echoMode() == QtWidgets.QLineEdit.Normal:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.confirmationInput.setEchoMode(QtWidgets.QLineEdit.Password)

            self.showPasswordBtn.setIcon(QtGui.QIcon('icons/show.png'))

        else:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.confirmationInput.setEchoMode(QtWidgets.QLineEdit.Normal)

            self.showPasswordBtn.setIcon(QtGui.QIcon('icons/hide.png'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    register = Resgister()
    sys.exit(app.exec_())
