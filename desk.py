import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog


class Desk(QMainWindow):
    def __init__(self, p=None, pp=None):
        super().__init__()
        self.p = p
        self.pp = pp
        self.setWindowTitle('Интерактивная доска')
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUi()

    def initUi(self):
        self.setFixedSize(400, 420)
        self.c = QColor(0, 0, 0)
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        self.btn = QPushButton('Назад', self)
        self.btn.resize(360, 20)
        self.btn.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btn.clicked.connect(self.back)
        self.btn_c = QPushButton('Цвет', self)
        self.btn_c.resize(40, 20)
        self.btn_c.move(360, 0)
        self.btn_c.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_c.clicked.connect(self.color)

    def back(self):
        if self.p is not None:
            self.d = self.p(self.pp)
            self.d.show()
        self.close()

    def color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.c = color

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        pp.setPen(self.c)
        pp.drawLine(self.lastPoint, self.endPoint)
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 20, self.pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos() - QPoint(0, 20)
            self.endPoint = self.lastPoint

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.endPoint = event.pos() - QPoint(0, 20)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos() - QPoint(0, 20)
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Desk()
    ex.show()
    sys.exit(app.exec_())
