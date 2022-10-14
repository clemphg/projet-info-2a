from abstract_joueur import AbstractJoueur

class Joueur(AbstractJoueur):

    def __init__(self, personnages):
        self.personnages = personnages