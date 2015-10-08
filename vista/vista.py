# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created: Sun Oct 04 16:26:16 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    """Esta clase se ocupa de la parte gráfica de la aplicación, gestiona aspectos como
    botones, frames, inputs, colores, entre otras cosas. Cabe agregar que esta clase se creo
    haciendo uso de la herramienta QtDesigner"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(522, 372)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: #252525;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 120, 321, 241))
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.button7 = QtGui.QPushButton(self.frame)
        self.button7.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.button7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button7.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;\n"
""))
        self.button7.setObjectName(_fromUtf8("button7"))
        self.button9 = QtGui.QPushButton(self.frame)
        self.button9.setGeometry(QtCore.QRect(170, 30, 61, 51))
        self.button9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button9.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button9.setObjectName(_fromUtf8("button9"))
        self.button8 = QtGui.QPushButton(self.frame)
        self.button8.setGeometry(QtCore.QRect(90, 30, 61, 51))
        self.button8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button8.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button8.setObjectName(_fromUtf8("button8"))
        self.button_decimal = QtGui.QPushButton(self.frame)
        self.button_decimal.setGeometry(QtCore.QRect(250, 30, 61, 51))
        self.button_decimal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_decimal.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 30px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button_decimal.setObjectName(_fromUtf8("button_decimal"))
        self.button4 = QtGui.QPushButton(self.frame)
        self.button4.setGeometry(QtCore.QRect(10, 100, 61, 51))
        self.button4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button4.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button4.setObjectName(_fromUtf8("button4"))
        self.button1 = QtGui.QPushButton(self.frame)
        self.button1.setGeometry(QtCore.QRect(10, 170, 61, 51))
        self.button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button1.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button1.setObjectName(_fromUtf8("button1"))
        self.button5 = QtGui.QPushButton(self.frame)
        self.button5.setGeometry(QtCore.QRect(90, 100, 61, 51))
        self.button5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button5.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button5.setObjectName(_fromUtf8("button5"))
        self.button2 = QtGui.QPushButton(self.frame)
        self.button2.setGeometry(QtCore.QRect(90, 170, 61, 51))
        self.button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button2.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button2.setObjectName(_fromUtf8("button2"))
        self.button6 = QtGui.QPushButton(self.frame)
        self.button6.setGeometry(QtCore.QRect(170, 100, 61, 51))
        self.button6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button6.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button6.setObjectName(_fromUtf8("button6"))
        self.button3 = QtGui.QPushButton(self.frame)
        self.button3.setGeometry(QtCore.QRect(170, 170, 61, 51))
        self.button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button3.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button3.setObjectName(_fromUtf8("button3"))
        self.button0 = QtGui.QPushButton(self.frame)
        self.button0.setGeometry(QtCore.QRect(250, 100, 61, 121))
        self.button0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button0.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#f3f3f3;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button0.setObjectName(_fromUtf8("button0"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(340, 120, 171, 231))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.button_erase = QtGui.QPushButton(self.frame_2)
        self.button_erase.setGeometry(QtCore.QRect(20, 30, 61, 51))
        self.button_erase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_erase.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#a4a4a4;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button_erase.setObjectName(_fromUtf8("button_erase"))
        self.multiplicacion = QtGui.QPushButton(self.frame_2)
        self.multiplicacion.setGeometry(QtCore.QRect(100, 100, 61, 51))
        self.multiplicacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiplicacion.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#a4a4a4;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.multiplicacion.setObjectName(_fromUtf8("multiplicacion"))
        self.suma = QtGui.QPushButton(self.frame_2)
        self.suma.setGeometry(QtCore.QRect(100, 170, 61, 51))
        self.suma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.suma.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#a4a4a4;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.suma.setObjectName(_fromUtf8("suma"))
        self.resta = QtGui.QPushButton(self.frame_2)
        self.resta.setGeometry(QtCore.QRect(20, 170, 61, 51))
        self.resta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resta.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#a4a4a4;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.resta.setObjectName(_fromUtf8("resta"))
        self.division = QtGui.QPushButton(self.frame_2)
        self.division.setGeometry(QtCore.QRect(20, 100, 61, 51))
        self.division.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.division.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#a4a4a4;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.division.setObjectName(_fromUtf8("division"))
        self.button_c = QtGui.QPushButton(self.frame_2)
        self.button_c.setGeometry(QtCore.QRect(100, 30, 61, 51))
        self.button_c.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_c.setStyleSheet(_fromUtf8("background-color:#303030;\n"
"border-radius:4px;\n"
"color:#a4a4a4;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;"))
        self.button_c.setObjectName(_fromUtf8("button_c"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 30, 481, 91))
        self.frame_3.setStyleSheet(_fromUtf8("background-color:#F8F6EA\n"
""))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.inputNumber = QtGui.QLineEdit(self.frame_3)
        self.inputNumber.setGeometry(QtCore.QRect(110, 0, 371, 91))
        self.inputNumber.setStyleSheet(_fromUtf8("background-color:#F8F6EA;\n"
"border: none;\n"
"text-align: center;\n"
"color: #231F20;\n"
"font-size:60px;    "))
        self.inputNumber.setObjectName(_fromUtf8("inputNumber"))
        self.resultado = QtGui.QPushButton(self.frame_3)
        self.resultado.setGeometry(QtCore.QRect(20, 20, 61, 51))
        self.resultado.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resultado.setStyleSheet(_fromUtf8("background-color:#F90;\n"
"border-radius:4px;\n"
"color:#f4f4f4;\n"
"font-size: 20px;\n"
"font-family: Courier;\n"
"font-weight:bold;\n"
"cursor: pointer;"))
        self.resultado.setObjectName(_fromUtf8("resultado"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.button_c, QtCore.SIGNAL(_fromUtf8("clicked()")), self.inputNumber.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vibora by CarMoreno", None))
        self.button7.setText(_translate("MainWindow", "7", None))
        self.button9.setText(_translate("MainWindow", "9", None))
        self.button8.setText(_translate("MainWindow", "8", None))
        self.button_decimal.setText(_translate("MainWindow", ".", None))
        self.button4.setText(_translate("MainWindow", "4", None))
        self.button1.setText(_translate("MainWindow", "1", None))
        self.button5.setText(_translate("MainWindow", "5", None))
        self.button2.setText(_translate("MainWindow", "2", None))
        self.button6.setText(_translate("MainWindow", "6", None))
        self.button3.setText(_translate("MainWindow", "3", None))
        self.button0.setText(_translate("MainWindow", "0", None))
        self.button_erase.setText(_translate("MainWindow", "⌫", None))
        self.multiplicacion.setText(_translate("MainWindow", "X", None))
        self.suma.setText(_translate("MainWindow", "+", None))
        self.resta.setText(_translate("MainWindow", "-", None))
        self.division.setText(_translate("MainWindow", "÷", None))
        self.button_c.setText(_translate("MainWindow", "C", None))
        self.resultado.setText(_translate("MainWindow", "=", None))

