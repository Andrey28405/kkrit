# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(287, 188)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.image = QLabel(Dialog)
        self.image.setObjectName(u"image")

        self.gridLayout.addWidget(self.image, 0, 2, 1, 2)

        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 2)

        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.image.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0441", None))
    # retranslateUi

