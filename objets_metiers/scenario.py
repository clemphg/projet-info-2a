""" Classe Scenario

Un scénario appartient à un maître de jeu. Une fois créé, il ne peut pas être modifié.

"""
class Scenario():

    def __init__(self, id=None, nom=None, description=None, niveau_min=None):
        """Créer un scénario (par un maître de jeu).

        Parameters
        ----------
        id : str
            Id du scénario
        nom : str
            Nom (description courte) du scénario
        description : str
            Description longue du scénario
        niveau_min : int
            Niveau minimal requis pour jouer au scénario
        """
        self.__id = id
        self.__nom = nom
        self.__description = description
        self.__niveau_min = niveau_min

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def nom(self):
        return self.__nom

    @property
    def description(self):
        return self.__description

    @property
    def niveau_min(self):
        return self.__niveau_min