from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO

from objets_metiers.organisateur import Organisateur

from service.service_messages import ServiceMessages

class ServiceOrganisateur(metaclass=Singleton):

    def liste_joueurs(self):
        " Retourne la liste des joueurs"
        return DAO().liste_joueurs()

    def bannir_joueur(self, joueur):
        " Retourne True si tous les personnages du joueur et de sa liste de parties ont été supprimés, et True si le joueur a été banni"
        status = True
        # supprimer les inscriptions du joueur
        inscriptions = DAO().liste_inscriptions_joueur(joueur.pseudo)
        if inscriptions:
            for ins in inscriptions:
                res = DAO().desinscription_personnage(ins['id_perso'], ins['id_partie'])
                status = status and res
        # supprimer ses personnages
        if len(joueur.personnages)>0:
            for perso in joueur.personnages:
                res = DAO().supprimer_personnage(perso)
                status = status and res
        # le supprimer
        res = DAO().bannir_joueur(joueur.pseudo)
        return status and res

    def supprimer_personnage(self, perso, joueur):
        "Retourne True si le personnage a été supprimé, et True si le personnage a été désinscrit, et notifie à la base de données les informations du personnage supprimé"  
        status = True
        # supprimer ses inscriptions
        inscriptions = DAO().liste_inscriptions_joueur(joueur.pseudo)
        if len(inscriptions)>0:
            for id_partie in [ins['id_partie'] for ins in inscriptions if ins['id_perso']==perso.id]:
                res = DAO().desinscription_personnage(perso.id, id_partie)
                status = status and res
        # le supprimer
        res = DAO().supprimer_personnage(perso)
        ServiceMessages().message_suppression_perso_org(joueur.pseudo, Session().utilisateur.pseudo, perso)
        return res and status

    def liste_mjs(self):
        " Retourne la liste des MJs"
        return DAO().liste_mjs()

    def bannir_mj(self, mj):
        " Retourne True si les parties et les scénarios du MJ ont été supprimées, et True si le MJ a été banni"
        status = True
        # supprimer les inscriptions du mj (donc les parties)
        inscriptions = DAO().liste_inscriptions_mj(mj.pseudo)
        if inscriptions:
            for id_partie in [ins['id_partie'] for ins in inscriptions]:
                partie = DAO().chercher_partie_par_id(id_partie)
                res = DAO().supprimer_partie(partie)
                status = status and res
        # supprimer ses scenarios
        if len(mj.scenarios)>0:
            for scenario in mj.scenarios:
                res = DAO().supprimer_scenario(scenario)
                status = status and res
        # le supprimer
        res = DAO().bannir_mj(mj.pseudo)
        return status and res


    def supprimer_scenario(self, scenario, mj):
        "retourne True si la partie dans laquelle le scénario a été utilisé a été supprimée, et True si le scénario a été supprimé, et notifie à la base de données les informations du scénario supprimé"
        status = True
        # supprimer les parties dans lesquelles le scénario est utilisé
        inscriptions = DAO().liste_inscriptions_mj(mj.pseudo)
        if inscriptions:
            for id_partie in list(set([ins['id_partie'] for ins in inscriptions if ins['id_scenario']==scenario.id])):
                partie = DAO().chercher_partie_par_id(id_partie)
                res = DAO().supprimer_partie(partie)
                status = status and res
        # supprimer le scénario
        res = DAO().supprimer_scenario(scenario)
        ServiceMessages().message_suppression_scenario_org(mj.pseudo, Session().utilisateur.pseudo, scenario)
        return status and res

    def liste_parties(self):
        "retourne la liste des parties pour chaque créneau"
        creneaux = DAO().liste_creneaux()
        parties = []
        for c in creneaux:
            parties = parties + DAO().chercher_parties_par_creneau(c)
        return parties

    def supprimer_partie(self, partie):
        "retourne la suppression de la partie"
        res = DAO().supprimer_partie(partie)
        return res

    def desinscrire_personnage(self, id_perso, id_partie):
        "retourne la désinscription du personnage, à l'aide de son identifiant et de l'identifiant de la partie"
        res = DAO().desinscription_personnage(id_perso, id_partie)
        return res

    def inscrire_personnage(self, perso, partie):
        "retourne l'inscription du personnage, à l'aide du personnage et de la partie"
        res = DAO().inscription_personnage(perso.id, partie.id)
        return res

    def personnages_possibles(self, partie):
        "retourne la liste des personnages possibles pour une partie"
        res = DAO().liste_perso_possibles(partie)
        return res
