# Ressources

# Imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as Wid
from FirstTab import FirstTab
from SecondTab import SecondTab
from ThirdTab import ThirdTab


# create a class Main_Window which inherits from QtWidgets.QmainWindow to be able to use menus, status bar etc.
class Main_window(QtWidgets.QMainWindow):
    """Main Window"""

    def __init__(self, parent=None):
        """Initializer"""
        super(Main_window, self).__init__(parent)
        self.setGeometry(50, 50, 1100, 750)
        self.setWindowTitle("Extractive and abstractive text summarization in Python")

        # sets the tabWidget as the central widget inside the QMainWindow
        self.tabWidget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabWidget)

        self.firstTab = FirstTab()
        self.tabWidget.addTab(self.firstTab, "Tab 1")
        self.secondTab = SecondTab()
        self.tabWidget.addTab(self.secondTab, "Tab 2")
        self.thirdTab = ThirdTab()
        self.tabWidget.addTab(self.thirdTab, "Tab 3")

        self.firstTab.line.textChanged.connect(self.secondTab.editor.setPlainText)
        self.firstTab.btn.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.secondTab))
        self.tabWidget.currentChanged.connect(self.current_tab_changed)

        self.updateLine()

        # Menu for the application
        self.qtMenu()

        # Status bar
        self.statusBar().showMessage("Message in the statusbar")

    def current_tab_changed(self):
        pass

    def updateLine(self):
        self.firstTab.line.insert("hi")

        self.thirdTab.textEdit_import.setPlainText("Test 0815")
        self.thirdTab.textEdit_source.setPlainText("Test source")


    # working :)
    # self.thirdTab.source.setPlainText("nice :)")

    # working
    # self.thirdTab.groupbox_import.setTitle("new titel for groupbox")

    def qtMenu(self):
        # creating a file menu
        file_menu = self.menuBar().addMenu("&File")
        # creating actions to add in the file menu i.e. creating a 'open file' action
        open_file_action = QAction("Open file",self)
        # setting status tip
        open_file_action.setStatusTip("Open file")
        # adding an action to the open file
        open_file_action.triggered.connect(self.file_open)
        # adding this to the file menu
        file_menu.addAction(open_file_action)

    # action called by file open action
    def file_open(self):

        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Text documents (*.txt);All files (*.*)")

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
                print(text)
                self.thirdTab.textEdit_source.setPlainText(text)

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


def main():
    """Main loop for the application"""
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = Main_window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
