# -*- coding: utf-8 -*-

# Le dossier contiendra le code pour générer l'interface graphique des fenêtres et des boîtes de dialogue etc... on va voir comment on fait

# Import de certaine fonctionnalité de la librairie PyQT5
from email import message
from tkinter import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtGui import QStandardItemModel, QStandardItem



#import de notre module
from .model import ContactsModel

# Fenêtre principale de l'application
class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        # Instanciation de l'objet contacs model
        self.contactsModel = ContactsModel()
        self.setWindowTitle("Gestionnaire de contacte v0.0.1")
        self.resize(1000, 400)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.setupUI()

# Configurer l'interface graphique de la fenêtre principale
    def setupUI(self):

        # Pour fournir la vue sous forme de tableau qui affiche la liste des contacts
        self.table = QTableView()
        # Sélection de vue de tableau
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # affichage du module d'affichage des contacts et de sa structure
        self.table.setModel(self.contactsModel.model)
        
        # Pour créer les boutons Ajouter , Supprimer et Effacer tout
        self.addButton = QPushButton("Ajouter")
        self.addButton.clicked.connect(self.openAddDialog)
        self.editButton = QPushButton("Editer")
        self.deleteButton = QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Tout supprimer")
        self.clearAllButton.clicked.connect(self.clearContacts)
        self.search = QLineEdit()
        self.search.setStyleSheet('font-size: 20px; height: 40px')

        # Créent et définissent une mise en page cohérente pour tous les widgets de l'interface graphique
        layout = QVBoxLayout()
        layout.addWidget(self.search)
        layout.addWidget(self.addButton)
        layout.addWidget(self.editButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    # Méthod qui affiche la box de confirmation et lance la method de suppression global
    def clearContacts(self):
        """ Supprimer tout """
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Voulez-vous réinisialiser la totalité de vos contacts ?",
            QMessageBox.Ok | QMessageBox.Cancel
        )
        
        if messageBox == QMessageBox.Ok:
            self.contactsModel.clearContacts()

    #
    def deleteContact(self):
        """Supprime un contact selectionné."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Supprimer le contact selectionné ?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.deleteContact(row)

    # Function qui affiche la boite de dialogue lorsque le click est effectué sur le button
    def openAddDialog(self):
        """Open the Add Contact dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()

# Class pour une boite de dialogue
class AddDialog(QDialog):
    """ajout de la boite ajout contact"""
    def __init__(self, parent=None):
        """Inisialisation"""
        super().__init__(parent=parent)
        self.setWindowTitle("Ajouter un contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()
    
    def setupUI(self):
        """Configuration de l'interface de la boite de dialogue"""
        # On créer des objets pour chaque champs du formulaire 
        self.prenomField = QLineEdit()
        self.prenomField.setObjectName("Prénom")
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Nom")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Métier")
        self.phoneField = QLineEdit()
        self.phoneField.setObjectName("Téléphone")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")
        # On construit la structure de la boite de dialogue
        layout = QFormLayout()
        layout.addRow("Prénom:", self.prenomField)
        layout.addRow("Nom:", self.nameField)
        layout.addRow("Métier:", self.jobField)
        layout.addRow("Téléphone:", self.phoneField)
        layout.addRow("Email:", self.emailField)
        self.layout.addLayout(layout)
        # On ajoute les boutons et ont les connectes
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        """Accepte les données fournies par le texte"""
        self.data = []
        for field in (self.prenomField, self.nameField, self.jobField, self.phoneField, self.emailField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Reinisialisation des donnée
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()
