import sys
import json
from reading_data import *
from sign_in import SignIn
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Money')
        self.setFixedSize(600, 400)

        self.vbox = QtWidgets.QVBoxLayout()

        # ----------------- BALANCE ----------------- #

        self.balanceLayout = QtWidgets.QHBoxLayout()

        self.balanceLabel = QtWidgets.QLabel('Balance:')

        self.balanceValue = QtWidgets.QLabel('R$ 0,00')

        self.balanceLayout.addWidget(self.balanceLabel)
        self.balanceLayout.addWidget(self.balanceValue)


        # ----------------- OPTIONS ----------------- #

        self.optionLayout = QtWidgets.QVBoxLayout()

        self.firstRow = QtWidgets.QHBoxLayout()

        self.accountBtn = QtWidgets.QPushButton('Account')


        self.firstRow.addWidget(self.accountBtn)


        self.optionLayout.addLayout(self.firstRow)


        # --------------- ARRANGING --------------- #
        self.vbox.addLayout(self.balanceLayout)
        self.vbox.addLayout(self.optionLayout)

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
