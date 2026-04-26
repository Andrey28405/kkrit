# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(736, 481)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(42, 74, 46, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush2)
        brush3 = QBrush(QColor(127, 127, 127, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush3)
        brush4 = QBrush(QColor(170, 170, 170, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush4)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush2)
        brush5 = QBrush(QColor(255, 255, 220, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush5)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 127))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush6)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush6)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
        brush7 = QBrush(QColor(127, 127, 127, 127))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush2)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#widget{\n"
"	background-color: rgb(42, 74, 46)\n"
"}\n"
"QMainWindow{\n"
"	background-color: rgb(42, 74, 46)\n"
"}\n"
"#stackedWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2xp solid gray;\n"
"	border-radius: 20xp;\n"
"}\n"
"#widget_6{\n"
"	background-color: rgb(42, 74, 46)\n"
"}\n"
"\n"
"#btn_client{\n"
"	background-color: rgb(42, 74, 46);\n"
"	border: 2xp solid gray;\n"
"	border-radius: 20xp;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"#btn_fromPolicy{\n"
"	background-color: rgb(42, 74, 46);\n"
"	border: 2xp solid gray;\n"
"	border-radius: 20xp;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"#btn_main{\n"
"	background-color: rgb(42, 74, 46);\n"
"	border: 2xp solid gray;\n"
"	border-radius: 20xp;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"#btn_pay{\n"
"	background-color: rgb(42, 74, 46);\n"
"	border: 2xp solid gray;\n"
"	border-radius: 20xp;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"")
        MainWindow.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush4)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush5)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush6)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush2)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush6)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush2)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush5)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush2)
#endif
        self.widget.setPalette(palette1)
        self.widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.widget.setStyleSheet(u"background- color: rgb(42, 74, 46)")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.btn_main = QPushButton(self.widget)
        self.btn_main.setObjectName(u"btn_main")
        font = QFont()
        font.setPointSize(9)
        self.btn_main.setFont(font)

        self.verticalLayout.addWidget(self.btn_main, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_client = QPushButton(self.widget)
        self.btn_client.setObjectName(u"btn_client")

        self.verticalLayout.addWidget(self.btn_client, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_fromPolicy = QPushButton(self.widget)
        self.btn_fromPolicy.setObjectName(u"btn_fromPolicy")

        self.verticalLayout.addWidget(self.btn_fromPolicy, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_pay = QPushButton(self.widget)
        self.btn_pay.setObjectName(u"btn_pay")

        self.verticalLayout.addWidget(self.btn_pay, 0, Qt.AlignmentFlag.AlignLeft)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacer)


        self.verticalLayout_3.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.gridLayout_2 = QGridLayout(self.page_0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.page_0)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 40, 711, 20))
        self.listWidget = QListWidget(self.frame)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(300, 70, 241, 331))
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 120, 201, 221))
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush3)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush4)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush5)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush6)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush2)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush3)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush4)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush5)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush6)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush2)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush3)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush3)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush4)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush3)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush3)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush5)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush7)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush2)
#endif
        self.frame_4.setPalette(palette2)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.rgClient = QPushButton(self.frame_4)
        self.rgClient.setObjectName(u"rgClient")

        self.gridLayout_3.addWidget(self.rgClient, 1, 0, 1, 1)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 49, 16))

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label_6 = QLabel(self.page_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 81, 21))
        self.tableWidget = QTableWidget(self.page_1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 200, 551, 261))
        self.widget_2 = QWidget(self.page_1)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 30, 251, 141))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_2.addWidget(self.pushButton_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_9 = QPushButton(self.page_1)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(440, 30, 111, 31))
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 521, 16))
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(310, 40, 221, 171))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.widget_3 = QWidget(self.page_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 240, 561, 181))
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.VIN = QLineEdit(self.widget_3)
        self.VIN.setObjectName(u"VIN")

        self.verticalLayout_6.addWidget(self.VIN)

        self.lineEdit_4 = QLineEdit(self.widget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_6.addWidget(self.lineEdit_4)

        self.lineEdit_6 = QLineEdit(self.widget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_6.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_6.addWidget(self.lineEdit_7)

        self.lineEdit_4.raise_()
        self.label_11.raise_()
        self.lineEdit_6.raise_()
        self.VIN.raise_()
        self.lineEdit_7.raise_()
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 40, 221, 171))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u041e\u041e \"\u0421\u0442\u0440\u043e\u0445\u043e\u0412\u0438\u043a\"", None))
        MainWindow.setWindowFilePath("")
        self.label_4.setText("")
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.btn_client.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.btn_fromPolicy.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u0441\u0430", None))
        self.btn_pay.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0441\u0441\u0430/\u041e\u043f\u043b\u0430\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0437\u0430\u043b\u043e\u0432\u0430\u0442\u044c ....", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem16 = self.listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem17 = self.listWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem18 = self.listWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem19 = self.listWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem20 = self.listWidget.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem21 = self.listWidget.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        ___qlistwidgetitem22 = self.listWidget.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.rgClient.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u0441\u0430", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421\u0410\u0413\u041e", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a\u043e \u044d\u0442\u043e", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.VIN.setInputMask("")
        self.VIN.setText("")
        self.VIN.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VIN:", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0430:", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c:", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0410\u0421\u041a\u041e", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a\u043e \u044d\u0442\u043e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi

