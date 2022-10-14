from objets_metiers.abstract_joueur import AbstractJoueur
from objets_metiers.abstract_joueur import AbstractJoueur

class MaitreDeJeu(AbstractJoueur):

    def __init__(self, pseudo, age):
        super().__init__(pseudo, age)
        self.scenarios = None

    def creer_scenario():
        pass

    def creer_partie():
        pass
