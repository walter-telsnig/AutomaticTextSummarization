# Imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from SecondTab import *

class FirstTab(QDialog):
    def __init__(self):
        super().__init__()
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)
        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
        self.btn=QPushButton('switch',self)
        self.btn.move(80, 50)
        self.btn.clicked.connect(lambda: SecondTab.display(SecondTab(),self.nameLabel.text()))