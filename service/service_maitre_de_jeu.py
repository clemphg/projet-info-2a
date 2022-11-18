from pickle import TRUE
from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO

from objets_metiers.maitre_de_jeu import MaitreDeJeu

from service.service_messages import ServiceMessages

nb_parties_par_creneau = 10

class ServiceMaitreDeJeu(metaclass=Singleton):

    def messages(self, pseudo):
        return DAO().chercher_messages_par_pseudo(pseudo)

    def creer_scenario(self, scenario):
        id = DAO().creer_scenario(scenario)
        scenario.id = id
        ServiceMessages().message_creation_scenario(scenario.pseudo_mj, scenario)
        return id

    def creer_partie(self, partie):
        id = DAO().creer_partie(partie)
        return id

    def details_partie(self, id_partie):
        return DAO().chercher_partie_par_id(id_partie)

    def liste_parties(self, pseudo_mj):
        return DAO().liste_inscriptions_mj(pseudo_mj)

    def liste_creneaux_dispos(self, mj):
        creneaux_dispos = DAO().liste_creneaux_dispos_mj(mj)
        return creneaux_dispos

    def verifier_nvlle_partie_possible(self, creneau):
        parties = DAO().chercher_parties_par_creneau(creneau)
        if len(parties)<nb_parties_par_creneau:
            return True
        else:
            return False

    def supprimer_partie(self, partie):
        res = DAO().supprimer_partie(partie)
        return res



