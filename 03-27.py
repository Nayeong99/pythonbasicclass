import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MySignal(QObject):
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.run()

    @pyqtSlot()     # decorator. 없어도 상관은 없지만 있으면 편하다.
    def signall_emitted(self):
        print("signall emitted")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()