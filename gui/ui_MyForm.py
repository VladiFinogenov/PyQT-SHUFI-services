# Form implementation generated from reading ui file 'main_window2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 624)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_dir_pc = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_dir_pc.setGeometry(QtCore.QRect(260, 30, 531, 61))
        self.text_dir_pc.setObjectName("text_dir_pc")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 200, 231, 81))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 201, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 330, 67, 17))
        self.label_2.setObjectName("label_2")
        self.text_dir_disk = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_dir_disk.setGeometry(QtCore.QRect(260, 110, 531, 61))
        self.text_dir_disk.setObjectName("text_dir_disk")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 191, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 320, 161, 41))
        self.label_4.setObjectName("label_4")
        self.used_disk_space = QtWidgets.QLabel(parent=self.centralwidget)
        self.used_disk_space.setGeometry(QtCore.QRect(40, 370, 181, 31))
        self.used_disk_space.setObjectName("used_disk_space")
        self.disk_size = QtWidgets.QLabel(parent=self.centralwidget)
        self.disk_size.setGeometry(QtCore.QRect(40, 430, 181, 31))
        self.disk_size.setObjectName("disk_size")
        self.disk_size_lcd = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.disk_size_lcd.setGeometry(QtCore.QRect(240, 420, 121, 31))
        self.disk_size_lcd.setObjectName("disk_size_lcd")
        self.used_disk_space_lcd = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.used_disk_space_lcd.setGeometry(QtCore.QRect(240, 370, 121, 31))
        self.used_disk_space_lcd.setObjectName("used_disk_space_lcd")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(490, 350, 271, 192))
        self.textBrowser_3.setObjectName("textBrowser_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 22))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_7 = QtWidgets.QMenu(parent=self.menu_3)
        self.menu_7.setObjectName("menu_7")
        self.menu_4 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_4.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.menu_4.setObjectName("menu_4")
        self.menu_1 = QtWidgets.QMenu(parent=self.menu_4)
        self.menu_1.setObjectName("menu_1")
        self.menu_5 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_6.setObjectName("menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.create_dir = QtGui.QAction(parent=MainWindow)
        self.create_dir.setObjectName("create_dir")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtGui.QAction(parent=MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtGui.QAction(parent=MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtGui.QAction(parent=MainWindow)
        self.action_9.setObjectName("action_9")
        self.select_dir_action = QtGui.QAction(parent=MainWindow)
        self.select_dir_action.setObjectName("select_dir_action")
        self.select_dir_action1 = QtGui.QAction(parent=MainWindow)
        self.select_dir_action1.setObjectName("select_dir_action1")
        self.disk_info = QtGui.QAction(parent=MainWindow)
        self.disk_info.setObjectName("disk_info")
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action2 = QtGui.QAction(parent=MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtGui.QAction(parent=MainWindow)
        self.action3.setObjectName("action3")
        self.menu_2.addAction(self.action_5)
        self.menu_7.addAction(self.action_8)
        self.menu_7.addAction(self.action_7)
        self.menu_7.addAction(self.action_6)
        self.menu_7.addAction(self.create_dir)
        self.menu_3.addAction(self.action_9)
        self.menu_3.addAction(self.menu_7.menuAction())
        self.menu_1.addAction(self.action3)
        self.menu_1.addAction(self.action2)
        self.menu_4.addAction(self.menu_1.menuAction())
        self.menu_5.addAction(self.disk_info)
        self.menu_6.addAction(self.select_dir_action)
        self.menu_6.addAction(self.select_dir_action1)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Включить автосканирование"))
        self.label.setText(_translate("MainWindow", "Выбранная директория на \n"
"ПК:"))
        self.label_2.setText(_translate("MainWindow", "Логи"))
        self.label_3.setText(_translate("MainWindow", "Директория для записи на \n"
"Яндекс диске"))
        self.label_4.setText(_translate("MainWindow", "Информация о диске:"))
        self.used_disk_space.setText(_translate("MainWindow", "Занятое место на диске:"))
        self.disk_size.setText(_translate("MainWindow", "Размер диска (ГБ):"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_3.setTitle(_translate("MainWindow", "Я.Диск"))
        self.menu_7.setTitle(_translate("MainWindow", "действие"))
        self.menu_4.setTitle(_translate("MainWindow", "Справка"))
        self.menu_1.setTitle(_translate("MainWindow", "справка1"))
        self.menu_5.setTitle(_translate("MainWindow", "информация о диске"))
        self.menu_6.setTitle(_translate("MainWindow", "выбор директорий"))
        self.create_dir.setText(_translate("MainWindow", "создать папку"))
        self.action_5.setText(_translate("MainWindow", "таймер сканирования"))
        self.action_6.setText(_translate("MainWindow", "Скачать файл"))
        self.action_7.setText(_translate("MainWindow", "Загрузить файл"))
        self.action_8.setText(_translate("MainWindow", "Удаление файла или папки"))
        self.action_9.setText(_translate("MainWindow", "очистка корзины"))
        self.select_dir_action.setText(_translate("MainWindow", "выбрать директорию на ПК"))
        self.select_dir_action1.setText(_translate("MainWindow", "выбрать директорию на диске"))
        self.disk_info.setText(_translate("MainWindow", "обновить информацию о диске"))
        self.action.setText(_translate("MainWindow", "справка"))
        self.action2.setText(_translate("MainWindow", "2 словарь"))
        self.action3.setText(_translate("MainWindow", "3 словар"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
