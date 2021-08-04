import sys
from PyQt5.Qtwidgets import *

app = QApplication(sys.argv)



# label = QLabel("Hello")
# label.show()
btn = QPushButton("Hello")  # 버튼 객체 생성
btn.show()

app.exec_()

#ctrl + shift + p 눌러서 python: Select Interpreter 입력하고 Python 3.8.8 64 bit ('base':conda)한번 실행해보세요
