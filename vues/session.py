from utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        """
        Variables que l'on stocke en session.

        """
        self.utilisateur = None
