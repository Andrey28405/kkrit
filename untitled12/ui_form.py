# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(471, 545)
        MainWindow.setStyleSheet(u"background-color: #99CCFF;\n"
"border: 2px solid #99CCFF;\n"
"border-radius: 5px;\n"
"\n"
"color: white;\n"
"font-size: 14px;\n"
"font-weight: Times New Roman;\n"
"text-align: center;\n"
"\n"
"QPushButton: {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 421, 221))
        self.label.setMinimumSize(QSize(421, 0))
        self.label.setPixmap(QPixmap(u":/images/images/logo.jpeg"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 410, 221, 71))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(50, 300, 181, 51))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(250, 310, 211, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 471, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043d", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u042d\u0442\u043e", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0436\u043d\u043e", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0442\u0438\u0442\u044c \u0437\u0430 \u043f\u043e\u0437\u0434\u043d\u044e\u044e \u0441\u0434\u0430\u0447\u0443", None))
    # retranslateUi

