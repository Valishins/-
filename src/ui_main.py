from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 1161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horLay = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horLay.setContentsMargins(0, 0, 0, 0)
        self.horLay.setObjectName("horLay")
        self.id = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.id.setAlignment(QtCore.Qt.AlignCenter)
        self.id.setObjectName("ID")
        self.horLay.addWidget(self.id)
        self.month = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.month.setFont(font)
        self.month.setAlignment(QtCore.Qt.AlignCenter)
        self.month.setObjectName("month")
        self.horLay.addWidget(self.month)
        self.number = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number.setFont(font)
        self.number.setAlignment(QtCore.Qt.AlignCenter)
        self.number.setObjectName("number")
        self.horLay.addWidget(self.number)
        self.item = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.item.setFont(font)
        self.item.setAlignment(QtCore.Qt.AlignCenter)
        self.item.setObjectName("item")
        self.horLay.addWidget(self.item)
        self.group = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.group.setFont(font)
        self.group.setAlignment(QtCore.Qt.AlignCenter)
        self.group.setObjectName("group")
        self.horLay.addWidget(self.group)
        self.classes = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.classes.setFont(font)
        self.classes.setAlignment(QtCore.Qt.AlignCenter)
        self.classes.setObjectName("classes")
        self.horLay.addWidget(self.classes)
        self.week = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.week.setFont(font)
        self.week.setAlignment(QtCore.Qt.AlignCenter)
        self.week.setObjectName("week")
        self.horLay.addWidget(self.week)
        self.who = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.who.setFont(font)
        self.who.setAlignment(QtCore.Qt.AlignCenter)
        self.who.setObjectName("who")
        self.horLay.addWidget(self.who)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 1161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horLay_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horLay_2.setContentsMargins(0, 0, 0, 0)
        self.horLay_2.setObjectName("horLay_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horLay_2.addWidget(self.label)
        self.month_1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.month_1.setFont(font)
        self.month_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.month_1.setObjectName("month_1")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.horLay_2.addWidget(self.month_1)
        self.number_1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_1.setFont(font)
        self.number_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number_1.setObjectName("number_1")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.horLay_2.addWidget(self.number_1)
        self.item_1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.item_1.setFont(font)
        self.item_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_1.setObjectName("item_1")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.horLay_2.addWidget(self.item_1)
        self.group_1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.group_1.setFont(font)
        self.group_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.group_1.setObjectName("group_1")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.horLay_2.addWidget(self.group_1)
        self.classes_1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.classes_1.setFont(font)
        self.classes_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.classes_1.setObjectName("classes_1")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.horLay_2.addWidget(self.classes_1)
        self.week_1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.week_1.setFont(font)
        self.week_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.week_1.setObjectName("week_1")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.horLay_2.addWidget(self.week_1)
        self.who_1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.who_1.setFont(font)
        self.who_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.who_1.setObjectName("who_1")
        self.who_1.addItem("")
        self.who_1.addItem("")
        self.who_1.addItem("")
        self.horLay_2.addWidget(self.who_1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 680, 1161, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horlLay_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horlLay_3.setContentsMargins(0, 0, 0, 0)
        self.horlLay_3.setObjectName("horlLay_3")
        self.openes = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openes.setFont(font)
        self.openes.setObjectName("openes")
        self.horlLay_3.addWidget(self.openes)
        self.exchange = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exchange.setFont(font)
        self.exchange.setObjectName("exchange")
        self.horlLay_3.addWidget(self.exchange)
        self.repear = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.repear.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.repear.setFont(font)
        self.repear.setObjectName("repear")
        self.horlLay_3.addWidget(self.repear)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 160, 1161, 511))
        self.tableView.setObjectName("tableView")
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows);
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection);
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 1161, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FIO = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FIO.setFont(font)
        self.FIO.setObjectName("FIO")
        self.FIO.addItem("")
        self.horizontalLayout.addWidget(self.FIO)
        self.dnev = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dnev.setFont(font)
        self.dnev.setObjectName("dnev")
        self.horizontalLayout.addWidget(self.dnev)
        self.but_ktp = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.but_ktp.setFont(font)
        self.but_ktp.setObjectName("but_ktp")
        self.horizontalLayout.addWidget(self.but_ktp)
        self.but_time = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.but_time.setFont(font)
        self.but_time.setObjectName("but_time")
        self.horizontalLayout.addWidget(self.but_time)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.FIO.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Занятия"))
        self.id.setText(_translate("MainWindow", "ID"))
        self.month.setText(_translate("MainWindow", "Месяц"))
        self.number.setText(_translate("MainWindow", "№ Пары"))
        self.item.setText(_translate("MainWindow", "Предмет"))
        self.group.setText(_translate("MainWindow", "Группа"))
        self.classes.setText(_translate("MainWindow", "Вид занятия"))
        self.week.setText(_translate("MainWindow", "Неделя"))
        self.who.setText(_translate("MainWindow", "Кто"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.month_1.setItemText(0, _translate("MainWindow", "Все"))
        self.month_1.setItemText(1, _translate("MainWindow", "Январь"))
        self.month_1.setItemText(2, _translate("MainWindow", "Февраль"))
        self.month_1.setItemText(3, _translate("MainWindow", "Март"))
        self.month_1.setItemText(4, _translate("MainWindow", "Апрель"))
        self.month_1.setItemText(5, _translate("MainWindow", "Май"))
        self.month_1.setItemText(6, _translate("MainWindow", "Июнь"))
        self.number_1.setItemText(0, _translate("MainWindow", "Все"))
        self.number_1.setItemText(1, _translate("MainWindow", "1"))
        self.number_1.setItemText(2, _translate("MainWindow", "2"))
        self.number_1.setItemText(3, _translate("MainWindow", "3"))
        self.number_1.setItemText(4, _translate("MainWindow", "4"))
        self.number_1.setItemText(5, _translate("MainWindow", "5"))
        self.number_1.setItemText(6, _translate("MainWindow", "6"))
        self.item_1.setItemText(0, _translate("MainWindow", "Все"))
        self.item_1.setItemText(1, _translate("MainWindow", "ДМ"))
        self.item_1.setItemText(2, _translate("MainWindow", "ИнфИС11к"))
        self.item_1.setItemText(3, _translate("MainWindow", "ИнфИС12к"))
        self.item_1.setItemText(4, _translate("MainWindow", "ИнфЮр11К"))
        self.item_1.setItemText(5, _translate("MainWindow", "ИнфЮр21К"))
        self.item_1.setItemText(6, _translate("MainWindow", "ИнфЮр22К"))
        self.item_1.setItemText(7, _translate("MainWindow", "ИнфЮр23К"))
        self.item_1.setItemText(8, _translate("MainWindow", "ИТИС21к"))
        self.item_1.setItemText(9, _translate("MainWindow", "МатИС11к"))
        self.item_1.setItemText(10, _translate("MainWindow", "УПр"))
        self.group_1.setItemText(0, _translate("MainWindow", "Все"))
        self.group_1.setItemText(1, _translate("MainWindow", "ИС21к"))
        self.group_1.setItemText(2, _translate("MainWindow", "ИС11к"))
        self.group_1.setItemText(3, _translate("MainWindow", "ИС12к"))
        self.group_1.setItemText(4, _translate("MainWindow", "ЮР11к"))
        self.group_1.setItemText(5, _translate("MainWindow", "ЮР21к"))
        self.group_1.setItemText(6, _translate("MainWindow", "ЮР22к"))
        self.group_1.setItemText(7, _translate("MainWindow", "ЮР23к"))
        self.classes_1.setItemText(0, _translate("MainWindow", "Все"))
        self.classes_1.setItemText(1, _translate("MainWindow", "0"))
        self.classes_1.setItemText(2, _translate("MainWindow", "Лекция"))
        self.classes_1.setItemText(3, _translate("MainWindow", "Практика"))
        self.classes_1.setItemText(4, _translate("MainWindow", "Урок"))
        self.classes_1.setItemText(5, _translate("MainWindow", "№Н/Д"))
        self.week_1.setItemText(0, _translate("MainWindow", "Все"))
        self.week_1.setItemText(1, _translate("MainWindow", "1"))
        self.week_1.setItemText(2, _translate("MainWindow", "2"))
        self.week_1.setItemText(3, _translate("MainWindow", "3"))
        self.week_1.setItemText(4, _translate("MainWindow", "4"))
        self.week_1.setItemText(5, _translate("MainWindow", "5"))
        self.week_1.setItemText(6, _translate("MainWindow", "6"))
        self.week_1.setItemText(7, _translate("MainWindow", "7"))
        self.week_1.setItemText(8, _translate("MainWindow", "8"))
        self.week_1.setItemText(9, _translate("MainWindow", "9"))
        self.week_1.setItemText(10, _translate("MainWindow", "10"))
        self.week_1.setItemText(11, _translate("MainWindow", "11"))
        self.week_1.setItemText(12, _translate("MainWindow", "12"))
        self.week_1.setItemText(13, _translate("MainWindow", "13"))
        self.week_1.setItemText(14, _translate("MainWindow", "14"))
        self.who_1.setItemText(0, _translate("MainWindow", "Все"))
        self.who_1.setItemText(1, _translate("MainWindow", "Я"))
        self.who_1.setItemText(2, _translate("MainWindow", "Другой"))
        self.openes.setText(_translate("MainWindow", "Открыть"))
        self.exchange.setText(_translate("MainWindow", "Добавить\Изменить"))
        self.repear.setText(_translate("MainWindow", "Удалить"))
        self.FIO.setCurrentText(_translate("MainWindow", "Стерлядева Лилия Венировна"))
        self.FIO.setItemText(0, _translate("MainWindow", "Стерлядева Лилия Венировна"))
        self.but_ktp.setText(_translate("MainWindow", "КТП"))
        self.dnev.setText(_translate("MainWindow", "Дневник"))
        self.but_time.setText(_translate("MainWindow", "Часы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
