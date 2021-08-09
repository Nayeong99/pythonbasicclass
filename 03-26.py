import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pykorbit


form_class = uic.loadUiType("코빗 시세 조회기.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

    def timeout (self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        
        price = pykorbit.get_current_price("BTC")
        price2 = pykorbit.get_current_price("ETH")
        price3 = pykorbit.get_current_price("XRP")
        price4 = pykorbit.get_current_price("ADA")

        self.lineEdit.setText(str(price))
        self.lineEdit_2.setText(str(price2))
        self.lineEdit_3.setText(str(price3))
        self.lineEdit_4.setText(str(price4))


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()