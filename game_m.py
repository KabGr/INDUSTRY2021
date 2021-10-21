import random
import sys
import time

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow_M(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "background: #75C6F3;\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "background: #5CC236;\n"
                                 "    font-size:13px;\n"
                                 "    color: #1e2e69;\n"
                                 "    font-weight: bold;\n"
                                 "   text-align: center;\n"
                                 "    border-radius: 10px;\n"
                                 "    margin:20 px;\n"
                                 "    border: 1px solid #0bd42c;\n"
                                 "}"
                                 "QLabel{ \n"
                                 "font-size: 15px; \n"
                                 "font-weight: bold; \n"
                                 "color: #3654C2; \n"
                                 "text-align: center; \n"
                                 "}\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 192, 91, 81))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 500, 140, 100))
        self.pushButton2.setObjectName("pushButton2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 400, 61))
        self.label.setText("Как можно быстрее нажми 10 кнопок")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра"))
        self.pushButton.setText(_translate("MainWindow", "Нажми меня"))
        self.pushButton2.setText(_translate("MainWindow", "Назад"))


class MouseGame(QtWidgets.QMainWindow, Ui_MainWindow_M):
    def __init__(self, p=None, pp=None):
        super().__init__()
        self.p = p
        self.pp = pp
        self.count = 0
        self.setupUi(self)
        self.time_start = time.time()
        self.pushButton.clicked.connect(self.start)
        self.pushButton2.clicked.connect(self.back)

    def start(self):
        self.count += 1
        if self.count == 10:
            self.finich_time = round(time.time() - self.time_start, 1)
            self.label.setText(f"Вы нажали {self.count} кнопок за {self.finich_time} сек.")
            self.pushButton.deleteLater()
        self.pushButton.move(random.randint(150, 700), random.randint(150, 500))

    def back(self):
        if self.p is not None:
            self.d = self.p(self.pp)
            self.d.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MouseGame()
    MainWindow.show()
    sys.exit(app.exec_())
