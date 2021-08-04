import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC") # 조회 할 코인의 이름 넣기. 예: 
        self.lineEdit.setText(str(price))
        # 비트코인, 이더리움, 리플, 에이다


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()