
import dotenv
import os

from utils.singleton import Singleton
from dao.dao import DAO

from service.service_messages import ServiceMessages


class ServiceMaitreDeJeu(metaclass=Singleton):

    def messages(self, pseudo):
        """Retourne une liste de message à l'aide du pseudo du personnage"""
        return DAO().chercher_messages_par_pseudo(pseudo)

    def creer_scenario(self, scenario):
        """Retourne l'id généré du nouveau scénario lors de sa création et notifie le changement à la base de données"""
        id = DAO().creer_scenario(scenario)
        scenario.id = id
        ServiceMessages().message_creation_scenario(scenario.pseudo_mj, scenario)
        return id

    def creer_partie(self, partie):
        """Retourne l'id généré de la nouvelle partie lors de sa création et notifie le changement à la base de données"""
        id = DAO().creer_partie(partie)
        ServiceMessages().message_creation_partie(partie.scenario.pseudo_mj, partie)
        return id

    def details_partie(self, id_partie):
        """Retourne le détail d'une partie"""
        return DAO().chercher_partie_par_id(id_partie)

    def liste_parties(self, pseudo_mj):
        """Retourne une liste de dictionnaire décrivant l'inscription aux parties"""
        return DAO().liste_inscriptions_mj(pseudo_mj)

    def liste_creneaux_dispos(self, mj):
        """Retourne la liste des créneaux disponibles pour un maître de jeu"""
        creneaux_dispos = DAO().liste_creneaux_dispos_mj(mj)
        return creneaux_dispos

    def verifier_nvlle_partie_possible(self, creneau):
        """Vérifie s'il est possible de créer une nouvelle partie pour le créneau voulu.
        Si c'est le cas, True sera retournée sinon False"""
        dotenv.load_dotenv(override=True)
        nb_parties_par_creneau = int(os.environ["NB_PARTIES_MAX_PAR_CRENEAU"])
        parties = DAO().chercher_parties_par_creneau(creneau)
        if len(parties) < nb_parties_par_creneau:
            return True
        else:
            return False

    def supprimer_partie(self, partie):
        """Permet de vérifier si la partie a été supprimée ou non et notifie le changement à
        la base de données. Si la partie a été supprimée, il sera retournée True sinon False"""
        res = DAO().supprimer_partie(partie)
        ServiceMessages().message_suppression_partie(partie.scenario.pseudo_mj, partie)
        return res
