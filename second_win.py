from PyQt5.QtWidgets import (
QApplication, QWidget, QLabel, QPushButton,
QLineEdit, QVBoxLayout, QHBoxLayout)
from instr import *
from PyQt5.QtCore import Qt 
import sys


class HealthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Health")
        self.resize(1200, 600)

        main_layout = QHBoxLayout()

  
        left_layout = QVBoxLayout()

        left_layout.addWidget(QLabel("Enter Your full name:"))
        left_layout.addWidget(QLineEdit())

        left_layout.addWidget(QLabel("Full years:"))
        left_layout.addWidget(QLineEdit())

        left_layout.addWidget(
            QLabel(
                "Lie on your back and take your pulse for 15 seconds.\n"
                "Click the button to start the timer."
            )
        )

        left_layout.addWidget(QPushButton("Start the first test"))
        left_layout.addWidget(QLineEdit())

        left_layout.addWidget(
            QLabel(
                "Perform 30 squats in 45 seconds."
            )
        )

        left_layout.addWidget(QPushButton("Start doing squats"))

        left_layout.addWidget(
            QLabel(
                "Take your pulse for the first and last 15 seconds."
            )
        )

        left_layout.addWidget(QPushButton("Start the final test"))
        left_layout.addWidget(QLineEdit())
        left_layout.addWidget(QLineEdit())

        left_layout.addWidget(QPushButton("Send the results"))


        main_layout.addLayout(left_layout, 3)
       

        self.setLayout(main_layout)


app = QApplication(sys.argv)

window = HealthWindow()
window.show()

app.exec_()
