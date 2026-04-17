# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_form import Ui_MainWindow
import resources_rc


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.add)
		self.ui.label.setScaledContents(True)
		self.ui.label.setFixedSize(400, 250)
		try:
			with open("style.qss", "r", encoding="utf-8") as f:
				self.setStyleSheet(f.read())
		except FileNotFoundError:
			print("Файл style.qss не найден!")

	def add(self):

		if self.ui.checkBox.isChecked():
			QMessageBox.information(self, "Ураа", "Спасибо большое!!!!!!!!!")
		else:
			QMessageBox.information(self, "(((", "Эх, ну мы сами виноваты")


if __name__ == "__main__":
	app = QApplication([])
	window = MainWindow()
	window.show()
	sys.exit(app.exec())
