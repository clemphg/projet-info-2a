
class Organisateur():

    def __init__(self, pseudo):
        """Création d'un maitre de jeu

        Parameters
        ----------
        pseudo : str
            Pseudo de l'organisateur. Identifiant de connexion.
        """
        self.__pseudo = pseudo

    def supprimer_joueur(self, joueur, partie):
        pass

    def reaffecter_joueur(self, joueur, partie):
        pass

    def supprimer_mj(self, mj, partie):
        pass

    def bannir_joueur(self, joueur):
        pass

    def bannir_mj(self, mj):
        pass

    def supprimer_partie(self, partie):
        """Redondant avec supprimer mj non ?"""
        pass
