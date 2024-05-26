from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem


class TableModel:
    def __init__(self, tableWidget: QTableWidget):
        self.tableWidget = tableWidget
        self.setupTable()

    def setupTable(self):
        # Задание параметров таблицы
        self.tableWidget.setColumnCount(5)
        title = ["Catalog Path", "Yandex Disk Path", "File Name", "Date Added", "Date Modified"]
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.update_table()

    def add_directory_to_db(self, dir_path):
        # Запись пути к директории в базу данных
        query = QSqlQuery("database2.db")
        query = QSqlQuery()
        query.prepare(
            f"""
            INSERT INTO catalog_table (catalog_path)
            VALUES ('{dir_path}')
            """
        )
        query.bindValue(":dir_path", dir_path)
        query.exec()

    def update_table(self):
        # Обновление таблицы данными из базы данных
        query = QSqlQuery()

        # Выполнение запроса на выборку всех данных, кроме столбца id
        if query.exec(
                "SELECT storage_catalog FROM catalog_path"):
            print("Данные успешно получены View")

            # Очистка таблицы перед заполнением новыми данными
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            column_count = query.record().count()
            row = 0
            while query.next():
                self.tableWidget.insertRow(row)  # Создание новой строки
                for column in range(column_count):
                    # Получение данных из каждого столбца, кроме id
                    item = QTableWidgetItem(str(query.value(column)))
                    self.tableWidget.setItem(row, column, item)
                row += 1
            self.tableWidget.update()  # Обновление интерфейса
        else:
            print("Ошибка при получении данных View:", query.lastError().text())

