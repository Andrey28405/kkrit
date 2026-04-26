# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QDateEdit#, QMessageBox
from PySide6.QtCore import QDate
#import mysql.connector
#from mysql.connector import Error

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
#from ui_info import Ui_Dialog
from ui_client import Ui_dialog as Ui_Client
class RgClient(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Client()
		self.ui.setupUi(self)

		self.ui.stackedWidget.setCurrentIndex(0)

		self.ui.dall.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
		self.ui.dali.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

		self.ui.tpy.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
		self.ui.tpy_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

		self.ui.dateEdit.setDate(QDate.currentDate())
		self.ui.dateEdit.setCalendarPopup(True)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.stackedWidget.setCurrentIndex(0)

		self.ui.btn_main.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
		self.ui.btn_client.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
		self.ui.btn_fromPolicy.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

		self.ui.rgClient.clicked.connect(self.open_rgclient)

	def open_rgclient(self):
		self.rg_client_dialog = RgClient()
		self.rg_client_dialog.exec()










if __name__ == "__main__":
	app = QApplication(sys.argv)

	#login_dlg = LoginDialog()

	#if login_dlg.exec() == LoginDialog.Accepted:
	widget = MainWindow()
	widget.show()
	sys.exit(app.exec())
	#else:
	#	sys.exit()
