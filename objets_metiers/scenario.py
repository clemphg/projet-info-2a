""" Classe Scenario

Un scénario appartient à un maître de jeu. Une fois créé, il ne peut pas être modifié.

"""
class Scenario():

    def __init__(self, id=None, nom=None, description=None, niveau_min=None, pseudo_mj=None):
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
        pseudo_mj : str
            Pseudo du maître de jeu possédant le scénario
        """
        self.__id = id
        self.__nom = nom
        self.__description = description
        self.__niveau_min = niveau_min
        self.__pseudo_mj = pseudo_mj

    def __str__(self):
        '''Chaine de caractères décrivant le scénario'''
        res = """ID                   : {id}\n
                 Nom                  : {nom}\n
                 Description          : {des}\n
                 Niveau minimal       : {niv}\n
                 Pseudo maitre de jeu : {pseudo}""".format(id=self.__id,
                                                           nom=self.__nom,
                                                           des=self.__description,
                                                           niv=self.__niveau_min,
                                                           pseudo=self.__pseudo_mj)
        return res

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

    @property
    def pseudo_mj(self):
        return self.__pseudo_mj