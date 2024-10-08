###! Проект в разработке.

**Описание проекта:**

# Сервис синхронизации файлов

Программа для синхронизации файлов в фоновом режиме отслеживает изменения файлов 
в указанной директории на компьютере пользователя и автоматически выполняет необходимые 
действия в облачном хранилище Яндекс диска. 

Дополнительно можно выполнять различные операции на Яндекс диске:
- получать информацию о диске;
- получать информацию о файлах;
- создавать директории;
- удалять файлы;
- скачивать файлы;

## Установка в (Linux)

1. Клонирование репозитория.
```git clone https://github.com/VladiFinogenov/PyQT-SHUFI-services.git```

2. Создание виртуального окружения.
```python3 -m venv .venv```

3. Переход в директорию SHUFI-services.
```cd SHUFI-services```

4. Активация виртуального окружения.
```source ./.venv/bin/activate```

5. Установка зависимостей.
```pip3 install -r requirements.txt```
