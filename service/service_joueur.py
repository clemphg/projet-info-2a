from utils.singleton import Singleton

from dao.dao import DAO

from vues.session import Session

from service.service_messages import ServiceMessages

class ServiceJoueur(metaclass=Singleton):

    def messages(self, pseudo):
        " Retourne la liste des messages reçus par l'utilisateur à l'aide de son pseudo"
        return DAO().chercher_messages_par_pseudo(pseudo)

    def creation_personnage(self, perso):
        " Génère l'id du personnage et notifie à la base de données les différentes informations du personnage en question"
        id = DAO().creer_perso(perso)
        perso.id = id
        ServiceMessages().message_creation_personnage(perso.pseudo_j, perso)
        return id

    def changer_classe_perso(self, perso, nvlle_classe):
        "Change la classe du personnage et notifie le changement à la base de données"
        res = DAO().maj_classe(perso, nvlle_classe)
        ServiceMessages().message_maj_classe(perso.pseudo_j, perso, nvlle_classe)
        perso.classe = nvlle_classe
        return res

    def details_partie(self, id_partie):
        "Retourne les détails d'une partie"
        return DAO().chercher_partie_par_id(id_partie)

    def liste_parties(self, pseudo_joueur):
        "Retourne une liste de dictionnaire décrivant l'inscription aux différentes parties"
        return DAO().liste_inscriptions_joueur(pseudo_joueur)

    def desinscription_personnage(self, id_perso, id_partie, pseudo_j):
        "Retourne un True si la désinscription a bien été réalisée, sinon False. Notifie les changements à la base de données"
        res = DAO().desinscription_personnage(id_perso,id_partie)
        ServiceMessages().message_desinscription_partie(pseudo_j, id_partie, id_perso)
        return res

    def liste_creneaux_dispos(self, joueur):
        "Retourne la liste des créneaux disponibles pour un joueur"
        creneaux_dispos = DAO().liste_creneaux_dispos_joueur(joueur)
        return creneaux_dispos

    def parties_dispos_creneau(self, id_creneau):
        "Retourne la liste des parties disponibles pour un créneau"
        parties = DAO().chercher_parties_par_creneau(id_creneau)
        # on ne conserve que les parties qui ont moins de quatre joueurs
        parties_ok = [partie for partie in parties if len(partie.liste_persos)<4]
        return parties_ok

    def persos_niv_sup_a(self, joueur, niveau):
        "Retourne une liste de personnages dont le niveau est supérieur ou égal au niveau minimum requis, retourne none s'il n'y a aucun personnage qui respecte la condition"
        l_res = []
        for perso in joueur.personnages:
            if perso.niveau>=niveau:
                l_res.append(perso)
        if len(l_res)>0:
            return l_res
        else:
            return None

    def inscription_perso(self, id_perso, id_partie, pseudo_j):
        "Retourne True si le personnage a bien été créé, false sinon. Notifie à la base de données, le changement réalisé"
        res = DAO().inscription_personnage(id_perso, id_partie)
        ServiceMessages().message_inscription_partie(pseudo_j, id_partie, id_perso)
        return res

