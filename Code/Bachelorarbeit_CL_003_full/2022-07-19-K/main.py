# Ressources

# Imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as Wid

import Luhn_summarizer_001
import NLTK_summarizer_001
from FirstTab import FirstTab
from SecondTab import SecondTab
from ThirdTab import ThirdTab
from FourthTab import FourthTab
from Luhn_summarizer_001 import *
from NLTK_summarizer_001 import *
from helper import *


# create a class Main_Window which inherits from QtWidgets.QmainWindow to be able to use menus, status bar etc.
class Main_window(QtWidgets.QMainWindow):
    """Main Window"""

    def __init__(self, parent=None):
        """Initializer"""
        super(Main_window, self).__init__(parent)
        self.setGeometry(50, 50, 1100, 750)
        self.setWindowTitle("Extractive and abstractive text summarization in Python")

        self.contents = "This is all there is. Not much to summarize, sorry mate."
        self.article = "This is !!# sentence 1. This is Ö sentence 2"
        self.raw_text_input = ""  # raw_text_input holds the input from the read() functions
        self.output_method = []

        self.qtMenu()  # menu for the application
        self.statusBar().showMessage("Message in the statusbar")  # status bar for the application

        # sets the tabWidget as the central widget inside the QMainWindow
        self.tabWidget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabWidget)

        # ToDo Renaming - this will get messy > self.thirdTab = FourthTab()
        self.firstTab = FirstTab()
        self.tabWidget.addTab(self.firstTab, "Tab 1")
        self.secondTab = SecondTab()
        self.tabWidget.addTab(self.secondTab, "Tab 2")
        self.thirdTab = FourthTab()
        self.tabWidget.addTab(self.thirdTab, "NLTK summarization")
        self.fourthTab = FourthTab()
        self.tabWidget.addTab(self.fourthTab, "Luhn summarization")
        self.fifthTab = FourthTab()
        self.tabWidget.addTab(self.fifthTab, "TD-IDF")
        self.sixthTab = FourthTab()
        self.tabWidget.addTab(self.sixthTab, "Page Rank")
        self.seventhTab = FourthTab()
        self.tabWidget.addTab(self.seventhTab, "KL Divergence")

        # Design guideline
        # Button functions like load text, store text, reset belong into the TabClass e.g. FourthTab()
        # Functions regarding the summarization algorithm belong into the main class because here the
        # tab is used to create a summarizer

        self.firstTab.line.textChanged.connect(self.secondTab.editor.setPlainText)
        self.firstTab.btn.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.secondTab))
        self.tabWidget.currentChanged.connect(self.current_tab_changed)

        # NLTK summarizer (not a real summarizer but to test)
        self.thirdTab.import_btn_summarize.clicked.connect(lambda: self.use_NLTK_summarizer())
        self.thirdTab.import_btn_step1.clicked.connect(lambda: print("none"))
        self.thirdTab.import_btn_step2.clicked.connect(lambda: print("none"))
        self.thirdTab.import_btn_step3.clicked.connect(lambda: print("none"))
        self.thirdTab.import_btn_step4.clicked.connect(lambda: self.thirdTab.textEdit_log.setPlainText("no function set yet, sorry mate :("))


        # Luhn summarizer
        self.fourthTab.import_btn_summarize.clicked.connect(lambda: self.use_Luhn_summarizer(0))
        self.fourthTab.import_btn_step1.clicked.connect(lambda: self.use_Luhn_summarizer(1))
        self.fourthTab.import_btn_step2.clicked.connect(lambda: self.use_Luhn_summarizer(2))
        self.fourthTab.import_btn_step3.clicked.connect(lambda: self.use_Luhn_summarizer(3))
        self.fourthTab.import_btn_step4.clicked.connect(lambda: self.fourthTab.textEdit_log.setPlainText("no function set yet, sorry mate :("))


    def current_tab_changed(self):
        pass

    def updateLine(self):
        self.firstTab.line.insert("hi")

        self.thirdTab.textEdit_import.setPlainText("Test 0815")
        self.thirdTab.textEdit_source.setPlainText("Test source")

    def hello_to_you(self, name):
        print("Hello " + name)

    def qtMenu(self):
        # creating a file menu
        file_menu = self.menuBar().addMenu("&File")
        # creating actions to add in the file menu i.e. creating a 'open file' action
        open_file_action = QAction("Open file", self)
        # setting status tip
        open_file_action.setStatusTip("Open file")
        # adding an action to the open file
        open_file_action.triggered.connect(self.file_open)
        # adding this to the file menu
        file_menu.addAction(open_file_action)

        # adding new open generic for test
        # ToDo generic file_open which takes into account which is the active tab
        # open_file_action = QAction("Open file generic with tab reference",self)
        # open_file_action.setStatusTip("file_open_generic")
        # open_file_action.triggered.connect(self.file_open_generic,"test")
        # file_menu.addAction(open_file_action)

        # File menu NLTK summarizer
        open_file_action = QAction("NLTK summarizer", self)
        open_file_action.setStatusTip("NLTK summarizer")
        open_file_action.triggered.connect(self.use_NLTK_summarizer)
        file_menu.addAction(open_file_action)

    # action called by file open action
    def file_open(self):

        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        # if path is true
        if path:
            # try opening path
            try:
                with open(path) as f:
                    # read the file
                    text = f.read()

            # if some error occurred
            except Exception as e:

                # show error using critical method
                self.dialog_critical(str(e))
            # else
            else:
                # update path value
                # self.path = path

                # update the text
                # print(text)
                self.raw_text_input = text
                # self.thirdTab.textEdit_source.setPlainText(text)

                # update the title
                # self.update_title()

        # creating dialog critical method
        # to show errors
        def dialog_critical(self, s):

            # creating a QMessageBox object
            dlg = QMessageBox(self)

            # setting text to the dlg
            dlg.setText(s)

            # setting icon to it
            dlg.setIcon(QMessageBox.Critical)

            # showing it
            dlg.show()

    def get_indices(self):
        index = self.tabWidget.currentIndex()
        print(index)

    def file_open_generic(self, tab_reference):
        self.tab_reference = tab_reference

        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        # if path is true
        if path:
            # try opening path
            try:
                with open(path) as f:
                    # read the file
                    text = f.read()

            # if some error occurred
            except Exception as e:

                # show error using critical method
                self.dialog_critical(str(e))
            # else
            else:
                # update path value
                # self.path = path

                # update the text
                print(self.tab_reference)
                # self.thirdTab.textEdit_source.setPlainText(text)

        # creating dialog critical method
        # to show errors
        def dialog_critical(self, s):

            # creating a QMessageBox object
            dlg = QMessageBox(self)

            # setting text to the dlg
            dlg.setText(s)

            # setting icon to it
            dlg.setIcon(QMessageBox.Critical)

            # showing it
            dlg.show()

    def file_open_return(self):

        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

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
                return (text)

    def use_NLTK_summarizer(self):
        raw_text = self.thirdTab.textEdit_source.toPlainText()
        final_text = NLTK_summarizer_001.nltk_summarizer(raw_text)
        # final_text = NLTK_summarizer_001.hello_NLTK(raw_text)
        self.thirdTab.textedit_summary.setPlainText(final_text)
        # print(final_text)

    def use_Luhn_summarizer(self, int):
        case = int
        raw_text = self.fourthTab.textEdit_source.toPlainText()
        max_words = self.fourthTab.max_words.text()
        summary = Luhn_summarizer_001.main(raw_text, max_words)[0]
        luhn_word_tokenize = Luhn_summarizer_001.main(raw_text, max_words)[1]
        luhn_sentence_tokenize = Luhn_summarizer_001.main(raw_text, max_words)[2]
        luhn_sentence_score = Luhn_summarizer_001.main(raw_text, max_words)[3]

        if case == 0: # Case 0: get summary and set summary to textedit_summary
            self.fourthTab.textedit_summary.setPlainText(summary)

        elif case == 1: # Case 1: get word_tokenize and output to textedit_log
            self.fourthTab.textEdit_log.setPlainText(luhn_word_tokenize)

        elif case == 2: # Case 2: get sentence_tokenize and output to textedit_log
            self.fourthTab.textEdit_log.setPlainText(luhn_sentence_tokenize)

        elif case == 3: # Case 3: sentence_score
            sentence_score = str(luhn_sentence_score)
            self.fourthTab.textEdit_log.setHtml(sentence_score)

        else:
            print("sorry mate no further else-case defined")

    # Todo: remove? not needed anymore because dealt with in the class Luhn_summarizer_001
    def use_Luhn_summarizer_stepClean(self):
        raw_text = self.fourthTab.textEdit_source.toPlainText()
        cleaned_text = Luhn_summarizer_001.clean(raw_text)
        self.fourthTab.textEdit_log.setPlainText(cleaned_text)


def main():
    """Main loop for the application"""
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = Main_window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
