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

        # --------------- NAME ---------------- #
        self.nameInput = QtWidgets.QLineEdit()
        self.nameInput.setPlaceholderText('Name')
        self.nameInput.setObjectName('userInput')
        self.nameError = QtWidgets.QLabel('')
        self.nameError.setObjectName('errorMessage')

        # -------------- USERNAME ------------- #
        self.usernameInput = QtWidgets.QLineEdit()
        self.usernameInput.setPlaceholderText('Username')
        self.usernameInput.setObjectName('userInput')
        self.usernameError = QtWidgets.QLabel('')
        self.usernameError.setObjectName('errorMessage')

        # -------------- PASSWORD ------------- #
        self.passwordInput = QtWidgets.QLineEdit()
        self.passwordInput.setPlaceholderText('Password')
        self.passwordInput.setObjectName('userInput')
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordError = QtWidgets.QLabel('')
        self.passwordError.setObjectName('errorMessage')


        self.showPasswordBtn = QtWidgets.QPushButton()
        self.showPasswordBtn.setObjectName('showPasswordBtn')

        self.showPasswordBtn.setIcon(QtGui.QIcon('icons/show.png'))
        self.showPasswordBtn.clicked.connect(self.showPassword)

        self.showErrorHBox = QtWidgets.QHBoxLayout()

        self.showErrorHBox.addWidget(self.passwordError)
        self.showErrorHBox.addWidget(self.showPasswordBtn)
        self.showErrorHBox.setAlignment(self.showPasswordBtn, QtCore.Qt.AlignRight)


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


        # ---------- ARRANGING THE WIDGETS --------- #
        self.vbox.addItem(spacer3)
        self.vbox.addItem(spacer2)
        self.vbox.addWidget(self.nameInput)
        self.vbox.addWidget(self.nameError)
        self.vbox.addWidget(self.usernameInput)
        self.vbox.addWidget(self.usernameError)
        self.vbox.addWidget(self.passwordInput)
        self.vbox.addLayout(self.showErrorHBox)
        self.vbox.addItem(spacer2)
        self.vbox.addWidget(self.joinBtn)
        self.vbox.addItem(spacer2)
        self.vbox.addLayout(self.signInHBox)
        self.vbox.addItem(spacer2)
        self.vbox.addItem(spacer3)
 
        self.setLayout(self.vbox)

        self.show()

    # Function to create the user in database
    def sign_up(self):
        self.usernameError.setText('')
        self.passwordError.setText('')

        self.nameInput.setStyleSheet('border-color: #68B2A0;')
        self.usernameInput.setStyleSheet('border-color: #68B2A0;')
        self.passwordInput.setStyleSheet('border-color: #68B2A0;')

        name = self.nameInput.text()
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        # List to the usernames
        usernamesDB = list()


        # Encrypting the password
        enkPassword = list()

        for letter in self.passwordInput.text():
            enkPassword.append(ord(letter)+7)


        if name != '':
            if username != '':
                if password != '':
                    data = load()

                    if data['users'] == []:
                        register(name, username, enkPassword)

                    else:
                        for accounts in data['users']:
                            # Adding the usernames to a list
                            usernamesDB.append(accounts['username'])

                        # Checking if the username already exists in the database
                        if username not in usernamesDB:
                            register(name, username, enkPassword)

                        else:
                            self.usernameError.setText('Username already exists')
                            self.usernameInput.setStyleSheet('border-color: red;')

                else:
                    self.passwordError.setText('You have to put a password')
                    self.passwordInput.setStyleSheet('border-color: red;')

            else:
                self.usernameError.setText('You have to put a username')
                self.usernameInput.setStyleSheet('border-color: red;')

                if password == '':
                    self.passwordError.setText('You have to put a password')
                    self.passwordInput.setStyleSheet('border-color: red;')
        else:
            self.nameInput.setStyleSheet('border-color: red;')
            self.nameError.setText('You have to put a name')

            if username == '':
                self.usernameInput.setStyleSheet('border-color: red;')
                self.usernameError.setText('You have to put a username')

            if password == '':
                self.passwordInput.setStyleSheet('border-color: red;')
                self.passwordError.setText('You have to put a password')

    # Changing the show-hide password button
    # and changing the stage of the QLineEdit
    def showPassword(self):
        if self.passwordInput.echoMode() == QtWidgets.QLineEdit.Normal:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

            self.showPasswordBtn.setIcon(QtGui.QIcon('icons/show.png'))

        else:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Normal)

            self.showPasswordBtn.setIcon(QtGui.QIcon('icons/hide.png'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    register = Resgister()
    sys.exit(app.exec_())
