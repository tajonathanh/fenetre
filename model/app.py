# -*- coding: utf-8 -*-

#Header
"""
- Que fait
- Jonathanh TA
- 11/03/2024
- a faire 
"""
# Importation des bibliothèques nécessaires
import tkinter as tk


# Classe pour définir la fenêtre

class app(tk.Tk):
    def __init__(self):

        #Initialisation de la fênetre de jeu
        super().__init__()
        self.title("NOM DU JEU")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(background='Yellow')

        # Création et positionnement du bouton Quitter
        quit_button = tk.Button(self, text="Quitter", command=self.quit, bg="White")  
        quit_button.pack(side='left', padx=10, pady=10)

    def quit(self):
        """Fonction pour fermer l'application."""
        self.destroy()
