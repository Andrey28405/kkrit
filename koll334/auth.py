from PySide6.QtWidgets import QDialog, QMessageBox
from ui_auth import Ui_Dialog
import mysql.connector
from mysql.connector import Error

class LoginDialog(QDialog, Ui_Dialog):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.db_config = {
		    "host": "localhost",
			"user": "root",
			"password": "12345",
			"database": "bd_strohovka2",
			"auth_plugin":'mysql_native_password'
			}


		self.btn.clicked.connect(self.check_auth)

	def check_auth(self):
		login = self.login_input.text().strip()
		password = self.pass_input.text().strip()

		if not login or not password:
			QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")
			return

		connection = None
		try:
			connection = mysql.connector.connect(**self.db_config)
			cursor = connection.cursor()

			query = "SELECT * FROM Accounts WHERE login = %s AND password = %s"
			cursor.execute(query, (login, password))

			if cursor.fetchone():
				self.accept()
			else:
				QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

		except Error as err:
			QMessageBox.critical(self, "Ошибка БД", f"Не удалось подключиться к базе данных: {err}")
			print(f"Полный текст ошибки: {err}")

		finally:
			if connection and connection.is_connected():
				cursor.close()
				connection.close()
