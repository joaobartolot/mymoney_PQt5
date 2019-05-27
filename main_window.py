import sys
import json
from reading_data import *
from sign_in import SignIn
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.vbox = QtWidgets.QVBoxLayout()

        # ----------------- BALANCE ----------------- #

        self.balanceLayout = QtWidgets.QHBoxLayout()

        self.balanceLabel = QtWidgets.QLabel('Balance:')

        self.balanceValue = QtWidgets.QLabel('R$ 0,00')

        self.balanceLayout.addWidget(self.balanceLabel)
        self.balanceLayout.addWidget(self.balanceValue)


        # ----------------- OPTIONS ----------------- #

        self.navbar = QtWidgets.QHBoxLayout()

        self.accountBtn = QtWidgets.QPushButton()
        self.accountBtn.setObjectName('navbarIconProfile')

        self.btn1 = QtWidgets.QPushButton()
        self.btn1.setObjectName('navbarIcon')


        self.btn2 = QtWidgets.QPushButton()
        self.btn2.setObjectName('navbarIcon')


        self.btn3 = QtWidgets.QPushButton()
        self.btn3.setObjectName('navbarIcon')


        self.btn4 = QtWidgets.QPushButton()
        self.btn4.setObjectName('navbarIcon')

        self.navbar.addWidget(self.accountBtn)
        self.navbar.addWidget(self.btn1)
        self.navbar.addWidget(self.btn2)
        self.navbar.addWidget(self.btn3)
        self.navbar.addWidget(self.btn4)


        # --------------- ARRANGING --------------- #
        self.vbox.addLayout(self.balanceLayout)
        self.vbox.addLayout(self.navbar)

        self.setLayout(self.vbox)


        self.show()


class Account(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
