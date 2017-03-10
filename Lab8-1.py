from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100), QPoint(100,110),
            QPoint(130,100), QPoint(100,150),
            ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawCircle([
            QPoint(50,200),QPoint(150,200),QPoint(100,400),
            ])
        p.drawImage(QRect(200,100,320,320),self.rabbit)
        p.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    a = Simple_drawing_window()

    a.show()

    app.exec_()

    sys.exit()
