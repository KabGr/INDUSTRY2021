import sys

from PyQt5 import QtCore, QtWidgets

from desk import Desk
from game_k import KeyGame
from game_m import MouseGame


class Ui_MainWindow_Menu():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.setFixedSize(510, 570)
        MainWindow.setStyleSheet("background-color: #191824;")
        self.pushButton_m = QtWidgets.QPushButton(MainWindow)
        self.pushButton_m.setGeometry(QtCore.QRect(140, 60, 220, 70))
        self.pushButton_m.setStyleSheet("background-color: #5271FF;")
        self.pushButton_m.setObjectName("pushButton_m")
        self.pushButton_k = QtWidgets.QPushButton(MainWindow)
        self.pushButton_k.setGeometry(QtCore.QRect(140, 160, 220, 70))
        self.pushButton_k.setStyleSheet("background-color: #5271FF;")
        self.pushButton_k.setObjectName("pushButton_k")
        self.pushButton_d = QtWidgets.QPushButton(MainWindow)
        self.pushButton_d.setGeometry(QtCore.QRect(140, 260, 220, 70))
        self.pushButton_d.setStyleSheet("background-color: #5271FF;")
        self.pushButton_d.setObjectName("pushButton_d")
        self.pushButton_b = QtWidgets.QPushButton(MainWindow)
        self.pushButton_b.setGeometry(QtCore.QRect(140, 360, 220, 70))
        self.pushButton_b.setStyleSheet("background-color: #5271FF;")
        self.pushButton_b.setObjectName("pushButton_b")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Меню"))
        self.pushButton_m.setText(_translate("MainWindow", "Работа с мышью"))
        self.pushButton_k.setText(_translate("MainWindow", "Работа с клавиатурой"))
        self.pushButton_d.setText(_translate("MainWindow", "Интерактивная доска"))
        self.pushButton_b.setText(_translate("MainWindow", "Назад"))


class Menu(QtWidgets.QMainWindow, Ui_MainWindow_Menu):
    def __init__(self, p=None):
        super().__init__()
        self.setupUi(self)
        self.p = p
        self.pushButton_m.clicked.connect(self.mouse)
        self.pushButton_k.clicked.connect(self.keyboard)
        self.pushButton_d.clicked.connect(self.desk)
        self.pushButton_b.clicked.connect(self.back)

    def mouse(self):
        self.d = MouseGame(Menu, self.p)
        self.d.show()
        self.close()

    def keyboard(self):
        self.d = KeyGame(Menu, self.p)
        self.d.show()
        self.close()

    def desk(self):
        self.d = Desk(Menu, self.p)
        self.d.show()
        self.close()

    def back(self):
        if self.parent is not None:
            self.d = self.p()
            self.d.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
