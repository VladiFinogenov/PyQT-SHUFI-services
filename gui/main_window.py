import os
import yadisk
# from PyQt6.QtSql import QSqlQuery, QSqlTableModel
from PyQt6.QtWidgets import QFileDialog, QMainWindow, QInputDialog, QMessageBox
from config.settings import YANDEX_TOKEN, CLIENT_SECRET, CLIENT_ID
from PyQt6 import QtWidgets, uic, QtGui
from apscheduler.schedulers.qt import QtScheduler

# import ui_MyForm
from .scheduler import check_directory_changes
from database.model import FileCatalog, ModelSetting, DatabaseConnection
from gui.widgets import TableModel

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'OAuth {YANDEX_TOKEN}'
}


scheduler = QtScheduler()


def format_size(size):
    sizes = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    i = 0
    while size >= 1024 and i < len(sizes)-1:
        size /= 1024
        i += 1
    return "{:3f} {}".format(size, sizes[i])


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

# class MyWindow(QMainWindow, ui_MyForm.Ui_MainWindow):
#     def __init__(self, parent=None):
#         QMainWindow.__init__(self, parent)
#         self.setupUi(self)
#         Загрузка .ui файла напрямую
#         uic.loadUi(r'main_window.ui', self)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(current_dir, 'main_window.ui')
        uic.loadUi(ui_file_path, self)
        self.yadisk = yadisk.Client(id="CLIENT_ID", secret="CLIENT_SECRET")
        self.header = headers

        self.db_connection = DatabaseConnection("database2.db")
        # self.db_file_catalog = FileCatalog()
        # self.db_model_setting = ModelSetting()
        self.initialize_database()

        self.select_dir_action.triggered.connect(self.on_select_directory)
        self.disk_info.triggered.connect(self.get_disk_info)
        self.create_dir.triggered.connect(self.create_mrdir)
        self.scan_timer.triggered.connect(self.hourly_task)

        table = self.tableWidget
        self.model = TableModel(table)

    def initialize_database(self):
        """
        Метод устанавливает соединение с базой данных
        и проверяет были ли созданы таблицы, если нет
        вызывает метод создания таблицы у моделей.
        """

        if self.db_connection.open_connection():
            db_file_catalog = FileCatalog()
            db_model_setting = ModelSetting()

            if ['file_catalog', 'catalog_table'] in self.db_connection.con.tables():
                pass
            else:
                db_file_catalog.create_table()
                db_model_setting.create_table()

    def hourly_task(self):
        """
        Метод вызывает виджет в котором вводится интервал
        времени, после чего передает его и функцию "check_directory_changes"
        в планировщик задач на исполнение.
        """

        value, ok = QInputDialog.getInt(self, 'Interval', 'Enter interval:')
        if ok:
            print('Interval entered:', value)
            scheduler.add_job(func=check_directory_changes, trigger='interval', seconds=10)
            print(scheduler.get_jobs())

    def create_mrdir(self):
        """
        Метод создает диалоговое окно в котором
        нужно ввести имя директории, если имя валидно
        создает директорию на яндекс диске.
        """

        while True:
            folder_name, ok = QInputDialog.getText(
                self,
                'Create Folder', 'Enter folder name:'
            )
            if ok:
                if self.yadisk.is_dir(folder_name, headers=self.header):
                    QMessageBox.information(self, 'Error', 'Такое имя уже существует')
                else:
                    self.yadisk.mkdir(f'/{folder_name}', headers=self.header)
                    self.text_dir_disk.setText(f'/{folder_name}')
                    break
            else:
                break

    def get_disk_info(self):
        """
        Метод получает информацию на яндекс диске.
        total_space: `int`, общий размер диска
        used_space: `int`, объём используемого пространства.
        """

        info = self.yadisk.get_disk_info(headers=self.header)
        if info:
            total_space = str(info.total_space / (1024**3))
            used_space = info.used_space
            self.disk_size_lcd.setText(total_space)
            used_space_formatted = format_size(used_space)
            self.used_disk_space_lcd.setText(used_space_formatted)

    def on_select_directory(self):
        """
        Метод использует диалоговое окно `QFileDialog`
        для выбора директории на компьютере пользователя.
        Если директория выбрана записывает путь в дисплей виджет
        "text_dir_pc" и базу данных
        """

        directory = QFileDialog.getExistingDirectory(self)
        if directory:
            if self.db_connection.open_connection():
                db = ModelSetting()
                db.save_directory(directory)
            self.model.update_table()
            self.text_dir_pc.setText(directory)
