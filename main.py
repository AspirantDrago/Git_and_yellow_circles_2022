import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    CIRCLE_COLOR = QColor(255, 255, 0)
    MINIMAL_DIAMETR = 10

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        diametr = random.randint(self.MINIMAL_DIAMETR, min(self.width(), self.height()) // 2)
        qp.setBrush(self.CIRCLE_COLOR)
        x = 30
        y = 30
        qp.drawEllipse(x, y, x + diametr, y + diametr)


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == '__main__':
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
