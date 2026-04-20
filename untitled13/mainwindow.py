# This Python file uses the following encoding: utf-8
import sys
import sqlite3

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QDialog


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_Widget import Ui_Widget
from ui_dialog import Ui_Dialog
class BurgerWidget(QWidget, Ui_Widget):
	def __init__(self, burger_id, name, path, price):
		super().__init__()
		self.setupUi(self)
		self.burger_id = burger_id
		self.path = path
		self.label_name.setText(name)
		self.label_image.setPixmap(QPixmap(path).scaled(150,150))
		self.label_price.setText(str(f"{price} ₽"))

		self.mouserPressEvent = lambda event: self.showDialog()
	def showDialog(self):
		dialog = Dialog(self.burger_id,self.path,self)
		dialog.exec()

class Dialog(QDialog, Ui_Dialog):
	def __init__(self, burger_id, path):
		super().__init__()
		self.setupUi(self)
		self.burger_id = burger_id
		self.image.setPixmap(QPixmap(path).scaled(150,150))

		self.conn = sqlite3.connect("Wood.db")
		self.cursor = self.conn.cursor()

		self.loadWeights()
		self.loadAdditives()
		self.buttonBox.accepted.connect(self.calculateTotal)

	def loadWeights(self):
		query = "SELECT weight, price_w FROM weights ORDER BY weight ASC;"
		self.cursor.execute(query)
		weights = self.cursor.fetchall()

		for weight, price in weights:
			self.ComboBox.addItem(f"{weight} гр (+{price} руб)", price)

	def loadAdditives(self):
		query = "SELECT name, price FROM additives ORDER BY name ASC;"
		self.cursor.execute(query)
		additives = self.cursor.fetchall()

		for name, price in additives:
			item = QListWidgetItem(f"{name} (+{price} руб)")
			item.setCheckState(Qt.Unchecked)
			self.additivesList.addItem(item)

	def calculateTotal(self):
		query = "SELECT base_price FROM food WHERE id=?;"
		self.cursor.execute(query, (self.food_id,))
		base_price = self.cursor.fetchone()[0]

		weight_price = self.weightComboBox.currentData()
		if weight_price is None:
			weight_price = 0

		extra_cost = 0
		for i in range(self.additivesList.count()):
			item = self.additivesList.item(i)
			if item.checkState() == Qt.Checked:
				price = float(item.text().split("(")[1].strip(" руб)"))
				extra_cost += price

				# Расчет итоговой суммы
		total_price = base_price + weight_price + extra_cost

		       # Сообщаем пользователю итоговую сумму
		QMessageBox.information(self, "Итоговая сумма",f"Ваш заказ: {total_price:.2f} руб.",buttons=QMessageBox.Ok)
		self.conn.close()

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)

		self.scrollAreaWidgetContents.setLayout(self.gridLayout)
		try:
			self.con = sqlite3.connect("Wood.db")
		except sqlite3.Error as e:
			QMessageBox.critical(self, "Критическая ошибка", f"Не удалось открыть базу данных: {e}")
			return
		self.load_burger_data()

	def load_burger_data(self):
		query = "SELECT id, name, image_path, base_price FROM food"
		records = self.con.execute(query).fetchall()

		row, col = 0, 0
		max_col = 3
		for record in records:
			burger_id = record[0]
			name = record[1]
			path = record[2]
			price = record[3]

			burger_widget = BurgerWidget(burger_id, name, path, price)
			self.gridLayout.addWidget(burger_widget, row, col)

			col += 1
			if col >= max_col:
				col = 0
				row += 1









if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
