# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_form import Ui_MainWindow
import resources_rc


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)



		self.pushButton.clicked.connect(self.add)
		self.label.setScaledContents(True)
		self.label.setFixedSize(400, 250)


	def add(self):

		if self.checkBox.isChecked():
			QMessageBox.information(self, "Ураа", "Спасибо большое!!!!!!!!!")
		else:
			QMessageBox.information(self, "(((", "Эх, ну мы сами виноваты")


if __name__ == "__main__":
	app = QApplication([])
	with open("style.qss", "r") as f:
		app.setStyleSheet(f.read())
	window = MainWindow()
	window.show()
	sys.exit(app.exec())
