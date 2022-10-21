

class Partie():

    def __init__(self, date, scenario):
        """ Création d'une partie (par un maître de jeu)

        Parameters
        ----------
        date : int
            Date (creneau) à laquelle se tient la partie
        scenario : Scenario
            Scénario utilisé pour la partie
        """
        self.__date = date
        self.__scenario = scenario
        self.__liste_persos = None

    def ajouter_perso(self, perso):
        """Ajouter un personnage à la partie.

        Permet d'ajouter un personnage à une partie. Le personnage ne peut être ajouter que
        s'il y a moins de 5 personnages déjà incrits à la partie.

        Parameters
        ----------
        perso : Personnage
            Personnage à ajouter à la partie
        """
        if self.__liste_persos and len(self.__liste_persos)<5 :
            self.__liste_persos.append(perso)
        elif len(self.__liste_persos)<5:
            self.__liste_persos = [perso]

    def supprimer_perso(self, perso):
        """Supprimer un personnage d'une partie.

        Permet d'ajouter un personnage à une partie. Le personnage ne peut être ajouter que
        s'il y a moins de 5 personnages déjà incrits à la partie.

        Parameters
        ----------
        perso : Personnage
            Personnage à ajouter à la partie
        """
        if self.__liste_persos and len(self.__liste_persos)<5 :
            self.__liste_persos.append(perso)
        elif len(self.__liste_persos)<5:
            self.__liste_persos = [perso]