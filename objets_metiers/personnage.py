"""Classe Personnage

Un personnage est créé par un Joueur. Celui-ci en a au maximum trois.

"""

class Personnage():

    def __init__(self, nom, age, race, niveau, classe ) -> None:
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
        self.__nom = nom
        self.__age = age
        self.__race = race
        self.__niveau = niveau
        self.__classe = classe

    def modifier_classe(self, nvlle_classe: str) -> None:
        """Modifier la classe du personnage

        Parameters
        ----------
        nvlle_classe : str
            Nouvelle classe à donner au personnage
        """
        self.__classe = nvlle_classe
