

class Personnage():
    ''' Un personnage est créé par un joueur et est choisi par ce même joueur lorsqu'il participe à une partie de jeu de rôle, il en a au maximum 3

        Attributes
        ----------
        id: int
           Id du personnage
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
        pseudo_j : str
            Pseudo du joueur possédant le personnage

        Examples
        ----------
        Exemple d'utilisation
        >>> c = Personnage()
        >>> c.id.classe()

        '''

    def __init__(self, id=None, nom=None, age=None, race=None, niveau=None, classe=None, pseudo_j=None) -> None:
        ''' Constructeur'''

        self.__id = id
        self.__nom = nom
        self.__age = age
        self.__race = race
        self.__niveau = niveau
        self.__classe = classe
        self.__pseudo_j = pseudo_j

    @property
    def id(self):
        ''' Retourne l'id du personnage'''
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nom(self):
        ''' Retourne le nom du personnage'''
        return self.__nom

    @property
    def age(self):
        ''' Retourne l'âge du personnage'''
        return self.__age

    @property
    def race(self):
        ''' Retourne la race du personnage'''
        return self.__race

    @property
    def niveau(self):
        '''Retourne le niveau du personnage'''
        return self.__niveau

    @property
    def classe(self):
        ''' Retourne la classe du personnage'''
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
        from dao.dao import DAO
        DAO().maj_classe(self, nvlle_classe)

    @property
    def pseudo_j(self):
        '''Retourne le pseudo du joueur possédant le personnage'''
        return self.__pseudo_j
