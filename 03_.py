import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("코빗 시세 조회기.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC") # 조회 할 코인의 이름 넣기. 예: 
        price2 = pykorbit.get_current_price("ETH")
        price3 = pykorbit.get_current_price("XRP")
        price4 = pykorbit.get_current_price("ADA")
        
        
        self.lineEdit.setText(str(price))
        self.lineEdit_2.setText(str(price2))
        self.lineEdit_3.setText(str(price3))
        self.lineEdit_4.setText(str(price4))
        # 비트코인, 이더리움, 리플, 에이다


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()