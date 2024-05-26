from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QMessageBox


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = None

    def open_connection(self):

        if self.con is None:
            print(self.con)
            self.con = QSqlDatabase.addDatabase("QSQLITE")
            self.con.setDatabaseName(self.db_name)
            print(self.con.isOpen())
        if not self.con.open():
            QMessageBox.critical(
                None,
                "Database Error",
                f"Database Error: {self.con.lastError().databaseText()}",
            )
            print('no_con')
            return False
        print(self.con.isOpen())
        print('con')
        return True

    def close_connection(self):
        if self.con is not None:
            self.con.close()
            print('con_closed')


class FileCatalog(DatabaseConnection):
    def __init__(self, db_name=None):
        super().__init__(db_name)
        self.query = QSqlQuery()

    def create_table(self):
        query = """
        CREATE TABLE file_catalog(
            id INTEGER PRIMARY KEY,
            file_name TEXT,
            created_at TEXT,
            update_at TEXT
        );
        """

        if self.query.exec(query):
            print('Таблица file_catalog успешно создана')
            self.query.clear()
            # self.close_connection()
        else:
            print('Данные file_catalog не сохранены')


class ModelSetting(DatabaseConnection):
    def __init__(self, db_name=None):
        super().__init__(db_name)
        self.query = QSqlQuery()

    def create_table(self):
        query = """
            CREATE TABLE catalog_path(
            id INTEGER PRIMARY KEY,
            storage_catalog TEXT,
            target_catalog TEXT
            );
        """
        if self.query.exec(query):
            print('Таблица file_catalog успешно создана')
            # self.close_connection()
        else:
            print('Данные catalog_path не сохранены')

    def save_directory(self, file_directory):
        self.query.exec("SELECT storage_catalog FROM catalog_path LIMIT 1")
        exists = self.query.next()

        if exists:
            # Если данные есть, обновляем их
            self.query.prepare("UPDATE catalog_path SET storage_catalog = ?")
        else:
            # Если данных нет, вставляем новые
            self.query.prepare("INSERT INTO catalog_path (storage_catalog) VALUES (?)")

        self.query.addBindValue(file_directory)

        # Выполняем запрос
        if self.query.exec():
            print('Операция успешно выполнена')
        else:
            print('Ошибка при выполнении операции:', self.query.lastError().text())
