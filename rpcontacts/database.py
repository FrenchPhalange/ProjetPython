# -*- coding: utf-8 -*-
# rpcontacts/database.py

# Connexion de l'appli à la Db, si c'est bon = True sinon False et explicayion de pourquoi echec/error

from PyQt5.QtWidgets import QMessageBox
# exécuter et manipuler des instructions SQL d'après StackOverFlow
from PyQt5.QtSql import QSqlDatabase, QSqlQuery




def _createContactsTable():
    # Créez la table des contacts dans la base de données
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            nom VARCHAR(40) NOT NULL,
            métier VARCHAR(50),
            téléphone VARCHAR(15) NOT NULL,
            email VARCHAR(40) NOT NULL
        )
        """
    )


def createConnection(databaseName):
    # Créez et ouvre une connexion à la base de données
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Gestionnaire de contacte v0.0.1",
            f"Erreur de base de données: {connection.lastError().text()}",
        )
        return False

    _createContactsTable()
    # Revient True si la tentative de connexion réussit
    return True




