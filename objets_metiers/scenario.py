""" Classe Scenario

Un scénario appartient à un maître de jeu. Une fois créé, il ne peut pas être modifié.

"""
class Scenario():

    def __init__(self, id, nom, description, niveau_min):
        """Créer un scénario (par un maître de jeu).

        Parameters
        ----------
        nom : str
            Nom (description courte) du scénario
        description : str
            Description longue du scénario
        niveau_min : int
            Niveau minimal requis pour jouer au scénario
        """
        self.id = id
        self.nom = nom
        self.description = description
        self.niveau_min = niveau_min