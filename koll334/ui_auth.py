# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(230, 184)
        Dialog.setStyleSheet(u"QDialog {\n"
"    background-color: #2d2d30;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"\n"
"QLabel#titleLabel {\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"    color: #ffffff;\n"
"    padding: 10px 0;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #444;\n"
"    border-radius: 10px;\n"
"    padding: 8px 12px;\n"
"    font-size: 12px;\n"
"    background-color: #3c3c3c;\n"
"    color: #ffffff;\n"
"    selection-background-color: #007acc;\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #007acc;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton#btn {\n"
"    background-color: #007acc;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 12px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton#btn:hover {\n"
"    background-color: #106ebc;\n"
"}\n"
"\n"
"QPushButton#btn:pressed {\n"
"    background-color: #005aa0;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setTextFormat(Qt.TextFormat.AutoText)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.login_input = QLineEdit(Dialog)
        self.login_input.setObjectName(u"login_input")

        self.verticalLayout.addWidget(self.login_input)

        self.pass_input = QLineEdit(Dialog)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.pass_input)

        self.btn = QPushButton(Dialog)
        self.btn.setObjectName(u"btn")

        self.verticalLayout.addWidget(self.btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0432\u0445\u043e\u0434\u0430:", None))
        self.login_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.pass_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

