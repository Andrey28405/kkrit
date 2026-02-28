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

        self.ui.dod.clicked.connect(self.add)
        self.ui.top.clicked.connect(self.add)
        self.ui.del_top.clicked.connect(self.add)
        ##self.ui.cik.clicked.connect(self.cik)
    def add(self):
        name = self.ui.name.text()
        avtor = self.ui.avtor.text()

        if not name:
            self.ui.name.setText("Где название!?")
        else:
            pass
        if not svtor:
            self.ui.avtor.setText("Где автор?!")
        else:
            pass

        got = self.ui.got.text()

        if isinstance(got, int) and 1500 <= got <= 2100:
            pass
        else:
            self.ui.got.setText("Не вероное значение"\n"Число не находится в диапазоне от 1500 до 2100 или не является числом")

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
