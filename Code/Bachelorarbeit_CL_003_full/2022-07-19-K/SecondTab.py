# Imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *


class SecondTab(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.editor = QTextEdit()
        self.layout.addWidget(self.editor)
        self.setLayout(self.layout)

    def display(self, text):
        self.editor.setText(text)