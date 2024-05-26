import os
import yadisk
from config.settings import YANDEX_TOKEN

y = yadisk.Client(id="CLIENT_ID", secret="CLIENT_SECRET")
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'OAuth {YANDEX_TOKEN}'
}


def check_directory_changes(directory='/home/oem/Изображения/'):
    current_files = os.listdir(directory)

    if hasattr(check_directory_changes, 'previous_files'):
        previous_files = getattr(check_directory_changes, 'previous_files')
    else:
        setattr(check_directory_changes, 'previous_files', current_files)
        return

    added_files = set(current_files) - set(previous_files)
    removed_files = set(previous_files) - set(current_files)

    if added_files:
        # y.download(folder_name, headers=headers)
        print("Added files:", added_files)

    if removed_files:
        print("Removed files:", removed_files)

    setattr(check_directory_changes, 'previous_files', current_files)
