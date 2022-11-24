class Organisateur():
    ''' Organisteur du jeu, il a beaucoup de pouvoir car il peut supprimer des personnages, bannir des joueur etc
    Attributes
       ----------
       pseudo : str
           Pseudo de l'organisateur, sert d'identifiant de connexion
           '''

    def __init__(self, pseudo):
        ''' Constructeur'''
        self.__pseudo = pseudo

    @property
    def pseudo(self):
        return self.__pseudo
