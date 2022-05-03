# -*- coding: utf-8 -*-
# rpcontacts/model.py

# Création de la class du model de vu du widget


from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        self.model = self._createModel()


    def deleteContact(self, row):
        """Suppression d'un contact depuis le bouton supprimé"""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()


    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Nom", "Métier", "Téléphone", "Email")
        for columnIndex, header, in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addContact(self, data):
        """Add a contact to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()