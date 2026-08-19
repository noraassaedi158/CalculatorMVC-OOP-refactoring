import signal
import sys
import json
import random
import datetime
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit
from PySide6.QtCore import QTimer, Qt
#open my JSON file to access the qoutes
with open("qoutes.json", 'r') as file:
    q = json.load(file)
#inherits QWidget
class CalculatorView(QWidget):
    #self is for anything that will be used outside this module, the rest of the variables are local
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.screen = QLineEdit(self)
        self.screen.setFixedHeight(30)
        self.screen.setPlaceholderText(self.en())
        self.screen.setReadOnly(True)
        cleared = QPushButton("Clear")
        cleared.clicked.connect(self.wipe)
        date = QLabel("Date: " + datetime.datetime.now().strftime("%A %d %B %Y"))
        self.time = QLabel()
        self.clock = QTimer()
        self.clock.setInterval(1000)
        self.clock.timeout.connect(self.time_rn)
        self.clock.start()
        one = QPushButton(" 1 ")
        one.clicked.connect(lambda: self.calc_num("1"))
        two = QPushButton(" 2 ")
        two.clicked.connect(lambda: self.calc_num("2"))
        three = QPushButton(" 3 ")
        three.clicked.connect(lambda: self.calc_num("3"))
        four = QPushButton(" 4 ")
        four.clicked.connect(lambda: self.calc_num("4"))
        five = QPushButton(" 5 ")
        five.clicked.connect(lambda: self.calc_num("5"))
        six = QPushButton(" 6 ")
        six.clicked.connect(lambda: self.calc_num("6"))
        seven = QPushButton(" 7 ")
        seven.clicked.connect(lambda: self.calc_num("7"))
        eight = QPushButton(" 8 ")
        eight.clicked.connect(lambda: self.calc_num("8"))
        nine = QPushButton(" 9 ")
        nine.clicked.connect(lambda: self.calc_num("9"))
        zero = QPushButton(" 0 ")
        zero.clicked.connect(lambda: self.calc_num("0"))
        addition_button = QPushButton(" + ")
        addition_button.clicked.connect(lambda: self.calc_num(" + "))
        subtraction_button = QPushButton(" - ")
        subtraction_button.clicked.connect(lambda: self.calc_num(" - "))
        multi_button = QPushButton(" x ")
        multi_button.clicked.connect(lambda: self.calc_num(" x "))
        divi_button = QPushButton(" ÷ ")
        divi_button.clicked.connect(lambda: self.calc_num(" ÷ "))
        dot = QPushButton(".")
        dot.clicked.connect(lambda: self.calc_num("."))
        left_br = QPushButton("(")
        left_br.clicked.connect(lambda: self.calc_num( " ( "))
        right_br = QPushButton(")")
        right_br.clicked.connect(lambda: self.calc_num(" ) "))
        self.equals = QPushButton(" = ")
        press_me = QPushButton("Press me!")
        press_me.clicked.connect(self.press)
        title = QLabel("This is my first personal mini project!")
        title.setObjectName("title")
        whole_layout = QVBoxLayout()
        whole_layout.addWidget(title)
        whole_layout.addWidget(date)
        whole_layout.addWidget(self.time)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        whole_layout.addWidget(self.screen)
        whole_layout.addWidget(cleared)
        buttons_layout = QGridLayout()
        buttons_layout.addWidget(seven, 0, 0)
        buttons_layout.addWidget(eight, 0, 1)
        buttons_layout.addWidget(nine, 0, 2)
        buttons_layout.addWidget(divi_button, 0, 3)
        buttons_layout.addWidget(four, 1, 0)
        buttons_layout.addWidget(five, 1, 1)
        buttons_layout.addWidget(six, 1, 2)
        buttons_layout.addWidget(multi_button, 1, 3)
        buttons_layout.addWidget(one, 2, 0)
        buttons_layout.addWidget(two, 2, 1)
        buttons_layout.addWidget(three, 2, 2)
        buttons_layout.addWidget(subtraction_button, 2, 3)
        buttons_layout.addWidget(zero, 3, 1)
        buttons_layout.addWidget(dot, 3, 2)
        buttons_layout.addWidget(addition_button, 3, 3)
        buttons_layout.addWidget(press_me, 3, 0)
        buttons_layout.addWidget(left_br, 4, 0)
        buttons_layout.addWidget(right_br, 4, 1)
        buttons_layout.addWidget(self.equals, 4, 2, 1, 2)
        whole_layout.addLayout(buttons_layout)
        self.setLayout(whole_layout)
        self.setStyleSheet(""" QWidget {background-color: #A6425B;
                                      color: black }
                          QPushButton { background-color: pink;
                                        color: #A6425B ;
                                        font-weight: bold;
                                        border: 1.5px solid #BD6073; 
                                        border-radius: 8px;
                                        } 
                           QPushButton:pressed { background-color: #FAEDED} 
                           QPushButton:hover { background-color: #FAEDED}             
                           QLabel { color : white ;
                                    font-weight: bold ; 
                                    font-family: Lucida Console }
                           QLabel#title{color : black ;
                                    font-size: 13px;
                                    font-family : Lucida Calligraphy}
                           QLineEdit{
                                    color : white ;
                                    font-weight: bold;
                                    border:  0.5px solid #BD6073;
                                    border-radius: 8px;
                                    font-family: Lucida Console} 
                           QLineEdit::placeholder { color: white;
                                                    font-weight: bold} """)




    def en(self):
        return random.choice(q["encourage"])
    def calc_num(self,n):
        self.screen.setText(self.screen.text() + n)

    def wipe(self):
        self.screen.clear()

    def press(self):
        self.screen.clear()
        self.screen.setPlaceholderText((self.en()))

    def display_answer(self, answer):
        self.screen.clear()
        self.screen.setText(str(answer[0]))

    def time_rn(self):
        self.time.setText("Time: " + datetime.datetime.now().strftime("%I:%M %p"))


