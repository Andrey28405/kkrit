# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rg_client.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(532, 391)
        dialog.setStyleSheet(u"\n"
"QDialog{\n"
"	background-color: rgb(42, 74, 46)\n"
"}\n"
"#stackedWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2xp solid gray;\n"
"	border-radius: 20xp;\n"
"}\n"
"")
        self.stackedWidget = QStackedWidget(dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 20, 471, 351))
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.layoutWidget = QWidget(self.page_0)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 25, 441, 231))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.full_name = QLineEdit(self.layoutWidget)
        self.full_name.setObjectName(u"full_name")

        self.verticalLayout.addWidget(self.full_name)

        self.passport = QLineEdit(self.layoutWidget)
        self.passport.setObjectName(u"passport")

        self.verticalLayout.addWidget(self.passport)

        self.phone = QLineEdit(self.layoutWidget)
        self.phone.setObjectName(u"phone")

        self.verticalLayout.addWidget(self.phone)

        self.email = QLineEdit(self.layoutWidget)
        self.email.setObjectName(u"email")

        self.verticalLayout.addWidget(self.email)

        self.address = QLineEdit(self.layoutWidget)
        self.address.setObjectName(u"address")

        self.verticalLayout.addWidget(self.address)

        self.layoutWidget1 = QWidget(self.page_0)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(250, 305, 201, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.otmen = QPushButton(self.layoutWidget1)
        self.otmen.setObjectName(u"otmen")

        self.horizontalLayout.addWidget(self.otmen)

        self.dall = QPushButton(self.layoutWidget1)
        self.dall.setObjectName(u"dall")

        self.horizontalLayout.addWidget(self.dall)

        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.widget = QWidget(self.page_1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, 9, 471, 180))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.power = QLineEdit(self.widget)
        self.power.setObjectName(u"power")

        self.gridLayout_2.addWidget(self.power, 10, 0, 1, 2)

        self.brand = QLineEdit(self.widget)
        self.brand.setObjectName(u"brand")
        self.brand.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.brand, 1, 0, 1, 2)

        self.reg_number = QLineEdit(self.widget)
        self.reg_number.setObjectName(u"reg_number")

        self.gridLayout_2.addWidget(self.reg_number, 8, 0, 1, 2)

        self.model = QLineEdit(self.widget)
        self.model.setObjectName(u"model")

        self.gridLayout_2.addWidget(self.model, 3, 0, 1, 2)

        self.yearIssue = QLineEdit(self.widget)
        self.yearIssue.setObjectName(u"yearIssue")

        self.gridLayout_2.addWidget(self.yearIssue, 9, 0, 1, 2)

        self.VIN = QLineEdit(self.widget)
        self.VIN.setObjectName(u"VIN")

        self.gridLayout_2.addWidget(self.VIN, 5, 0, 1, 2)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(260, 280, 201, 71))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tpy = QPushButton(self.frame)
        self.tpy.setObjectName(u"tpy")

        self.horizontalLayout_2.addWidget(self.tpy)

        self.dali = QPushButton(self.frame)
        self.dali.setObjectName(u"dali")

        self.horizontalLayout_2.addWidget(self.dali)

        self.layoutWidget2 = QWidget(self.page_1)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(9, 182, 451, 101))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.type = QComboBox(self.layoutWidget2)
        self.type.setObjectName(u"type")

        self.verticalLayout_2.addWidget(self.type)

        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.category = QComboBox(self.layoutWidget2)
        self.category.setObjectName(u"category")

        self.verticalLayout_2.addWidget(self.category)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.dateEdit = QDateEdit(self.page_2)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_3.addWidget(self.dateEdit)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.dateEdit_2 = QDateEdit(self.page_2)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.verticalLayout_3.addWidget(self.dateEdit_2)

        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(170, 0, 281, 44))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tpy_2 = QPushButton(self.frame_2)
        self.tpy_2.setObjectName(u"tpy_2")

        self.horizontalLayout_3.addWidget(self.tpy_2)

        self.cox = QPushButton(self.frame_2)
        self.cox.setObjectName(u"cox")

        self.horizontalLayout_3.addWidget(self.cox)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430 ", None))
        self.full_name.setPlaceholderText(QCoreApplication.translate("dialog", u"\u0424\u0418\u041e", None))
        self.passport.setPlaceholderText(QCoreApplication.translate("dialog", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442 \u0420\u0424", None))
        self.phone.setPlaceholderText(QCoreApplication.translate("dialog", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.email.setPlaceholderText(QCoreApplication.translate("dialog", u"email", None))
        self.address.setPlaceholderText(QCoreApplication.translate("dialog", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.otmen.setText(QCoreApplication.translate("dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.dall.setText(QCoreApplication.translate("dialog", u"\u0414\u0430\u043b\u044c\u0448\u0435", None))
        self.power.setPlaceholderText(QCoreApplication.translate("dialog", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.brand.setPlaceholderText(QCoreApplication.translate("dialog", u"\u041c\u0430\u0440\u043a\u0430 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.reg_number.setPlaceholderText(QCoreApplication.translate("dialog", u"\u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.model.setPlaceholderText(QCoreApplication.translate("dialog", u"\u041c\u043e\u0434\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.yearIssue.setPlaceholderText(QCoreApplication.translate("dialog", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.VIN.setPlaceholderText(QCoreApplication.translate("dialog", u"VIN-\u041d\u043e\u043c\u0435\u0440 \u0430\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.tpy.setText(QCoreApplication.translate("dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.dali.setText(QCoreApplication.translate("dialog", u"\u0414\u0430\u043b\u044c\u0448\u0435", None))
        self.label.setText(QCoreApplication.translate("dialog", u"\u0422\u0438\u043f \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
#if QT_CONFIG(whatsthis)
        self.type.setWhatsThis(QCoreApplication.translate("dialog", u"<html><head/><body><p>\u0422\u0438\u043f \u0430\u0432\u0442\u043e</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0422\u0421", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043f\u043e\u043b\u0438\u0441\u0430", None))
        self.label_4.setText(QCoreApplication.translate("dialog", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043f\u043e\u043b\u0438\u0441\u0430", None))
        self.label_6.setText(QCoreApplication.translate("dialog", u"\u0421\u0442\u0440\u043e\u0445\u043e\u0432\u0430\u044f \u0441\u0443\u043c\u043c\u0430: ", None))
        self.label_5.setText(QCoreApplication.translate("dialog", u"\u0421\u0442\u0440\u043e\u0445\u043e\u0432\u0430\u044f \u043f\u0440\u0435\u043c\u0438\u044f", None))
        self.tpy_2.setText(QCoreApplication.translate("dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.cox.setText(QCoreApplication.translate("dialog", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044e", None))
    # retranslateUi

