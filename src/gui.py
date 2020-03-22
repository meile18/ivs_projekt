import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import PyQt5.QtWidgets

app = QtWidgets.QApplication([])
win = uic.loadUi("gui.ui")

win.show()

sys.exit(app.exec())
