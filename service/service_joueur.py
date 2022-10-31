from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO

from objets_metiers.joueur import Joueur

class ServiceJoueur(metaclass=Singleton):

    def messages(self, pseudo):
        return DAO().chercher_messages_par_pseudo(pseudo)

    def details_partie(self, id_partie):
        return DAO().chercher_partie_par_id(id_partie)

    def liste_parties(self, joueur):
        return DAO().liste_inscriptions_joueur(joueur)

    def desinscription_joueur(self, joueur, id_partie):
        res = DAO().desinscription_joueur(joueur,id_partie)
        return res

    def liste_creneaux_dispos(self, joueur):
        creneaux_dispos = DAO().liste_creneaux_dispos_joueur(joueur)
        return creneaux_dispos

    def parties_dispos_creneau(self, id_creneau):
        parties = DAO().chercher_parties_par_creneau(id_creneau)
        # on ne conserve que les parties qui ont moins de quatre joueurs
        parties_ok = [partie for partie in parties if len(partie.liste_persos)<4]
        return parties_ok

    def persos_niv_sup_a(self, joueur, niveau):
        l_res = []
        for perso in joueur.personnages:
            if perso.niveau>=niveau:
                l_res.append(perso)
        if len(l_res)>0:
            return l_res
        else:
            return None

    def inscription_perso(self, id_perso, id_partie):
        DAO().inscription_personnage(id_perso, id_partie)

