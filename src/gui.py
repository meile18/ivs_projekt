import sys
import matlib
from PyQt5.QtWidgets import QPushButton, QToolButton, QLabel
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self)  # Load the .ui file
        self.used_operation = ""
        self.first_value = ""
        self.result = 0

        self.first_input = True
        self.dot_used = False
        self.make_operation = False
        self.used_sum = False
        self.error_happen = False
        self.clear_was = False

        self.ac.clicked.connect(self.clear_all)
        self.ce.clicked.connect(self.clear_previous)

        # self.sqrt = self.findChild(QtWidgets.QPushButton, 'sqrt')
        self.sqrt.clicked.connect(lambda: self.pushed_op_button("sqrt"))
        self.pow.clicked.connect(lambda: self.pushed_op_button("pow"))
        self.div.clicked.connect(lambda: self.pushed_op_button("/"))
        self.mul.clicked.connect(lambda: self.pushed_op_button("*"))
        self.sub.clicked.connect(lambda: self.pushed_op_button("-"))
        self.add.clicked.connect(lambda: self.pushed_op_button("+"))
        self.factorial.clicked.connect(lambda: self.pushed_op_button("!"))
        self.modulo.clicked.connect(lambda: self.pushed_op_button("%"))

        self.sum.clicked.connect(self.show_result)
        self.dot.clicked.connect(self.add_dot)

        self.num_0.clicked.connect(lambda: self.pushed_num_button("0"))
        self.num_1.clicked.connect(lambda: self.pushed_num_button("1"))
        self.num_2.clicked.connect(lambda: self.pushed_num_button("2"))
        self.num_3.clicked.connect(lambda: self.pushed_num_button("3"))
        self.num_4.clicked.connect(lambda: self.pushed_num_button("4"))
        self.num_5.clicked.connect(lambda: self.pushed_num_button("5"))
        self.num_6.clicked.connect(lambda: self.pushed_num_button("6"))
        self.num_7.clicked.connect(lambda: self.pushed_num_button("7"))
        self.num_8.clicked.connect(lambda: self.pushed_num_button("8"))
        self.num_9.clicked.connect(lambda: self.pushed_num_button("9"))

    ##
    # @brief Clear last pushed number
    def clear_previous(self):
        # No error happened during the previous computation
        if not self.error_happen:
            print("first before clear "+self.first_value)
            self.first_value = "0"
            self.label.setText("0")
            self.clear_was = True
            print("clear one result "+str(self.result))
        else:
            self.clear_all()

    ##
    # @brief Reset all class variables used in the program.
    def clear_all(self):
        self.used_operation = ""
        self.first_value = ""
        self.used_sum = False
        self.result = 0

        self.first_input = True
        print("clear all first true")
        self.dot_used = False
        self.make_operation = False
        self.error_happen = False
        self.label.setText("0")

    ##
    # @brief Creating float number by connecting dot to the current number.
    def add_dot(self):
        # Connect dot if the dot button was not used before
        # and the there was number already pushed
        if (not self.dot_used) and len(self.first_value):
            self.first_value += "."
            self.label.setText(self.first_value)
            self.dot_used = True

    ##
    # @brief Shows the result of the computation.
    def show_result(self):
        # No error happened during the previous computation
        if not self.error_happen:
            # Perform chosen operation for factorial
            # or with the result of the previous computation
            if self.make_operation or (self.used_operation == "!"):
                self.perform_operation()
                self.make_operation = False
            else:
                self.make_operation = True

            self.used_sum = True
            self.dot_used = False
            self.first_value = ""
            self.label.setText(str(self.result))
            print("Result is "+str(self.result)+" op is "+self.used_operation+"first is "+self.first_value)
            self.used_operation = "+"
        else:
            self.clear_all()

    ##
    # @brief Stores the value of the pushed button for numbers.
    # @param num Number of the button which was pushed.
    def pushed_num_button(self, num):
        # Concat pushed numbers
        if self.clear_was:
            self.first_value = num
            self.clear_was = False
        else:
            self.first_value += num
        self.label.setText(self.first_value)

        # If previous computation was completed and button for numbers is pushed
        # clear the variables like the new input is the first number of the next computation
        if self.used_sum:
            self.used_sum = False
            self.result = 0
            self.first_input = True
            print("self.first_input true")
        print(num)

    ##
    # @brief Stores which operation was chosen.
    # @param op Sign of the operation button which was pushed.
    def pushed_op_button(self, op):
        # If no error happen during previous calculation
        if not self.error_happen and (len(self.first_value) or self.used_sum):
            print("in op_button")
            #
            if self.used_sum and not self.clear_was:
                print("if used sum ...")
                self.first_value = self.result
                self.first_input = True
                self.used_sum = False

            # If the first number of the computation is pressed
            # store it into result variable, the type is based on
            # if the dot button was pushed (float) or not (int)
            if self.first_input or self.clear_was:
                print("first input true")
                self.first_input = False
                if self.dot_used:
                    self.result = float(self.first_value)
                else:
                    self.result = int(self.first_value)

            # Store the chosen operation
            self.used_operation = op

            # Perform operation with the result of the previous operation
            # and the new number
            if self.make_operation:
                print("make op "+self.used_operation)
                self.perform_operation()
                self.make_operation = False
                self.label.setText(str(self.result))
            else:
                self.make_operation = True

            self.first_value = ""
            self.dot_used = False
            print("Result is "+str(self.result)+" first is "+self.first_value)
        else:
            # If error was the result of the last calculation and
            # user want to perform operations with that result
            # reset all variables
            self.clear_all()
        print("end of op_button "+self.used_operation)

    ##
    # @brief Performing the chosen operation. Counting out the result.
    def perform_operation(self):
        try:
            # Performing the operation. Using the needed function from matlib.py header
            # The conversion of string to int or float is performed based on that if the
            # button for dot was used
            if self.used_operation != "!":
                second_number = 0
                if self.dot_used:
                    second_number = float(self.first_value)
                else:
                    second_number = int(self.first_value)

            if self.used_operation == "+":
                self.result = matlib.add(self.result, second_number)

            elif self.used_operation == "-":
                self.result = matlib.sub(self.result, second_number)

            elif self.used_operation == "*":
                self.result = matlib.mul(self.result, second_number)

            elif self.used_operation == "/":
                self.result = matlib.div(self.result, second_number)

            elif self.used_operation == "sqrt":
                self.result = matlib.sqrt(self.result, second_number)

            elif self.used_operation == "pow":
                self.result = matlib.pow(self.result, second_number)

            elif self.used_operation == "!":
                self.result = matlib.factorial(self.result)

            elif self.used_operation == "%":
                self.result = matlib.modulo(self.result, second_number)

        # Catching errors raised by functions
        except ValueError:
            # The exponent was not natural number when counting power
            self.result = "n has to be natural number"
            self.error_happen = True
        except ZeroDivisionError:
            # The denominator was 0 when trying to perform division
            self.result = "Booom! Zero division!"
            self.error_happen = True
        except RecursionError:
            # The number of recursions is higher then max. depth
            self.result = "Too big number for factorial!"
            self.error_happen = True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
