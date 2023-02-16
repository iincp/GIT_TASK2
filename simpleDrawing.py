# Hello Ice

import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e): 
        pass


class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing 1")
        self.pic_1 = QPixmap("images/horse.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(200,100,320,320), self.pic_1)
        p.end()


#derived class2
class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing2")
        self.rabbit = QPixmap("images/rabbit.png")

    #overiden method
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        p.drawPixmap(QRect(0, 0, 675, 475), self.rabbit)

        p.end()

#derived class3
class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing3")
        self.pic_1 = QPixmap("images/cat.png")

    #overiden method
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        p.drawPixmap(QRect(0, 0, 675, 475), self.pic_1)

        p.end()


def main():
    app = QApplication(sys.argv)

    b = Simple_drawing_window1()
    i = Simple_drawing_window2()
    f = Simple_drawing_window3()
    b.show()
    i.show()
    f.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())