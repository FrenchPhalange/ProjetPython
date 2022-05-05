# -*- coding: utf-8 -*-
# rpcontacts/model.py

# Création de la class du model de vu du widget


from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    # Fonction supprimant toute les données de la base de donnée 
    def clearContacts(self):
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

    # Fonction supprmant la données selectionnée (si aucune selectionné ce sera la première)
    def deleteContact(self, row):
        """Suppression d'un contact depuis le bouton supprimé"""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    # Création de la method static pour créer un modèle et l'instancié
    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("Prénom", "Nom", "Métier", "Téléphone", "Email")
        for columnIndex, header, in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addContact(self, data):
        """Ajoute un contact à la base de données."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column), field)
        self.model.submitAll()
        self.model.select()