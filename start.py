import sys

import pyttsx3
from PyQt5 import QtCore, QtGui, QtWidgets

from menu import Menu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("QLabel{ \n"
                                 "font-size: 30px; \n"
                                 "font-weight: bold; \n"
                                 "color: #3654C2; \n"
                                 "text-align: center; \n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow{ \n"
                                 "background: #191824; \n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(590, 460, 151, 111))
        self.btn.setStyleSheet("QPushButton{\n"
                               "background: #5271FF;\n"
                               "    font-size:19px;\n"
                               "    color: #ffffff;\n"
                               "    font-weight: bold;\n"
                               "    text-align: center;\n"
                               "    border-radius: 10px;\n"
                               "    margin:20 px;\n"
                               "}")
        self.btn.setObjectName("btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 644, 104))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{ \n"
                                 "font-size: 30px; \n"
                                 "font-weight: bold; \n"
                                 "color: #3654C2; \n"
                                 "text-align: center; \n"
                                 "}\n"
                                 "QMainWindow{ \n"
                                 "background: #75C6F3; \n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("QLabel{ \n"
                                      "font-size: 20px; \n"
                                      "font-weight: bold; \n"
                                      "color: rgb(255, 255, 255); \n"
                                      "text-align: center; \n"
                                      "}")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QLabel{ \n"
                                    "font-size: 20px; \n"
                                    "font-weight: bold; \n"
                                    "color: rgb(255, 255, 255); \n"
                                    "text-align: center; \n"
                                    "}")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Старт"))
        self.btn.setText(_translate("MainWindow", "Далее"))
        self.label.setText(_translate("MainWindow", "Выбрете настройки для Вашего ребёнка"))
        self.checkBox_2.setText(_translate("MainWindow", "Слепота"))
        self.checkBox.setText(_translate("MainWindow", "Глухота"))


class Start(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.cont)
        self.checkBox_2.stateChanged.connect(self.changeTitle)

    def changeTitle(self, state):
        if state == QtCore.Qt.Checked:
            self.a = 1
            Msg = 'Режим для слепых вкл'
            engine = pyttsx3.init()
            volume = engine.getProperty('volume')
            voices = engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")
            engine.setProperty('volume', 10)
            engine.say(Msg)
            engine.runAndWait()
        else:
            self.a = 0

    def cont(self):
        self.m = Menu(Start)
        self.m.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Start()
    MainWindow.show()
    sys.exit(app.exec_())
