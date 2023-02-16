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


    #abstract method
    def paintEvent(self, e):
        pass
        # p = QPainter()
        # p.begin(self)
        # p.setPen(QColor(0, 0, 0))
        # p.setBrush(QColor(0, 127, 0))

        # p.drawPolygon([
        #     QPoint(70, 100), QPoint(100, 110),
        #     QPoint(130, 100), QPoint(100, 150),
        # ])

        # p.setPen(QColor(255, 127, 0))
        # p.setBrush(QColor(255, 127, 0))
        # p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        # p.drawPolygon(
        #     [QPoint(50, 200), QPoint(150, 200), QPoint(100, 400)]
        # )

        # p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        # p.end()


    #abstract method
    def draw(self):
        raise NotImplementedError

#derived class1
class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")

    #overiden method
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        #ur code

        p.end()

#derived class2
class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")

    #overiden method
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        #ur code

        p.end()

#derived class3
class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")

    #overiden method
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        #ur code

        p.end()

def main():
    app = QApplication(sys.argv)

    k = Simple_drawing_window1()
    w = Simple_drawing_window2()
    t = Simple_drawing_window3()
    k.show()
    w.show()
    t.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())