from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO

from objets_metiers.maitre_de_jeu import MaitreDeJeu


nb_parties_par_creneau = 10

class ServiceMaitreDeJeu(metaclass=Singleton):

    def messages(self, pseudo):
        return DAO().chercher_messages_par_pseudo(pseudo)

    def details_partie(self, id_partie):
        return DAO().chercher_partie_par_id(id_partie)

    def liste_parties(self, pseudo_mj):
        return DAO().liste_inscriptions_mj(pseudo_mj)

    def verifier_nvlle_partie_possible(self, creneau):
        pass

