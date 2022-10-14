
from curses import ACS_GEQUAL


class Personnage():

    def __init__(self, nom, age, race, niveau, classe ) :
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
