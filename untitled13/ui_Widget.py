# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(342, 203)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_image = QLabel(Widget)
        self.label_image.setObjectName(u"label_image")

        self.gridLayout.addWidget(self.label_image, 0, 0, 1, 2)

        self.label_name = QLabel(Widget)
        self.label_name.setObjectName(u"label_name")

        self.gridLayout.addWidget(self.label_name, 1, 0, 1, 1)

        self.label_price = QLabel(Widget)
        self.label_price.setObjectName(u"label_price")

        self.gridLayout.addWidget(self.label_price, 1, 1, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.label_image.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_name.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_price.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
    # retranslateUi

