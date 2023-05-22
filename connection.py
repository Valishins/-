from PyQt5 import QtWidgets, QtSql
import sqlite3

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expense (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "number VARCHAR(20), predmet VARCHAR(20), grup REAL, vid VARCHAR(20), nedel VARCHAR(20), who VARCHAR(20))")
        return True

    def execute_query(self, sql_query, values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if values is not None:
            for value in values:
                query.addBindValue(value)

        query.exec()

    def add_new_transaction_query(self, month_1, number_1, item_1, group_1, classes_1, week_1, who_1):
        sql_query = "INSERT INTO expense (Date, number, predmet, grup, vid, nedel, who) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.execute_query(sql_query, [month_1, number_1, item_1, group_1, classes_1,  week_1, who_1])

    def update_transaction_query(self, month_1, number_1, item_1, group_1, classes_1, week_1, who_1, id):
        sql_query = "UPDATE expense SET Date=?, number=?, predmet=?, grup=?, vid=?, nedel=?, who=? WHERE ID=?"
        self.execute_query(sql_query, [month_1, number_1, item_1, group_1, classes_1, week_1, who_1, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expense WHERE ID=?"
        self.execute_query(sql_query, [id])

