# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(388, 544)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.box = QComboBox(self.centralwidget)
        self.box.addItem("")
        self.box.addItem("")
        self.box.addItem("")
        self.box.addItem("")
        self.box.setObjectName(u"box")
        self.box.setGeometry(QRect(40, 30, 131, 31))
        self.kolvo = QLineEdit(self.centralwidget)
        self.kolvo.setObjectName(u"kolvo")
        self.kolvo.setGeometry(QRect(200, 30, 111, 31))
        self.editT = QTextEdit(self.centralwidget)
        self.editT.setObjectName(u"editT")
        self.editT.setGeometry(QRect(190, 200, 171, 221))
        self.editT.setReadOnly(True)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(40, 292, 91, 19))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(40, 270, 111, 18))
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(40, 315, 91, 18))
        self.cik = QPushButton(self.centralwidget)
        self.cik.setObjectName(u"cik")
        self.cik.setGeometry(QRect(69, 440, 81, 21))
        self.sum = QPushButton(self.centralwidget)
        self.sum.setObjectName(u"sum")
        self.sum.setGeometry(QRect(50, 360, 91, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 10, 81, 16))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 130, 141, 118))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.radioButton)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 180, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 388, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0444\u0435 274(\u20bd)", None))
        self.box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0439 182(\u20bd)", None))
        self.box.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u044d\u043d\u0434\u0432\u0438\u0447 456(\u20bd)", None))
        self.box.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043b\u0430\u0442 548(\u20bd)", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043a\u0435\u0442 (10\u20bd)", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043c\u043e\u043a\u043e\u0434 -10%", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0435\u0432\u044b\u0435 5%", None))
        self.cik.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.sum.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u044b:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430:", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044b\u0447\u043d\u0430\u044f (182\u20bd)", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u0440\u0435\u0441\u0441 (455\u20bd)", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043c\u043e\u0432\u044b\u0432\u043e\u0437 (0\u20bd)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043a:", None))
    # retranslateUi

