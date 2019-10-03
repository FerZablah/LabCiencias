
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QLabel, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    label1 = None
    label2 = None
    label3 = None
    def initUI(self):
        
        btn = QPushButton('Button1', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        btn.clicked.connect(self.on_click1)

        self.label1 = QLabel('00', self)
        self.label1.resize(self.label1.sizeHint())
        self.label1.move(80, 100) 
        self.label1.setText('0')

        btn2 = QPushButton('Button2', self)
        btn2.resize(btn.sizeHint())
        btn2.move(260, 50)
        btn2.clicked.connect(self.on_click2)

        self.label2 = QLabel('00', self)
        self.label2.resize(self.label2.sizeHint())
        self.label2.move(290, 100) 
        self.label2.setText('0')

        btn3 = QPushButton('Button3', self)
        btn3.resize(btn.sizeHint())
        btn3.move(480, 50)
        btn3.clicked.connect(self.on_click3)

        self.label3 = QLabel('00', self)
        self.label3.resize(self.label3.sizeHint())
        self.label3.move(510, 100) 
        self.label3.setText('0')

        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('App 1 - Python - Nativo')    
        self.show()
        
    
    @pyqtSlot()
    def on_click1(self):
        print(self.label1.text())
        self.label1.setText(str(int(self.label1.text()) + 1))
    def on_click2(self):
        print(self.label2.text())
        self.label2.setText(str(int(self.label2.text()) + 1))
    def on_click3(self):
        print(self.label3.text())
        self.label3.setText(str(int(self.label3.text()) + 1))
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())