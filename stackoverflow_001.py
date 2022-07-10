import sys
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    # window object
    def __init__(self):
       super().__init__()
       self.initGUI() # call custom code

    def initGUI(self):
       self.setWindowTitle("Window With Tabs") # window...
       self.setGeometry(50,50,400,400)         #...properties
       TabW=self.createTabs()                  # a custom-tab object
       layout = QVBoxLayout(self)              # main window layout
       layout.addWidget(TabW)                  #populate layout with Tab object


       self.show()                             # display window

    def createTabs(self):            # create and return Tab object
       oPage1 = QWidget()            # tabs...
       oPage2 = QWidget()
       oPage3 = QWidget()

       oTabWidget = QTabWidget()    # Tabobject

       oTabWidget.addTab(FirstTab(),"Page1") # populate tab object...
       oTabWidget.addTab(oPage2,"Page2")
       oTabWidget.addTab(oPage3,"Page3")

       return   oTabWidget              # return tab object

class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        name = QLabel('Name:')
        nameedit = QLineEdit()
        age = QLabel('Age:')
        ageedit = QLineEdit()
        nation = QLabel('Nation:')
        nationedit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameedit)
        vbox.addWidget(age)
        vbox.addWidget(ageedit)
        vbox.addWidget(nation)
        vbox.addWidget(nationedit)
        vbox.addStretch()

        self.setLayout(vbox)

if __name__ == "__main__":             # Rest is History!

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())