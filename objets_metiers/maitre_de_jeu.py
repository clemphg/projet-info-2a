from objets_metiers.abstract_joueur import AbstractJoueur
from objets_metiers.scenario import Scenario
from objets_metiers.partie import Partie


class MaitreDeJeu(AbstractJoueur):
    ''' Un maître de jeu est un abstract joueur défini par son pseudo, son âge et la liste de scénario(s) qu'il crée
    Attributes
    ----------
    pseudo : str
        Le pseudo du maître de jeu
    age : int
        L'âge du maître de jeu
    scénarios : liste
        Liste de scénarios que crée le maître de jeu, il peut en avoir maximum 2, au départ elle est vide
    '''

    def __init__(self, pseudo, age, scenarios=[]):
        ''' Constructeur'''
        super().__init__(pseudo, age)
        self.__scenarios = scenarios

    def __str__(self):
        res = "Pseudo   : {pseudo}\nAge      : {age}".format(
            pseudo=self.pseudo, age=self.age)
        if len(self.__scenarios) > 0:
            res = res+"\nScenario :"
            for scenario in self.__scenarios:
                res = res+"\n"+scenario.__str__()
        return res

    @property
    def scenarios(self):
        return self.__scenarios

    def creer_scenario(self, id, nom, description, niveau_min):
        """Création d'un scénario.

        Un maitre de jeu possède des scénarios. Ils lui servent pour créer une partie sur une table vide.
        Il ne peut pas avoir plus de deux scénarios.

        Parameters
        ----------
        id : id
            Id du scénario
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
        if len(self.__scenarios) < 2:
            scenar = Scenario(id=id,
                              nom=nom,
                              description=description,
                              niveau_min=niveau_min,
                              pseudo_mj=self.pseudo)
            self.__scenarios.append(scenar)
            status = True
        else:
            status = False
        return status
