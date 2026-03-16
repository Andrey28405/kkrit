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

		self.ui.sum.clicked.connect(self.add)
		#self.ui.cik.clicked.connect(self.cikl)\

	def add(self):

		kol = self.ui.kolvo.text()

		try:
			x = (int(kol))
			if x > 0:
				pass
			else:
				self.ui.editT.setText("Подумай ещё раз)")
		except(ValueError, TypeError):
			self.ui.editT.setText("Это не число.")

		tovar = self.ui.box.currentIndex()

		if tovar == 0:
			tov = (int(274))
		elif tovar == 1:
			tov = (int(182))
		elif tovar == 2:
			tov = (int(456))
		else:
			tov = (int(548))

		if self.ui.radioButton.isChecked():
			jop = "Самовывоз"
			io = (int(0))
		elif self.ui.radioButton_2.isChecked():
			jop = "Экспресс"
			io = (int(455))
		else:
			jop = "Обычная"
			io = (int(182))
			self.ui.radioButton_3.setChecked(True)

		rizyl = int((tov * x) + io)

		if self.ui.checkBox.isChecked():
			mod = "Пакет"
			mod_2 = (int(10))
			rizyl = int((tov * x) + io + mod_2)
		else:
			pass
		if self.ui.checkBox_2.isChecked():
			prom = float(1 - 10/100)
			promo = "Ваша скидка 10%"
			rizyl = int((tov * x) * prom)
		#if self.ui.checkBox_3.isChecked():


		self.ui.editT.setText(f"{rizyl}")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
