import sys
import json
from reading_data import *
from sign_in import SignIn
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Money')
        self.resize(600, 400)

        self.stacked = QtWidgets.QStackedWidget(self)

        self.sign_in = SignIn()

        self.stacked.addWidget(self.sign_in)

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
