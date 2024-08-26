from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        # Input and labels
        self.name_label = QLabel(txt_name)
        self.name_input = QLineEdit(txt_hintname)

        self.age_label = QLabel(txt_age)
        self.age_input = QLineEdit(txt_hintage)

        self.test1_label = QLabel(txt_test1)
        self.test1_input = QLineEdit(txt_hinttest1)
        self.start_test1_btn = QPushButton(txt_starttest1)

        self.test2_label = QLabel(txt_test2)
        self.test2_input = QLineEdit(txt_hinttest2)
        self.start_test2_btn = QPushButton(txt_starttest2)

        self.test3_label = QLabel(txt_test3)
        self.test3_input = QLineEdit(txt_hinttest3)
        self.start_test3_btn = QPushButton(txt_starttest3)

        self.send_results_btn = QPushButton(txt_sendresults)

        self.timer_label = QLabel("00:00:00")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)

        self.layout.addWidget(self.test1_label)
        self.layout.addWidget(self.test1_input)
        self.layout.addWidget(self.start_test1_btn)

        self.layout.addWidget(self.test2_label)
        self.layout.addWidget(self.test2_input)
        self.layout.addWidget(self.start_test2_btn)

        self.layout.addWidget(self.test3_label)
        self.layout.addWidget(self.test3_input)
        self.layout.addWidget(self.start_test3_btn)

        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.send_results_btn)

        self.setLayout(self.layout)

        # Timer setup
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_left = QTime(0, 0, 0)

    def next_click(self):
        self.hide()
        # Обработка исключений для ввода данных
        try:
            age = int(self.age_input.text())
            test1 = int(self.test1_input.text())
            test2 = int(self.test2_input.text())
            test3 = int(self.test3_input.text())
        except ValueError:
            print("Ошибка ввода данных.")
            return

        self.exp = Experiment(age, test1, test2, test3)
        self.fw = FinalWin(self.exp)
        print('Вызов 3-го экрана')

    def connects(self):
        self.start_test1_btn.clicked.connect(self.start_test1)
        self.start_test2_btn.clicked.connect(self.start_test2)
        self.start_test3_btn.clicked.connect(self.start_test3)
        self.send_results_btn.clicked.connect(self.next_click)

    def start_test1(self):
        self.time_left = QTime(0, 0, 15)
        self.timer.start(1000)
        print("Starting Test 1")

    def start_test2(self):
        self.time_left = QTime(0, 0, 15)
        self.timer.start(1000)
        print("Starting Test 2")

    def start_test3(self):
        self.time_left = QTime(0, 0, 15)
        self.timer.start(1000)
        print("Starting Test 3")

    def update_timer(self):
        if self.time_left == QTime(0, 0, 0):
            self.timer.stop()
            self.timer_label.setText("Time's up!")
        else:
            self.time_left = self.time_left.addSecs(-1)
            self.timer_label.setText(self.time_left.toString("hh:mm:ss"))


    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(400, 600)
        self.move(100, 100)

