from utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        """
        Variables que l'on stocke en session.

        utilisateur : utilisateur de la session (Joueur, MaitreDeJeu ou Organisateur)

        """
        self.utilisateur = None
