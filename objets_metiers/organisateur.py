
class Organisateur():

    def __init__(self, pseudo):
        """Création d'un maitre de jeu

        Parameters
        ----------
        pseudo : str
            Pseudo de l'organisateur. Identifiant de connexion.
        """
        self.__pseudo = pseudo

    @property
    def pseudo(self):
        return self.__pseudo

    def supprimer_personnage(self, personnage, partie):
        partie.supprimer(personnage)

    def reaffecter_personnage(self, personnage, prec_partie, nvlle_partie):
        # si on peut l'ajouter à la nouvelle partie,
        pass

    def bannir_joueur(self, joueur):
        # effacer le joueur, ses personnages et l'enlever de toutes les parties
        pass

    def bannir_mj(self, mj):
        # effacer le mj, ses scénarios et toutes les parties qu'il menaient
        # => supprimer les joueurs de ces parties
        pass

    def supprimer_partie(self, partie):
        # supprimer le maitre de jeu et tous les joueurs de la partie
        pass
