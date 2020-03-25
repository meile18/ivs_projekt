import sys
from PyQt5.QtWidgets import QPushButton, QToolButton, QLabel
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self)  # Load the .ui file

# testovanie vypisu po kliknuti sum
        self.button = self.findChild(QtWidgets.QPushButton, 'sum')
        self.button.clicked.connect(self.printButtonSum)
####
        self.show()                 # Show the GUI

# testovanie vypisu
    def printButtonSum(self):
        print("ahoj")
####

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
