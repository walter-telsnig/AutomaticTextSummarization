from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTextEdit, QMessageBox
from helper import *

class FourthTab(QWidget):

    def __init__(self):
        super().__init__()

        #self.source = QTextEdit(self)
        #self.source.move(80, 20)
        #self.source.resize(200, 32)
        #self.nameLabel.move(20, 20)

        self.layout = QGridLayout()

        # Groupbox Import
        self.groupbox_import = QGroupBox("Import")
        self.layout.addWidget(self.groupbox_import,0,0)

        # Groupbox Log
        self.groupbox_log = QGroupBox("Log")
        self.layout.addWidget(self.groupbox_log,1,0)

        # Groupbox Source (source text and summary text)
        self.groupbox_source = QGroupBox("Source")
        self.layout.addWidget(self.groupbox_source,0,1,-1,1)

        self.textEdit_import = QTextEdit()
        self.textEdit_log = QTextEdit()
        self.textEdit_source = QTextEdit()
        self.textedit_summary = QTextEdit()

        # creating 2 Labels and 2 QlineEdits for path to source file and possible output file
        self.importLabel = QLabel(self)
        self.importLabel.setText('Import file:')
        self.import_reference = QLineEdit()
        self.exportLabel = QLabel(self)
        self.exportLabel.setText('Export file:')
        self.export_reference = QLineEdit()

        # creating buttons for (1) import/log and (2) summarizer steps
        self.btn_import_file = QPushButton("Import")
        self.btn_export_file = QPushButton("Export")
        self.import_btn_summarize = QPushButton("Summarize")
        self.import_btn_step1 = QPushButton("Step 1")
        self.import_btn_step2 = QPushButton("Step 2")
        self.import_btn_step3 = QPushButton("Step 3")
        self.import_btn_step4 = QPushButton("Step 4")
        self.import_spacer = QSpacerItem(20, 40)

        # groupbox Import
        self.grid_import = QGridLayout()
        self.grid_import.addWidget(self.importLabel,0,0)
        self.grid_import.addWidget(self.import_reference,0,1,1,3)
        self.grid_import.addWidget(self.btn_import_file,0,4)
        self.grid_import.addWidget(self.exportLabel,1,0)
        self.grid_import.addWidget(self.export_reference,1,1,1,3)
        self.grid_import.addWidget(self.btn_export_file,1,4)
        self.grid_import.addItem(self.import_spacer)

        # Buttons
        self.grid_import.addWidget(self.import_btn_summarize,3,3,1,-1)
        self.grid_import.addWidget(self.import_btn_step1, 4, 1)
        self.grid_import.addWidget(self.import_btn_step2, 4, 2)
        self.grid_import.addWidget(self.import_btn_step3, 4, 3)
        self.grid_import.addWidget(self.import_btn_step4, 4, 4)

        #self.grid_import.addWidget(self.textEdit_import,1,0)
        self.groupbox_import.setLayout(self.grid_import)

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
        # self.btn_import_file.clicked.connect(self.greeting)  # connect button Import to greeting

        # Button Signal/Slot for Luhn
        # self.btn_import_file.clicked.connect(lambda: self.file_open())
        # self.btn_import_file.clicked.connect(lambda: self.textEdit_source.setPlainText(self.raw_text_input))


        self.btn_import_file.clicked.connect(lambda: self.textEdit_source.setPlainText(file_open_return_helper(self)[0]))
        #self.btn_import_file.clicked.connect(lambda: self.import_reference.setText(file_open_return_helper(self)[1]))
        # Todo: file_open_return_helper returns the text and the path to the text, can only catch one
        self.btn_import_file.clicked.connect(lambda: self.import_reference.setText("here should be the path to the file"))

    # only for testing program flow
    def greeting(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message Box")
        msg.setText("This is the message text")
        x = msg.exec()

    # Todo: remove? not needed anymore because it's in class helper
    def file_open_return(self):

        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "","Text documents (*.txt);All files (*.*)")

        # if path is true
        if path:
            # try opening path
            try:
                with open(path) as f:
                    # read the file
                    text = f.read()

            # if some error occurred
            except Exception as e:
                pass
            # else
            else:
                return(text)
