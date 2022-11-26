
from objets_metiers.personnage import Personnage
from objets_metiers.scenario import Scenario


class Partie():
    ''' Une partie est jouée par 4 personnages et met en scène un des scénarios des maîtres du jeu, elle est donc créee par le maître du jeu

        Attributes
        ----------
        id : int
            Id de la partie
        creneau : int
            Le créneau durant lequel se déroulera la partie
        scenario : Scenario
            Le scénario utilisé pour la partie
        liste_persos: list[Personnage]
            La liste des personnages qui participent à la partie

       Examples
       ----------
       Exemple d'utilisation
       >>> c = Partie()
       >>> c.ajouter_perso()
       >>> c.supprimer_perso
    '''

    def __init__(self, id: int = None, creneau: int = None, scenario: Scenario = None, liste_persos: list[Personnage] = []):
        ''' Constructeur'''
        self.__id = id
        self.__creneau = creneau
        self.__scenario = scenario
        self.__liste_persos = liste_persos

    def __str__(self):
        res = f"ID          : {self.__id}\nCreneau     : {self.__creneau}\nScenario    : "
        res = res+"\n"+self.__scenario.__str__()
        if len(self.__liste_persos) > 0:
            res = res+"\nPersonnages :"
            for perso in self.__liste_persos:
                res = res+"\n"+perso.__str__()
        return res

    @property
    def id(self):
        ''' Retourne l'id de la partie'''
        return self.__id

    @id.setter
    def id(self, valeur):
        self.__id = valeur

    @property
    def creneau(self):
        ''' Retourne le créneau de la partie '''
        return self.__creneau

    @property
    def scenario(self):
        ''' Retourne le scénario choisi pour la partie'''
        return self.__scenario

    @property
    def liste_persos(self):
        ''' Retourne la liste des personnages participant à la partie'''
        return self.__liste_persos
