"""Classe Personnage

Un personnage est créé par un Joueur. Celui-ci en a au maximum trois.

"""

class Personnage():

    def __init__(self, id=None, nom=None, age=None, race=None, niveau=None, classe=None) -> None:
        """Créer un personnage

        Parameters
        ----------
        nom : str
            Nom du personnage
        age : int
            Age du personnage
        race : str
            Race du personnage
        niveau : str
            Niveau du personnage
        classe : str
            Classe du personnage
        """
        self.__id = id
        self.__nom = nom
        self.__age = age
        self.__race = race
        self.__niveau = niveau
        self.__classe = classe

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nom(self):
        return self.__nom

    @property
    def age(self):
        return self.__age

    @property
    def race(self):
        return self.__race

    @property
    def niveau(self):
        return self.__niveau

    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, nvlle_classe: str):
        """Modifier la classe du personnage

        Parameters
        ----------
        nvlle_classe : str
            Nouvelle classe à donner au personnage
        """
        self.__classe = nvlle_classe
