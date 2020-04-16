import sys
import matlib
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui, QtWidgets, uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Ui, self).__init__()
        # Load the .ui file
        uic.loadUi('gui.ui', self)
        # Variable containing the last operation used
        self.used_operation = ""
        # Variable containing the last operation used
        self.first_value = "0"
        # Variable containing the result of the computation
        self.result = 0
        # Previous operation was realised, result can be used as first number
        self.state = 'not_computed'
        # Negative number is going to be entered
        self.negative_sign = False
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

        # Connection of buttons and functions performed on click
        self.ac.clicked.connect(self.clear_all)
        self.ce.clicked.connect(self.clear_previous)
        self.sum.clicked.connect(self.show_result)
        self.dot.clicked.connect(self.add_dot)

        # Operators
        self.sqrt.clicked.connect(lambda: self.pushed_op_button("sqrt"))
        self.pow.clicked.connect(lambda: self.pushed_op_button("pow"))
        self.div.clicked.connect(lambda: self.pushed_op_button("/"))
        self.mul.clicked.connect(lambda: self.pushed_op_button("*"))
        self.sub.clicked.connect(lambda: self.pushed_op_button("-"))
        self.add.clicked.connect(lambda: self.pushed_op_button("+"))
        self.factorial.clicked.connect(lambda: self.pushed_op_button("!"))
        self.modulo.clicked.connect(lambda: self.pushed_op_button("%"))

        # Numbers
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

        # Help information
        self.help.clicked.connect(self.help_message)

        # Setting window icon
        self.setWindowIcon(QtGui.QIcon("icon_calculator.xpm"))

    @staticmethod
    ##
    # @brief Show help information about the usage of the calculator
    def help_message():
        # Popup message
        msg = QMessageBox()
        # Title of the window
        msg.setWindowTitle("Information about usage")
        # Text with information
        msg.setText("Simple Calculator Manual")
        # Setting the shown icon
        msg.setIcon(QMessageBox.Information)
        # "OK" button is going to bo shown
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        # Fixing the little rex "X" button to close the window !!
        msg.setEscapeButton(QMessageBox.Ok)

        msg.setInformativeText("Calculator is a simple tool to make simple math calculations.\n"
                               "It works like most pocket calculators.\n"
                               "Press the number buttons to enter numbers and they appear on the display.\n"
                               "Press the operation buttons to choose the next operation to be performed.\n"
                               "Press \"=\" or Enter to display the result.\n")
        msg.setDetailedText("Decimal numbers can be entered using the \",\" or comma button.\n"
                            "Press the \"AC\" button or Ctrl+Backspace to clear the calculator and reset functions.\n"
                            "Press the \"CE\" button or Backspace to erase the last entered number.\n"
                            "\n"
                            "Please be aware that the factorial operation (\"!\") works just with one digit!\n")
        # showing the message
        msg.exec_()

    ##
    # @brief Clear last pushed number
    def clear_previous(self):
        # No error happened during the previous computation
        if not self.error_happen:
            # Clearing last pushed number and
            # needed variables based on the current state
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

            self.negative_sign = False
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
        self.state = "not_computed"
        self.negative_sign = False

        self.label.setText("0")

    ##
    # @brief Creating float number by connecting dot to the current number.
    def add_dot(self):
        # After an error or computation the first pushed button is the comma
        if self.error_happen or (self.used_sum and not self.num_pushed):
            if self.error_happen:
                self.error_happen = False
            self.clear_all()

        # Connect dot if the dot button was not used before
        # and the there was number already pushed
        elif (not self.dot_used) and (len(self.first_value) > 0):
            self.first_value += "."
            self.label.setText(self.first_value)
            self.dot_used = True

    ##
    # @brief Shows the result of the computation.
    def show_result(self):
        # No error happened during the previous computation
        if not self.error_happen:
            # Performing operation if previously it was not realised
            if self.make_operation:
                self.perform_operation()
                self.make_operation = False
                self.state = "computed"

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
            # Clearing the last used operator
            self.used_operation = ""

        else:
            self.label.setText(str(self.result))

    ##
    # @brief Stores the value of the pushed button for numbers.
    # @param num Number of the button which was pushed.
    def pushed_num_button(self, num):
        # After an error the first pushed button is a number
        if self.error_happen:
            self.error_happen = not self.error_happen
            self.clear_all()

        # Button pushed when explicitly "0" is stored in first_value
        if self.first_input and not self.dot_used and not self.num_pushed:
            # Minus sign is used, user wants to enter negative number
            if self.negative_sign:
                self.first_value = "-"+num
                self.negative_sign = False
            else:
                self.first_value = num
            self.num_pushed = True
        # Negative sign is used for the second number of the computation
        elif not self.first_input and not self.dot_used and not self.num_pushed and self.negative_sign:
            self.first_value = "-"+num
            self.negative_sign = False
            self.num_pushed = True
        else:
            # Concat the values of the pushed num. buttons
            self.first_value += num

        # Previous option performed, the new pushed number can be
        # used as second parameter for option
        if self.state == "computed":
            self.num_pushed = True

        # Show the created number and enable next operation
        self.label.setText(self.first_value)
        self.make_operation = True

    ##
    # @brief Stores which operation was chosen.
    # @param op Sign of the operation button which was pushed.
    def pushed_op_button(self, op):
        if not self.error_happen:
            # If the user wants to enter negative number :
            # 1) No previous number was entered so the application assumes that
            # the minus sign is used for negative number and not subtraction
            # 2) The negative sign is used for the second number from the operation
            if op == "-" and (self.first_input and not ('-' in self.first_value) and not self.num_pushed
               and not self.used_sum) or (not self.first_input and self.first_value == '') and \
                    self.used_operation != '!':

                self.negative_sign = True
                self.num_pushed = False
            else:
                # If right after the sum is used an operation button
                # So the next computation will use the previous result
                # example --> "prev result" + 3 = new result
                if self.used_sum and not self.num_pushed:
                    self.first_input = False
                    self.used_sum = False

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
                    # Next value is going to be the second number
                    self.first_input = False
                    # Enabling to use the dot again
                    self.dot_used = False

                # The chosen operation is factorial
                if op == "!":
                    # Perform the operation, one number is just needed
                    self.used_operation = op
                    self.perform_operation()
                    # Show the result
                    self.label.setText(str(self.result))

                    self.num_pushed = False
                    # Sign that computation was performed and clear the used operator
                    self.state = "computed"
                    self.used_operation = ""
                    # If after the factorial operation the Enter or '=' is pushed,
                    # there is no need to perform operation
                    self.make_operation = False

                # The chosen operation is not factorial
                # and two new numbers were chosen for the operation
                # or one new number end the prev. result is going to be used
                elif self.num_pushed and (self.two_numbers or self.state == 'computed') and self.first_value != '' \
                        and self.used_operation != "":
                    self.perform_operation()
                    # Show result
                    self.label.setText(str(self.result))
                    # Sign that computation was performed and enable to enter new number
                    self.make_operation = False
                    self.num_pushed = False
                    self.dot_used = False
                    self.state = "computed"

                # For every second chosen operation there were two numbers chosen
                self.two_numbers = not self.two_numbers

                # Storing the pushed operation button
                if op != '!':
                    self.used_operation = op

                # Clearing the variable to store the second number of the calculation
                self.first_value = ""
        else:
            self.clear_all()

    ##
    # @brief Performing the chosen operation. Counting out the result.
    def perform_operation(self):
        try:
            # Local variable used to store the converted second number of operation
            second_number = 0

            # Performing the operation. Using the needed function from matlib.py header file
            # The conversion of string to int or float is performed based on that if the
            # button for dot was used
            if self.used_operation != "!":
                # Containing the converted number
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
            self.result = "Not natural num. entered"
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
