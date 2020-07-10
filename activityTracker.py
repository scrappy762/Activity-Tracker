from functools import partial

from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QMessageBox, QTextEdit, QLayoutItem, \
    QWidget, QDialog, QMainWindow, QGridLayout, QLineEdit, QFormLayout
import os
import sys
from PyQt5.QtCore import Qt, QObject

#
#
# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('You clicked the button!')
#     alert.exec_()

#
# if __name__ == '__main__':
#     app = QApplication([])
#     app
#     window = QLabel()
#
#     # label = QLabel('Hello World!')
#     # label.show()
#
#     text = QTextEdit()
#     text.setText("Hello")
#     text.show()
#
#     layout = QVBoxLayout()
#     # layout.addItem(text)
#     # layout.addWidget(QPushButton('Top'))
#     #
#     # bottom = QPushButton('Bottom')
#     # bottom.clicked.connect(on_button_clicked)
#     #
#     # layout.addWidget(bottom)
#     # layout.addItem(text)
#
#     window.setLayout(layout)
#
#     window.show()
#     sys.exit(app.exec_())
#
#
# def rest():
#     import geocoder
#     g = geocoder.ip('me')
#     print(g.latlng)
#
# rest()


# from PySide2.QtWidgets import QApplication, QWidget

# Create a subclass of QMainWindow to setup the calculator's GUI
from datetime import datetime

appendTxt = []
class UserPage(QMainWindow):
    def __init__(self):
        """View initializer."""
        super().__init__()
        self.setWindowTitle('Activity Tracker')
        self.setFixedSize(420, 420)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.le = QLineEdit()
        layout = QFormLayout()
        layout.addRow('User Name:', self.le)
        self.generalLayout.addLayout(layout)

        btn = QPushButton('Enter')

        btn.clicked.connect(partial(self.showActivityType))
        self.generalLayout.addWidget(btn)

    def showActivityType(self):
        userName = self.le.text()
        view = ChooseActivityType(userName)
        view.show()


class ChooseActivityType(QMainWindow):

    def __init__(self, userName):
        """View initializer."""
        super().__init__()
        self.userName = userName
        self.setWindowTitle('Activity Tracker')
        self.setFixedSize(420, 420)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        btn = QPushButton('Single Activity')
        btn1 = QPushButton('Multiple Activity')

        self.generalLayout.addWidget(btn)
        self.generalLayout.addWidget(btn1)

        btn.clicked.connect(partial(self.show_activity_page, userName=userName))
        btn1.clicked.connect(partial(self.start_tracker, userName=userName))

    def show_activity_page(self, userName):
        layer = 3
        view = PyCalcUi(layer=layer, btnText="", userName=userName)
        view.show()
        # Create instances of the model and the controller
        PyCalcCtrl(view=view, layer=layer)

    def start_tracker(self, userName):
        layer = 1
        view = PyCalcUi(layer=layer, btnText="", userName=userName)
        view.show()
        # Create instances of the model and the controller
        PyCalcCtrl(view=view, layer=layer)


