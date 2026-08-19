from CalculatorModel import CalculatorModel
from CalculatorView import CalculatorView
from CalculatorControl import CalculatorControl
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit
from PySide6.QtCore import QTimer, Qt
class CalculatorMain:
    def main(self):
        app = QApplication(sys.argv)
        model = CalculatorModel()
        view = CalculatorView()
        controller= CalculatorControl(model, view)
        view.equals.clicked.connect(controller.text_handle)
        view.setFixedSize(300, 300)
        view.show()
        sys.exit(app.exec())

my_calc= CalculatorMain()
CalculatorMain.main(my_calc)
