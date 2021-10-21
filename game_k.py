import random
import sys

from PyQt5 import QtWidgets, QtCore


class Ui_MainWindow_K(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.resize(600, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(100, 140, 400, 50))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(430, 210, 75, 40))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.btn = QtWidgets.QPushButton(MainWindow)
        self.btn.setObjectName(u"pushButton")
        self.btn.setGeometry(QtCore.QRect(220, 540, 160, 30))
        self.btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.btn.setObjectName("btn")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(100, 70, 320, 30))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 320, 30))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(220, 430, 220, 100))
        self.label_3.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра"))
        self.pushButton.setText(_translate("MainWindow", "ОТПРАВИТЬ"))
        self.btn.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "Напишите:"))
        self.label_3.setText(_translate("MainWindow", "Счет: 0"))


class KeyGame(QtWidgets.QMainWindow, Ui_MainWindow_K):
    def __init__(self, p=None, pp=None):
        super().__init__()
        self.setupUi(self)
        self.p = p
        self.pp = pp
        self.pushButton.clicked.connect(self.add_function)
        self.btn.clicked.connect(self.back)
        self.words = ['Мир', 'Собака', 'Кошка', 'Кит', 'кот', 'Дерево', 'Питон']
        self.random_index = random.randint(0, len(self.words) - 1)
        self.label.setText("Напишите: " + self.words[self.random_index])
        self.a = 0

    def back(self):
        if self.p is not None:
            self.d = self.p(self.pp)
            self.d.show()
        self.close()

    def add_function(self):
        if self.lineEdit.text() == self.words[self.random_index]:
            self.random_index = random.randint(0, len(self.words) - 1)
            self.label.setText("Напишите: " + self.words[self.random_index])
            self.label_2.setText("")
            self.a += 1
            self.label_3.setText('Счет:' + str(self.a))
            self.lineEdit.setText('')
        else:
            self.label_2.setText("Повторите попытку")
            self.a -= 1
            self.label_3.setText('Счет:' + str(self.a))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = KeyGame()
    ex.show()
    sys.exit(app.exec_())
