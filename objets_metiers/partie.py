

from pickle import TRUE
from dao.dao import DAO


class Partie():


    def __init__(self, id=None, creneau=None, scenario=None, liste_persos=None):

        """ Création d'une partie (par un maître de jeu)

        Parameters
        ----------
        creneau : int
            Créneau sur lequel se tient la partie
        scenario : Scenario
            Scénario utilisé pour la partie
        """

        self.__id = id
        self.__creneau = creneau
        self.__scenario = scenario
        self.__liste_persos = liste_persos

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valeur):
        self.__id = valeur

    @property
    def creneau(self):
        return self.__creneau

    @property
    def scenario(self):
        return self.__scenario

    @property
    def liste_persos(self):
        return self.__liste_persos

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
            DAO.ajouter_joueur_partie(self,personnage)
            if DAO.ajouter_joueur_partie(self,personnage)==TRUE:
                status=True
        elif len(self.__liste_persos)==0:
            self.__liste_persos = [personnage]
            DAO.ajouter_joueur_partie(self,personnage)
            if DAO.ajouter_joueur_partie(self,personnage)==TRUE:
                status=True
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
