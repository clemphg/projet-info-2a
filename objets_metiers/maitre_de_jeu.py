from objets_metiers.abstract_joueur import AbstractJoueur
from objets_metiers.scenario import Scenario

class MaitreDeJeu(AbstractJoueur):

    def __init__(self, pseudo, age, scenarios = []):
        super().__init__(pseudo, age)
        self.__scenarios = scenarios

    @property
    def scenarios(self):
        return self.__scenarios

    def creer_scenario(self, nom, description, niveau_min):
        """Création d'un scénario.

        Un maitre de jeu possède des scénarios. Ils lui servent pour créer une partie sur une table vide.
        Il ne peut pas avoir plus de deux scénarios.

        Parameters
        ----------
        nom : str
            Nom du scénario.
        description : str
            Description du scénario.
        niveau_min : int
            Niveau minimal requis pour les personnages afin de jouer ce scénario.

        Returns
        -------
        bool
            True si le scénario a bien été ajouté, False sinon.
        """
        if len(self.__scenarios)<2:
            self.__scenarios.append(Scenario(nom, description, niveau_min))
            status = True
        else:
            status = False
        return status


    def creer_partie():
        pass
