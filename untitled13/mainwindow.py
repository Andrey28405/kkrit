import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox, QListWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtCore import Qt

from ui_form import Ui_MainWindow
from ui_Widget import Ui_Widget as Ui_BurgerWidget
from ui_dialog import Ui_Dialog as Ui_OrderDialog
class BurgerWidget(QWidget, Ui_BurgerWidget):
	def __init__(self, burger_id, name, image_path, price):
		super().__init__()
		self.setupUi(self)
		self.burger_id = burger_id
		self.image_path = image_path
		self.label_name.setText(name)
		self.label_price.setText(f"{price} ₽")
		self.label_image.setPixmap(QPixmap(image_path).scaled(150, 150, Qt.KeepAspectRatio))

		self.mousePressEvent = lambda event: self.showOrderDialog()

	def showOrderDialog(self):
		dialog = OrderDialog(self.burger_id, self.image_path, parent=self)
		dialog.exec()

class OrderDialog(QDialog, Ui_OrderDialog):
	def __init__(self, burger_id, image_path, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.burger_id = burger_id
		self.image.setPixmap(QPixmap(image_path).scaled(200, 200, Qt.KeepAspectRatio))
		self.loadWeights()
		self.loadAdditives()

		self.buttonBox.accepted.connect(self.calculateTotal)

	def loadWeights(self):
		query = QSqlQuery("SELECT weight, price_w FROM weights")
		while query.next():
			w_name = query.value(0)
			w_price = query.value(1)
			self.comboBox.addItem(f"{w_name} (+{w_price}₽)", w_price)

	def loadAdditives(self):
		query = QSqlQuery("SELECT name, price FROM additives")
		while query.next():
			name = query.value(0)
			price = query.value(1)
			item = QListWidgetItem(f"{name} (+{price}₽)")
			item.setData(Qt.UserRole, price) # Сохраняем цену внутри айтема
			item.setCheckState(Qt.Unchecked)
			self.listWidget.addItem(item)

	def calculateTotal(self):
		query = QSqlQuery()
		query.prepare("SELECT base_price FROM food WHERE id = ?")
		query.addBindValue(self.burger_id)
		query.exec()

		if query.next():
			total = query.value(0)
		else:
			return

		total += self.comboBox.currentData()

		selected_names = []
		for i in range(self.listWidget.count()):
			item = self.listWidget.item(i)
			if item.checkState() == Qt.Checked:
				total += item.data(Qt.UserRole)
				selected_names.append(item.text().split(" (")[0])
		count = self.spinBox.value()
		final_sum = total * count

		summary = f"Бургер: {count} шт.\nДобавки: {', '.join(selected_names) if selected_names else 'нет'}\nИтого: {final_sum} ₽"
		QMessageBox.information(self, "Заказ оформлен", summary)

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.scrollAreaWidgetContents.setLayout(self.gridLayout)
		self.db = QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName("Wood.db")

		if not self.db.open():
			QMessageBox.critical(self, "Ошибка", "Не удалось открыть Wood.db")
			return

		self.load_burgers()

	def load_burgers(self):
		query = QSqlQuery("SELECT id, name, image_path, base_price FROM food")
		row, col = 0, 0
		max_col = 3

		while query.next():
			b_id = query.value(0)
			name = query.value(1)
			img = query.value(2)
			price = query.value(3)

			widget = BurgerWidget(b_id, name, img, price)
			self.gridLayout.addWidget(widget, row, col)

			col += 1
			if col >= max_col:
				col = 0
				row += 1

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())
