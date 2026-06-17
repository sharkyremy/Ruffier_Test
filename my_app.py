from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.txt_instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        #self.hello_text.addWidget(self.layout)
        #self.instruction.addWidget(self.layout)
        #self.button.addWidget(self.layout)
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.txt_instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)



    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height) 
        self.move(win_x, win_y)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
app = QApplication([])
mw = MainWin()
app.exec_()

