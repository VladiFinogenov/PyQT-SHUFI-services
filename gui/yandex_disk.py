import yadisk
import os
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QFileDialog

from config.settings import YANDEX_TOKEN, CLIENT_SECRET, CLIENT_ID


URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {YANDEX_TOKEN}'}


class YandexDiskManager(QObject):

    def __init__(self):
        super().__init__()
        self.yadisk = yadisk.Client(id="CLIENT_ID", secret="CLIENT_SECRET")
        self.header = headers

    def download_file(self, file_path, save_path):
        self.yadisk.download(file_path, save_path)
        self.download_signal.emit(file_path, save_path)

    def upload_file(self, local_file_path, remote_path):
        self.yadisk.upload(local_file_path, remote_path)
        self.upload_signal.emit(local_file_path, remote_path)

    def create_directory(self, local_file_path="/test1"):
        self.yadisk.mkdir(path=local_file_path, headers=self.header)
        self.create_directory_signal.emit(local_file_path)
        self.yadisk.close()
        print('кнопка создать директорию')

    def delete(self, path):
        self.yadisk.remove(path)

    def get_disk_info(self):
        info = self.yadisk.get_disk_info()
        return info

    def reload(self, path):
        pass

    # download_signal = pyqtSignal(str, str)
    # upload_signal = pyqtSignal(str, str)
    # create_directory_signal = pyqtSignal(str)
    # delete_file_signal = pyqtSignal(str)
    # get_file_info_signal = pyqtSignal(str)


    def open_directory_disk(self):
        folders_info = self.yadisk.listdir('/', headers=self.header)

        for item in folders_info:
            if item['type'] == 'dir':
                print(f'Каталог: {item["name"]}')
                index = self.model.index('/')
                if index.isValid():
                    child_index = self.model.index(self.model.rowCount(index), 0, index)
                    self.model.setData(child_index, item["name"])

    def on_treeView_clicked(self, index):
        item_path = self.model.filePath(index)
        print(f'Выбран путь: {item_path}')


def select_directory(self):
    # Открытие диалога выбора директории
    dir_path = QFileDialog.getExistingDirectory(self, "Выберите каталог")
    if dir_path:
        self.textBrowser_2.setText(f'{dir_path}')
        # Получение информации о файлах и подкаталогах
        file_count, total_size = self.get_dir_info(dir_path)
        print(file_count, total_size)
        # Обновление интерфейса
        self.fileCountLabel.setText(f'{file_count}')
        self.totalSizeLabel.setText(f'{total_size} байт')


def get_dir_info(self, dir_path):
    total_size = 0
    file_count = 0
    for root, dirs, files in os.walk(dir_path):
        file_count += len(files)
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return file_count, total_size