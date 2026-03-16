# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.ozi.clicked.connect(self.cik)
		self.ui.rya.clicked.connect(self.add)

	def add(self):

		name = str(self.ui.name.text())
		email = str(self.ui.email.text())
		tema = str(self.ui.box.currentText())
		soo = str(self.ui.soo.toPlainText())


		if self.ui.checkBox.isChecked():
			kol = 'ДА'
		else:
			kol = 'НЕТ'
		if self.ui.checkBox_2.isChecked():
			kolp = 'ДА'
		else:
			kolp = 'НЕТ'

		if self.ui.radioButton_2.isChecked():
			jop = "Отлично"
		elif self.ui.radioButton_3.isChecked():
			jop = "Плохо"
		else:
			jop = "Нормально"
			self.ui.radioButton.setChecked(True)
		if not self.ui.checkBox_3.isChecked():
			self.ui.editT.setPlainText("Ошибка: необходимо согласиться на обработку данных.")
			return

		edit = (
		    f"Имя: {name}\n"
			f"Email: {email}\n"
			f"Тема: {tema}\n"
			f"Оценка: {jop}\n"
			f"Параметры:\n"
			"\n"
			f"-Отправить копию на email: {kol}\n"
			f"-Срочно: {kolp}\n"
			"\n"
			f"Сообщение: {soo}"
			)

		self.ui.editT.setText(edit)

	def cik(self):
		self.ui.editT.clear()

		self.ui.soo.clear()
		self.ui.name.clear()
		self.ui.email.clear()
		self.ui.box.clear()

		self.ui.radioButton.setChecked(True)

		self.ui.checkBox.setChecked(False)
		self.ui.checkBox_2.setChecked(False)
		self.ui.checkBox_3.setChecked(False)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = MainWindow()
	widget.show()
	sys.exit(app.exec())