class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""

    def __init__(self, layer, btnText, userName):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.userName = userName
        self.setWindowTitle('Activity Tracker')
        self.setFixedSize(600, 600)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay(layer=layer, btnText=btnText)
        self._createButtons(layer=layer)


    def _createDisplay(self, layer, btnText):
        """Create the display."""

        # self.lable = QLabel("Hello")
        # self.lable.setFixedHeight(35)

        # Create the display widget
        if layer == 1:
            #     first_page_text = str(btnText)
            self.display = QLabel("Main Page")
        elif layer == 2:
            self.display = QLabel("Page " + btnText + "  B")
        else:
            self.display = QLabel("Page " + btnText + "  C")
        # self.display.text("as")
        # Set some display's properties
        self.display.setFixedHeight(20)
        self.display.setAlignment(Qt.AlignCenter)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self, layer):
        """Create the buttons."""

        self.buttons = {}
        self.le = QLineEdit()

        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout

        print("layer", layer)

        if layer == 1:

            buttons = {'PMCS': (0, 0),
                       '2': (0, 1),
                       '3': (0, 2),
                       '4': (0, 3),
                       '5': (0, 4),
                       '6': (0, 5),
                       '7': (1, 0),
                       '8': (1, 1),
                       '9': (1, 2),
                       '10': (1, 3),
                       '11': (1, 4),
                       '12': (1, 5),
                       '13': (2, 0),
                       '14': (2, 1),
                       '15': (2, 2),
                       '16': (2, 3),
                       '17': (2, 4),
                       '18': (2, 5),
                       '19': (3, 0),
                       '20': (3, 1),
                       '21': (3, 2),
                       '22': (3, 3),
                       '23': (3, 4),
                       '24': (3, 5)
                       }
        elif layer == 2:
            buttons = {'BLK F150': (0, 0),
                       'Dodge Van': (0, 1),
                       'Jeep': (0, 2),
                       'TAN F150': (0, 3),
                       'Camry': (0, 4),
                       'Tahoe': (0, 5),
                       '17': (1, 0),
                       '18': (1, 1),
                       '19': (1, 2),
                       '20': (1, 3),
                       '21': (1, 4),
                       '22': (1, 5),
                       '23': (2, 0),
                       '24': (2, 1),
                       '25': (2, 2),
                       '26': (2, 3),
                       '27': (2, 4),
                       '28': (2, 5),
                       '29': (3, 0),
                       '30': (3, 1),
                       '31': (3, 2),
                       '32': (3, 3),
                       '33': (3, 4),
                       '34': (3, 5)
                       }
        else:
            buttons = {'Start': (1, 0),
                       'Stop': (1, 5)
                       }

            layout = QFormLayout()
            layout.addRow('Activity Name:', self.le)
            self.generalLayout.addLayout(layout)
            # self.connect(self.buttons, SIGNAL("clicked()"), self.activity_entered())

        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(100, 100)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')

    def activity_entered(self, btnText, layer):
        text = self.le.text()
        text = str(btnText) + "  " + text
        self.entry_log(text, layer=layer)
        self.le.setText("")

    def entry_log(self, text, layer):
        if layer > 3:
            print("append Text ", appendTxt)
            with open('activity_log.txt', 'a') as file:
                dt = datetime.now()
                dt = dt.strftime("%Y-%m-%d %H:%M:%S")
                file.write(dt + " " + str(self.userName) + " " + " ".join(appendTxt) + " " +text + "\n")
                file.close()
        else:
            appendTxt.append(text)

class PyCalcCtrl:
    """PyCalc Controller class."""

    def __init__(self, view, layer):
        """Controller initializer."""
        self._view = view
        # Connect signals and slots
        self._connectSignals(layer)

    def _buildExpression(self, sub_exp, layer):
        """Build expression."""
        # expression = self._view.displayText() + sub_exp
        # self._view.setDisplayText(expression)
        self._view.entry_log(text=sub_exp, layer=layer)
        view = PyCalcUi(layer=layer, btnText=sub_exp, userName=self._view.userName)
        view.show()
        # Create instances of the model and the controller
        PyCalcCtrl(view=view, layer=layer)

    def _buildUiOthers(self, btnText, layer):
        self._view.activity_entered(btnText, layer=layer)
        # if btnText == "Back":
        #     print("hi")
        #     sys.exit(pycalc.exec_())

    def _connectSignals(self, layer):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText == "Start" or btnText == "Stop":
                btn.clicked.connect(partial(self._buildUiOthers, btnText=btnText, layer=layer+1))
                # self._view.buttons["Enter"].clicked.connect(self._view.activity_entered)

            if btnText not in {'=', 'C', "Start", "Stop"}:
                btn.clicked.connect(
                    partial(self._buildExpression, btnText, layer + 1))

        # self._view.buttons["Enter"].clicked.connect(self._view.activity_entered)


if __name__ == "__main__":
    # Create an instance of QApplication
    # cx = ApplicationContext()
    pycalc = QApplication(sys.argv)

    # Show the calculator's GUI
    # layer = 1
    view = UserPage()
    view.show()
    # # Create instances of the model and the controller
    # PyCalcCtrl(view=view, layer=layer)
    # Execute calculator's main loop
    # exit_code = cx.app.exec_()  # 2. Invoke appctxt.app.exec_()
    # sys.exit(exit_code)
    sys.exit(pycalc.exec_())
