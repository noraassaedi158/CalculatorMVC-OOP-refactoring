import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit
from PySide6.QtCore import QTimer, Qt
class CalculatorMain:
    def main(self):
        app = QApplication(sys.argv)
        model = self.CalculatorModel()
        view = self.CalculatorView()
        controller= self.CalculatorControl(model, view)
        view.equals.connect(controller.text_handle)
        view.show()
        sys.exit(app.exec())
