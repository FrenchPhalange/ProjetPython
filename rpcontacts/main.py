# -*- coding: utf-8 -*-

# Bah le main quoi, là ou l'appli est héberger la db , run et les fonctions principales etc...

# import sys = accéder à exit() et donc, ça se ferme proprement
import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window

# Fonction principale de l'appli
def main():
    # Créer l'application
    app = QApplication(sys.argv)

    # Il faut se connecter à la DB avant de vouloir lancer ou créer 
    if not createConnection("contacts.sqlite"):
        # Si problème, il indiquera une erreur
        sys.exit(1)

    # Créer la fenêtre principale (C'est le fichier views.py)
    win = Window()
    win.show()

    # Exécute la boucle
    sys.exit(app.exec())