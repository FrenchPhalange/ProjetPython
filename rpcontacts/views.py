# -*- coding: utf-8 -*-

# Le dossier contiendra le code pour générer l'interface graphique des fenêtres et des boîtes de dialogue etc... on va voir comment on fait

from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

# Fenêtre principale de l'application
class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gestionnaire de contacte v0.0.1")
        self.resize(700, 400)
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

        # Pour créer les boutons Ajouter , Supprimer et Effacer tout
        self.addButton = QPushButton("Ajouter")
        self.editButton = QPushButton("Editer")
        self.deleteButton = QPushButton("Supprimer")
        self.clearAllButton = QPushButton("Poutine")

        # Créent et définissent une mise en page cohérente pour tous les widgets de l'interface graphique
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.editButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

