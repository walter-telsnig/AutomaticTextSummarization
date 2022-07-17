from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTextEdit


class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()
        #self.nameLabel = QLabel(self)
        #self.nameLabel.setText('Name:')
        #self.source = QTextEdit(self)
        #self.source.move(80, 20)
        #self.source.resize(200, 32)
        #self.nameLabel.move(20, 20)

        self.layout = QGridLayout()
        self.groupbox_import = QGroupBox("Import")
        self.layout.addWidget(self.groupbox_import,0,0)
        self.groupbox_log = QGroupBox("Log")
        self.layout.addWidget(self.groupbox_log,1,0)
        self.groupbox_source = QGroupBox("Source")
        self.layout.addWidget(self.groupbox_source,0,1,-1,1)

        self.textEdit_import = QTextEdit()
        self.textEdit_log = QTextEdit()
        self.textEdit_source = QTextEdit()
        self.textedit_summary = QTextEdit()

        # groupbox Import
        self.vbox_import = QVBoxLayout()
        self.vbox_import.addWidget(self.textEdit_import)
        self.groupbox_import.setLayout(self.vbox_import)

        # groupbox Log
        self.vbox_log = QVBoxLayout()
        self.vbox_log.addWidget(self.textEdit_log)
        self.groupbox_log.setLayout(self.vbox_log)

        # groupbox Source
        self.vbox_source = QVBoxLayout()
        self.vbox_source.addWidget(self.textEdit_source)
        self.vbox_source.addWidget(self.textedit_summary)
        self.groupbox_source.setLayout(self.vbox_source)





        self.setLayout(self.layout)