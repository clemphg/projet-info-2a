from utils.singleton import Singleton

from dao.dao import DAO

from vues.session import Session

from service.service_messages import ServiceMessages

from client.client_personnage import ClientPersonnage

class ServiceJoueur(metaclass=Singleton):

    def messages(self, pseudo):
        """Affichage des messages du joueur

        Retourne la liste des messages reçus par l'utilisateur à l'aide de son pseudo

        Parameters
        ----------
        pseudo : str
            Le pseudonyme d'un utilisateur
        Returns
        -------
        list[ str ]
        """
        return DAO().chercher_messages_par_pseudo(pseudo)

    def creation_personnage(self, perso):
        """Création d'un personnage

        Génère l'id du personnage et notifie à la base de données les différentes informations du personnage en question.

        Parameters
        ----------
        perso : Personnage

        Returns
        -------
        int
            Retourne l'id du personnage nouvellement créé.
        """
        id = DAO().creer_perso(perso)
        perso.id = id
        ServiceMessages().message_creation_personnage(perso.pseudo_j, perso)
        return id

    def changer_classe_perso(self, perso, nvlle_classe):
        """Changer la classe d'un personage

        Change la classe du personnage et notifie le changement à la base de données.

        Parameters
        ----------
        perso : Personnage

        Returns
        -------
        bool
            Retourne True si la classe du personnage a bien été modifié.
        """
        res = DAO().maj_classe(perso, nvlle_classe)
        ServiceMessages().message_maj_classe(perso.pseudo_j, perso, nvlle_classe)
        perso.classe = nvlle_classe
        return res

    def details_partie(self, id_partie):
        """ Accès aux détails d'une partie

        Parameters
        ----------
        id_partie : int

        Returns
        -------
        Partie
            Retourne les détails d'une partie.
        """
        return DAO().chercher_partie_par_id(id_partie)

    def liste_parties(self, pseudo_joueur):
        """ Accès à la liste des parties du joueur

        Parameters
        ----------
        pseudo_joueur : str
            Le pseudonyme du joueur

        Returns
        -------
        list[ dict ]
            Retourne une liste de dictionnaire décrivant l'inscription aux différentes parties.
        """
        return DAO().liste_inscriptions_joueur(pseudo_joueur)

    def desinscription_personnage(self, id_perso, id_partie, pseudo_j):
        """ Désinscription d'un personnage à une partie

        Parameters
        ----------
        pseudo_j : str
                  Le pseudonyme du joueur
        id_perso : int
                   L'id du personnage que l'on souhaite désinscrire
        id_partie: int
                   L'id de la partie pour laquelle on souhaite désisncrire notre personnage

        Returns
        -------
        bool

            Retourne un True si la désinscription a bien été réalisée, sinon False. Notifie les changements à la base de données.
        """

        res = DAO().desinscription_personnage(id_perso,id_partie)
        ServiceMessages().message_desinscription_partie(pseudo_j, id_partie, id_perso)
        return res

    def liste_creneaux_dispos(self, joueur):
        """ Accès à la liste des crénaux disponibles pour un joueur

        Parameters
        ----------
        joueur : Joueur

        Returns
        -------
        list[ int ]

            Retourne la liste des créneaux disponibles pour un joueur.
        """
        creneaux_dispos = DAO().liste_creneaux_dispos_joueur(joueur)
        return creneaux_dispos

    def parties_dispos_creneau(self, id_creneau):
        """ Accès à la liste des parties pour lesquels il y a moins de 4 joueurs, à l'aide d'un créneau

        Parameters
        ----------
        id_creneau : int
                   L'id du créneau

        Returns
        -------
        list[ Partie ]

            Retourne la liste des parties disponibles pour un créneau.
        """
        parties = DAO().chercher_parties_par_creneau(id_creneau)
        # on ne conserve que les parties qui ont moins de quatre joueurs
        parties_ok = [partie for partie in parties if len(partie.liste_persos)<4]
        return parties_ok

    def persos_niv_sup_a(self, joueur, niveau):
        """ Accès à la liste des personnages du joueur dont le niveau est supérieur ou égal à un niveau minimum requis
        Parameters
        ----------
        niveau : int
        joueur: Joueur

        Returns
        -------
        list[Personnage]

            Retourne une liste de personnages dont le niveau est supérieur ou égal au niveau minimum requis, retourne none s'il  n'y a aucun personnage qui respecte la condition.
        """
        l_res = []
        for perso in joueur.personnages:
            if perso.niveau>=niveau:
                l_res.append(perso)
        if len(l_res)>0:
            return l_res
        else:
            return None

    def inscription_perso(self, id_perso, id_partie, pseudo_j):
        """ Inscription d'un personnage d'un joueur à une partie
        Parameters
        ----------
        id_perso : int
                  L'id du personnage que le joueur souhaite inscrire à une partie
        id_partie : int
                  L'id de la partie pour laquelle le joueur souhaite inscrire son personnage
        pseudo_j: str
                Le pseudonyme du Joueur

        Returns
        -------
        bool
            Retourne True si le personnage a bien été créé, false sinon. Notifie à la base de données, le changement réalisé."""
        res = DAO().inscription_personnage(id_perso, id_partie)
        ServiceMessages().message_inscription_partie(pseudo_j, id_partie, id_perso)
        return res

    def races_possibles(self):
        """ Liste des races possibles

        Appelle l'API via un client pour déterminer la liste des races ossibles d'un personnage.

        Returns
        -------
        list
            La liste des races possibles (liste de chaines de caractères)
        """
        return ClientPersonnage().races_possibles()

    def classes_possibles(self):
        """ Liste des classes possibles

        Appelle l'API via un client pour déterminer la liste des classes possibles d'un personnage.

        Returns
        -------
        list
            La liste des classes possibles (liste de chaines de caractères)
        """
        return ClientPersonnage().classes_possibles()
