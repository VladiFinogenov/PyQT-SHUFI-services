from PyQt6 import QtWidgets
from gui.main_window import MainWindow, scheduler


if __name__ == "__main__":
    import sys
    scheduler.start()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
