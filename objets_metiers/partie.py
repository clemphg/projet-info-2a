

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

    def ajouter_perso(self, personnage):
        """Ajouter un personnage à la partie.

        Permet d'ajouter un personnage à une partie. Le personnage ne peut être ajouter que
        s'il y a moins de 5 personnages déjà incrits à la partie.

        Parameters
        ----------
        perso : Personnage
            Personnage à ajouter à la partie

        Returns
        -------
        bool :
            True si le personnage a été ajouté à la partie, False sinon
        """
        status = False
        if self.__liste_persos and len(self.__liste_persos)<5 :
            self.__liste_persos.append(personnage)
            status = True
        elif len(self.__liste_persos)==0:
            self.__liste_persos = [personnage]
            status = True

        # ajouter en base via DAO
        return status

    def supprimer_perso(self, personnage):
        """Supprimer un personnage d'une partie.

        Permet de supprimer un personnage d'une partie.

        Parameters
        ----------
        perso : Personnage
            Personnage à supprimer de la partie

        Returns
        -------
            True si le personnage a bien été supprimé de la partie, False sinon
        """
        status = False
        for perso in self.__liste_persos:
            if perso.id == personnage.id:
                self.__liste_persos.remove(perso)
                status = True
        return status
