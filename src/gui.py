import sys
import matlib
from PyQt5.QtWidgets import QPushButton, QToolButton, QLabel, QMessageBox
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self)  # Load the .ui file
        # Variable containing the last operation used
        self.used_operation = ""
        # Variable containing the last operation used
        self.first_value = "0"
        # Variable containing the result of the computation
        self.result = 0

        # First variable of the computation
        self.first_input = True
        # Button for dot was used (float conversion have to be used)
        self.dot_used = False
        # Operation can be performed, enough variables are given
        self.make_operation = False
        # Button for result was used, as one of the variable
        self.used_sum = False
        # Error happened during computation
        self.error_happen = False
        # The "CE" button was used, last entered number was cleared
        self.clear_was = False
        # Two needed numbers for computation are given
        self.two_numbers = False
        # Pushed already button for numbers
        self.num_pushed = False
        # If factorial was the previous operation
        self.factorial_was = False

        # Connection of buttons and functions performed on click
        self.ac.clicked.connect(self.clear_all)
        self.ce.clicked.connect(self.clear_previous)
        #
        self.sqrt.clicked.connect(lambda: self.pushed_op_button("sqrt"))
        self.pow.clicked.connect(lambda: self.pushed_op_button("pow"))
        self.div.clicked.connect(lambda: self.pushed_op_button("/"))
        self.mul.clicked.connect(lambda: self.pushed_op_button("*"))
        self.sub.clicked.connect(lambda: self.pushed_op_button("-"))
        self.add.clicked.connect(lambda: self.pushed_op_button("+"))
        self.factorial.clicked.connect(lambda: self.pushed_op_button("!"))
        self.modulo.clicked.connect(lambda: self.pushed_op_button("%"))
        #
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

        # help information
        self.help.clicked.connect(self.help_message)

        # setting window icon
        self.setWindowIcon(QtGui.QIcon("icon_calculator.xpm"))

    ##
    # @brief Show help information about the usage of the calculator
    def help_message(self):
        # popup message
        msg = QMessageBox()
        # title of the window
        msg.setWindowTitle("Information about usage")
        # text with information
        msg.setText("Test textttttt")
        # setting the shown icon
        msg.setIcon(QMessageBox.Information)
        # "OK" button is going to bo shown
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        # fixing the little rex "X" button to close the window !!
        msg.setEscapeButton(QMessageBox.Ok)

        msg.setInformativeText("more info")
        msg.setDetailedText("detailed information")
        # showing the message
        x = msg.exec_()

    ##
    # @brief Clear last pushed number
    def clear_previous(self):
        # No error happened during the previous computation
        if not self.error_happen:
            if self.first_input:
                self.first_value = "0"
                self.label.setText(self.first_value)
            if self.two_numbers:
                self.two_numbers = False
                self.first_value = ""
                self.label.setText("0")
            if self.used_sum:
                self.used_sum = False
                self.first_value = "0"
                self.label.setText("0")
                if self.used_operation == "!":
                    self.used_operation = ""

            self.dot_used = False
            self.num_pushed = False
        else:
            self.clear_all()

    ##
    # @brief Reset all class variables used in the program.
    def clear_all(self):
        self.used_operation = ""
        self.first_value = "0"
        self.used_sum = False
        self.result = 0

        self.first_input = True
        self.dot_used = False
        self.make_operation = False
        self.error_happen = False
        self.two_numbers = False
        self.num_pushed = False
        self.factorial_was = False

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
        # if not self.error_happen and (self.two_numbers or self.used_operation == "!"):
        if not self.error_happen:
            if self.make_operation:
                self.perform_operation()
                self.make_operation = False

            # Clearing the variables to accept the first number of new calculation
            self.first_input = True
            self.first_value = ""
            self.dot_used = False

            # Two new numbers are needed or the prev. result and one new number
            self.two_numbers = False

            # No number was pushed
            self.num_pushed = False

            # The sum was used
            self.used_sum = True
            self.label.setText(str(self.result))

        else:
            self.label.setText(str(self.result))
            # self.clear_all()

    ##
    # @brief Stores the value of the pushed button for numbers.
    # @param num Number of the button which was pushed.
    def pushed_num_button(self, num):
        # Button pushed when explicitly "0" is stored in first_value
        if self.first_input and not self.dot_used and not self.num_pushed:
            self.first_value = num
            self.num_pushed = True
        else:
            # Concat the values of the pushed num. buttons
            self.first_value += num

        # Show the created number
        self.label.setText(self.first_value)
        self.make_operation = True
        print(num)

    ##
    # @brief Stores which operation was chosen.
    # @param op Sign of the operation button which was pushed.
    def pushed_op_button(self, op):
        if not self.error_happen:
            # If right after the sum is used an operation button
            # So the next computation will use the previous result
            # example --> "prev result" + 3 = new result
            if self.used_sum and not self.num_pushed:
                self.first_input = False
                # self.used_sum = False
            # First input is made for the calculation,
            # store the value in result because it is used as the first number
            # when performing math. operations
            elif self.first_input:
                # Convert the string into number based on that if dot was used (float)
                # or not (int)
                if self.dot_used:
                    self.result = float(self.first_value)
                else:
                    self.result = int(self.first_value)
                # Next value is going to be the next number
                self.first_input = False
                # Enabling to use the dot again
                self.dot_used = False

            if op == "!":
                self.used_operation = op
                self.perform_operation()
                self.factorial_was = True

                # self.label.setText(str(self.result))

                self.make_operation = False

            elif self.two_numbers and self.num_pushed:
                self.perform_operation()

                self.label.setText(str(self.result))
                # pass
                self.make_operation = False
                self.num_pushed = False

            self.two_numbers = not self.two_numbers

            # Storing the pushed operation button
            self.used_operation = op

            if self.used_sum and not self.num_pushed:
                self.used_sum = False

            # Clearing the variable to store the second number of the calculation
            self.first_value = ""
            self.num_pushed = False
        else:
            self.clear_all()

    ##
    # @brief Performing the chosen operation. Counting out the result.
    def perform_operation(self):
        try:
            # Performing the operation. Using the needed function from matlib.py header file
            # The conversion of string to int or float is performed based on that if the
            # button for dot was used
            if self.used_operation != "!":
                # Containing the converted number
                second_number = 0
                if self.dot_used:
                    second_number = float(self.first_value)
                else:
                    second_number = int(self.first_value)
                print("Perform operation result " + str(
                    self.result) + " op " + self.used_operation + " second " + str(second_number))
            else:
                print("Perform operation result " + str(self.result) + " op " + self.used_operation)

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
    # Main application loop
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
