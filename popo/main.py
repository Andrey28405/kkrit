import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QDate

from ui_main import Ui_MainWindow
from ui_dialog import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.pushButton_add.clicked.connect(self.open_add_dialog)
		self.pushButton_edit.clicked.connect(self.open_edit_dialog)
		self.pushButton_delete.clicked.connect(self.delete_row)

	def open_add_dialog(self):
		dialog = FormDialog()

		if dialog.exec():
			name, surname, birth = dialog.get_data()

			if not name or not surname:
				QMessageBox.warning(self, "Ошибка", "Поля не должны быть пустыми")
				return

			self.add_row(name, surname, birth)

	def add_row(self, name, surname, birth):
		row = self.tableWidget.rowCount()
		self.tableWidget.insertRow(row)

		self.tableWidget.setItem(row, 0, QTableWidgetItem(name))
		self.tableWidget.setItem(row, 1, QTableWidgetItem(surname))
		self.tableWidget.setItem(row, 2, QTableWidgetItem(birth))

		self.tableWidget.selectRow(row)

	def open_edit_dialog(self):
		row = self.tableWidget.currentRow()

		if row == -1:
			QMessageBox.warning(self, "Ошибка", "Выберите строку")
			return

		name = self.tableWidget.item(row, 0).text()
		surname = self.tableWidget.item(row, 1).text()
		birth = self.tableWidget.item(row, 2).text()

		dialog = FormDialog()
		dialog.set_data(name, surname, birth)

		if dialog.exec():
			new_name, new_surname, new_birth = dialog.get_data()

			if not new_name or not new_surname:
				QMessageBox.warning(self, "Ошибка", "Поля не должны быть пустыми")
				return

			self.update_row(row, new_name, new_surname, new_birth)

	def update_row(self, row, name, surname, birth):
		self.tableWidget.setItem(row, 0, QTableWidgetItem(name))
		self.tableWidget.setItem(row, 1, QTableWidgetItem(surname))
		self.tableWidget.setItem(row, 2, QTableWidgetItem(birth))

	def delete_row(self):
		row = self.tableWidget.currentRow()
		if row == -1:
			QMessageBox.warning(self, "Ошибка", "Выберите строку")
			return

		reply = QMessageBox.question(self,"Подтверждение","Удалить запись?",QMessageBox.Yes | QMessageBox.No)

		if reply == QMessageBox.Yes:
			self.tableWidget.removeRow(row)


class FormDialog(QDialog, Ui_Dialog):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

	def get_data(self):
		name = self.lineEdit_name.text()
		surname = self.lineEdit_surname.text()
		birth = self.dateEdit_birth.date().toString("yyyy-MM-dd")
		return name, surname, birth

	def set_data(self, name, surname, birth):
		self.lineEdit_name.setText(name)
		self.lineEdit_surname.setText(surname)
		self.dateEdit_birth.setDate(QDate.fromString(birth, "yyyy-MM-dd"))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = MainWindow()  # Исправлено: добавлены скобки
	widget.show()
	sys.exit(app.exec())
