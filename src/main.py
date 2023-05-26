import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit


from ui_main import Ui_MainWindow
from new_transaction import Ui_Dialog
from connection import Data


class Tracker(QMainWindow):
    def __init__(self):
        super(Tracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        # временный коммент
        #  self.ui.btn_exchange.clicked.connect(self.open_new_transaction_window)
        #  self.ui.btn_edit_transaction.clicked.connect(self.open_new_transaction_window)
        #  self.ui.btn_delete_transaction.clicked.connect(self.delete_current_transaction)
        #
        #  self.ui.current_balance.setText(self.conn.total_balance())
        #  self.ui.income_balance.setText(self.conn.total_income())
        #  self.ui.outcome_balance.setText(self.conn.total_outcome())
        #  self.ui.total_groceries.setText(self.conn.total_groceries())
        #  self.ui.total_auto.setText(self.conn.total_auto())
        #  self.ui.total_entertainment.setText(self.conn.total_entertainment())
        #  self.ui.total_other.setText(self.conn.total_other())

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "New transaction":
            self.ui_window.btn_new_transaction.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.btn_new_transaction.clicked.connect(self.edit_current_transaction)

    def add_new_transaction(self):
        month_1 = self.ui_window.dateEdit.text()
        number_1 = self.ui_window.cb_choose_category.currentText()
        item_1 = self.ui_window.le_description.text()
        group_1 = self.ui_window.le_balance.text()
        classes_1 = self.ui_window.cb_status.currentText()

        self.conn.add_new_transaction_query(month_1, number_1, item_1, group_1, classes_1, week_1, who_1)
        self.view_data()
        self.new_window.close()

    def edit_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        date = self.ui_window.dateEdit.text()
        category = self.ui_window.cb_choose_category.currentText()
        description = self.ui_window.le_description.text()
        balance = self.ui_window.le_balance.text()
        status = self.ui_window.cb_status.currentText()

        self.conn.update_transaction_query(month_1, number_1, item_1, group_1, classes_1, week_1, who_1, id)
        self.view_data()
        self.new_window.close()

    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.conn.delete_transaction_query(id)
        self.view_data()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Создаем класс главного окна приложения
    traker = Tracker()
    traker.show()
    # перехватываем выход из приложения
    sys.exit(app.exec_())
