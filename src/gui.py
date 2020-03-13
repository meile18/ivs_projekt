# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 582)
        MainWindow.setMinimumSize(QtCore.QSize(411, 582))
        MainWindow.setMaximumSize(QtCore.QSize(1169, 717))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("background-color: rgb(25, 23, 23);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # label
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("QLabel {\n"
                                 "  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
                                 "  border: none;\n"
                                 "}\n"
                                 "\n"
                                 "background-color : white;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)

        # num 0
        self.num_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_0.sizePolicy().hasHeightForWidth())
        self.num_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_0.setFont(font)
        self.num_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_0.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_0.setObjectName("num_0")
        self.num_group.addButton(self.num_0)
        self.gridLayout.addWidget(self.num_0, 5, 0, 1, 2)

        # num 1
        self.num_1 = QtWidgets.QPushButton(self.centralwidget)
        self.num_1.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_1.setFont(font)
        self.num_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_1.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_1.setObjectName("num_1")
        self.num_group.addButton(self.num_1)
        self.gridLayout.addWidget(self.num_1, 4, 0, 1, 1)

        # num 2
        self.num_2 = QtWidgets.QPushButton(self.centralwidget)
        self.num_2.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_2.setFont(font)
        self.num_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_2.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_2.setObjectName("num_2")
        self.num_group.addButton(self.num_2)
        self.gridLayout.addWidget(self.num_2, 4, 1, 1, 1)

        # num 3
        self.num_3 = QtWidgets.QPushButton(self.centralwidget)
        self.num_3.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_3.setFont(font)
        self.num_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_3.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_3.setObjectName("num_3")
        self.num_group.addButton(self.num_3)
        self.gridLayout.addWidget(self.num_3, 4, 2, 1, 1)

        # num 4
        self.num_4 = QtWidgets.QPushButton(self.centralwidget)
        self.num_4.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_4.setFont(font)
        self.num_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_4.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_4.setObjectName("num_4")
        self.num_group.addButton(self.num_4)
        self.gridLayout.addWidget(self.num_4, 3, 0, 1, 1)

        # num 5
        self.num_5 = QtWidgets.QPushButton(self.centralwidget)
        self.num_5.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_5.setFont(font)
        self.num_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_5.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_5.setObjectName("num_5")
        self.num_group.addButton(self.num_5)
        self.gridLayout.addWidget(self.num_5, 3, 1, 1, 1)

        # num 6
        self.num_6 = QtWidgets.QPushButton(self.centralwidget)
        self.num_6.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_6.setFont(font)
        self.num_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_6.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_6.setObjectName("num_6")
        self.num_group.addButton(self.num_6)
        self.gridLayout.addWidget(self.num_6, 3, 2, 1, 1)

        # num 7
        self.num_7 = QtWidgets.QPushButton(self.centralwidget)
        self.num_7.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_7.setFont(font)
        self.num_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_7.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_7.setObjectName("num_7")
        self.num_group = QtWidgets.QButtonGroup(MainWindow)
        self.num_group.setObjectName("num_group")
        self.num_group.addButton(self.num_7)
        self.gridLayout.addWidget(self.num_7, 2, 0, 1, 1)

        # num 8
        self.num_8 = QtWidgets.QPushButton(self.centralwidget)
        self.num_8.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_8.setFont(font)
        self.num_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_8.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_8.setObjectName("num_8")
        self.num_group.addButton(self.num_8)
        self.gridLayout.addWidget(self.num_8, 2, 1, 1, 1)

        # num 9
        self.num_9 = QtWidgets.QPushButton(self.centralwidget)
        self.num_9.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.num_9.setFont(font)
        self.num_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.num_9.setStyleSheet("QPushButton {\n"
                                 "  background-color:  rgb(25, 23, 23);\n"
                                 "  color:  rgb(211, 215, 207); \n"
                                 "    border-radius: 35px;\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                                 "}")
        self.num_9.setObjectName("num_9")
        self.num_group.addButton(self.num_9)
        self.gridLayout.addWidget(self.num_9, 2, 2, 1, 1)

        # ac
        self.ac = QtWidgets.QPushButton(self.centralwidget)
        self.ac.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ac.setFont(font)
        self.ac.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ac.setStyleSheet("QPushButton {\n"
                              "  background-color:  rgb(64, 64, 64);\n"
                              "  color:  rgb(211, 215, 207); \n"
                              "    border-radius: 35px;\n"
                              "  border: 1px solid gray;\n"
                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                              "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                              "}")
        self.ac.setObjectName("ac")
        self.operator_group.addButton(self.ac)
        self.gridLayout.addWidget(self.ac, 1, 4, 1, 1)

        # ce
        self.ce = QtWidgets.QPushButton(self.centralwidget)
        self.ce.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ce.setFont(font)
        self.ce.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ce.setStyleSheet("QPushButton {\n"
                              "  background-color:  rgb(64, 64, 64);\n"
                              "  color:  rgb(211, 215, 207); \n"
                              "    border-radius: 35px;\n"
                              "  border: 1px solid gray;\n"
                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                              "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                              "}")
        self.ce.setObjectName("ce")
        self.operator_group.addButton(self.ce)
        self.gridLayout.addWidget(self.ce, 2, 4, 1, 1)

        # mul
        self.mul = QtWidgets.QPushButton(self.centralwidget)
        self.mul.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mul.setFont(font)
        self.mul.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mul.setStyleSheet("QPushButton {\n"
                               "  background-color:  rgb(64, 64, 64);\n"
                               "  color:  rgb(211, 215, 207); \n"
                               "    border-radius: 35px;\n"
                               "  border: 1px solid gray;\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                               "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                               "}")
        self.mul.setObjectName("mul")
        self.operator_group.addButton(self.mul)
        self.gridLayout.addWidget(self.mul, 3, 3, 1, 1)

        # modulo
        self.modulo = QtWidgets.QPushButton(self.centralwidget)
        self.modulo.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.modulo.setFont(font)
        self.modulo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.modulo.setStyleSheet("QPushButton {\n"
                                  "  background-color:  rgb(64, 64, 64);\n"
                                  "  color:  rgb(211, 215, 207); \n"
                                  "    border-radius: 35px;\n"
                                  "  border: 1px solid gray;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                  "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                                  "}")
        self.modulo.setObjectName("modulo")
        self.operator_group = QtWidgets.QButtonGroup(MainWindow)
        self.operator_group.setObjectName("operator_group")
        self.operator_group.addButton(self.modulo)
        self.gridLayout.addWidget(self.modulo, 1, 0, 1, 1)

        # sqrt
        self.sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.sqrt.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sqrt.setFont(font)
        self.sqrt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sqrt.setStyleSheet("QPushButton {\n"
                                "  background-color:  rgb(64, 64, 64);\n"
                                "  color:  rgb(211, 215, 207); \n"
                                "    border-radius: 35px;\n"
                                "  border: 1px solid gray;\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                                "}")
        self.sqrt.setObjectName("sqrt")
        self.operator_group.addButton(self.sqrt)
        self.gridLayout.addWidget(self.sqrt, 1, 1, 1, 1)

        # pow
        self.pow = QtWidgets.QPushButton(self.centralwidget)
        self.pow.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pow.setFont(font)
        self.pow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pow.setStyleSheet("QPushButton {\n"
                               "  background-color:  rgb(64, 64, 64);\n"
                               "  color:  rgb(211, 215, 207); \n"
                               "    border-radius: 35px;\n"
                               "  border: 1px solid gray;\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                               "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                               "}")
        self.pow.setObjectName("pow")
        self.operator_group.addButton(self.pow)
        self.gridLayout.addWidget(self.pow, 1, 2, 1, 1)

        # factorial
        self.factorial = QtWidgets.QPushButton(self.centralwidget)
        self.factorial.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.factorial.setFont(font)
        self.factorial.setFocusPolicy(QtCore.Qt.NoFocus)
        self.factorial.setStyleSheet("QPushButton {\n"
                                     "  background-color:  rgb(64, 64, 64);\n"
                                     "  color:  rgb(211, 215, 207); \n"
                                     "    border-radius: 35px;\n"
                                     "  border: 1px solid gray;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                                     "}")
        self.factorial.setObjectName("factorial")
        self.operator_group.addButton(self.factorial)
        self.gridLayout.addWidget(self.factorial, 1, 3, 1, 1)

        # div
        self.div = QtWidgets.QPushButton(self.centralwidget)
        self.div.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.div.setFont(font)
        self.div.setFocusPolicy(QtCore.Qt.NoFocus)
        self.div.setStyleSheet("QPushButton {\n"
                               "  background-color:  rgb(64, 64, 64);\n"
                               "  color:  rgb(211, 215, 207); \n"
                               "    border-radius: 35px;\n"
                               "  border: 1px solid gray;\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                               "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                               "}")
        self.div.setObjectName("div")
        self.operator_group.addButton(self.div)
        self.gridLayout.addWidget(self.div, 2, 3, 1, 1)

        # sum
        self.sum = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sum.sizePolicy().hasHeightForWidth())
        self.sum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sum.setFont(font)
        self.sum.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sum.setStyleSheet("QPushButton {\n"
                               "  background-color:  rgb(25, 23, 23);\n"
                               "  color:  rgb(211, 215, 207); \n"
                               "    border-radius: 35px;\n"
                               "  border: 1px solid gray;\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                               "                                      stop: 0 #2e2a2a, stop: 1 #423c3c);\n"
                               "}")
        self.sum.setObjectName("sum")
        self.gridLayout.addWidget(self.sum, 3, 4, 3, 1)

        # sub
        self.sub = QtWidgets.QPushButton(self.centralwidget)
        self.sub.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sub.setFont(font)
        self.sub.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sub.setStyleSheet("QPushButton {\n"
                               "  background-color:  rgb(64, 64, 64);\n"
                               "  color:  rgb(211, 215, 207); \n"
                               "    border-radius: 35px;\n"
                               "  border: 1px solid gray;\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                               "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                               "}")
        self.sub.setObjectName("sub")
        self.operator_group.addButton(self.sub)
        self.gridLayout.addWidget(self.sub, 4, 3, 1, 1)

        # dot
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setMinimumSize(QtCore.QSize(70, 70))
        self.dot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dot.setStyleSheet("QPushButton {\n"
                               "  background-color:  rgb(64, 64, 64);\n"
                               "  color:  rgb(211, 215, 207); \n"
                               "    border-radius: 35px;\n"
                               "  border: 1px solid gray;\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                               "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                               "}")
        self.dot.setObjectName("dot")
        self.operator_group.addButton(self.dot)
        self.gridLayout.addWidget(self.dot, 5, 2, 1, 1)

        # add
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.add.setFont(font)
        self.add.setFocusPolicy(QtCore.Qt.NoFocus)
        self.add.setStyleSheet("QPushButton {\n"
                               "  background-color:  rgb(64, 64, 64);\n"
                               "  color:  rgb(211, 215, 207); \n"
                               "    border-radius: 35px;\n"
                               "  border: 1px solid gray;\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                               "                                      stop: 0 rgb(105,105,105), stop: 1 rgb(135,135,135));\n"
                               "}")
        self.add.setObjectName("add")
        self.add.setShortcut("+")
        self.operator_group.addButton(self.add)
        self.gridLayout.addWidget(self.add, 5, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.modulo.setText(_translate("MainWindow", "mod"))
        self.sqrt.setText(_translate("MainWindow", "sqrt"))
        self.pow.setText(_translate("MainWindow", "pow"))
        self.factorial.setText(_translate("MainWindow", "!"))
        self.ac.setText(_translate("MainWindow", "AC"))
        self.num_7.setText(_translate("MainWindow", "7"))
        self.num_8.setText(_translate("MainWindow", "8"))
        self.num_9.setText(_translate("MainWindow", "9"))
        self.div.setText(_translate("MainWindow", "÷"))
        self.ce.setText(_translate("MainWindow", "CE"))
        self.num_4.setText(_translate("MainWindow", "4"))
        self.num_5.setText(_translate("MainWindow", "5"))
        self.num_6.setText(_translate("MainWindow", "6"))
        self.mul.setText(_translate("MainWindow", "*"))
        self.sum.setText(_translate("MainWindow", "="))
        self.sum.setShortcut(_translate("MainWindow", "Return"))
        self.num_1.setText(_translate("MainWindow", "1"))
        self.num_2.setText(_translate("MainWindow", "2"))
        self.num_3.setText(_translate("MainWindow", "3"))
        self.sub.setText(_translate("MainWindow", "-"))
        self.num_0.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", ","))
        self.add.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    sys.exit(app.exec_())
