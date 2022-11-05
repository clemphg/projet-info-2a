from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO

from objets_metiers.organisateur import Organisateur

class ServiceOrganisateur(metaclass=Singleton):

    def liste_joueurs(self):
        return DAO().liste_joueurs()

    def bannir_joueur(self, joueur):
        status = True
        # supprimer les inscriptions du joueur
        inscriptions = DAO().liste_inscriptions_joueur(joueur.pseudo)
        if inscriptions:
            for id_partie in [ins['id_partie'] for ins in inscriptions]:
                res = DAO().desinscription_joueur(joueur, id_partie)
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
        status = True
        # supprimer ses inscriptions
        inscriptions = DAO().liste_inscriptions_joueur(joueur.pseudo)
        if len(inscriptions)>0:
            for id_partie in [ins['id_partie'] for ins in inscriptions if ins['id_perso']==perso.id]:
                res = DAO().desinscription_joueur(joueur, id_partie)
                status = status and res
        # le supprimer
        res = DAO().supprimer_personnage(perso)
        return res and status

    def liste_mjs(self):
        return DAO().liste_mjs()

    def bannir_mj(self, mj):
        status = True
        # supprimer les inscriptions du mj (donc les parties)
        inscriptions = DAO().liste_inscriptions_mj(mj.pseudo)
        if inscriptions:
            for id_partie in [ins['id_partie'] for ins in inscriptions]:
                res = DAO().supprimer_partie(id_partie)
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
        status = True
        # supprimer les parties dans lesquelles le scénario est utilisé
        inscriptions = DAO().liste_inscriptions_mj(mj.pseudo)
        if inscriptions:
            for id_partie in [ins['id_scenario'] for ins in inscriptions]:
                res = DAO().supprimer_partie(id_partie)
                status = status and res
        # supprimer le scénario
        res = DAO().supprimer_scenario(scenario)
        return status and res

    def liste_parties(self):
        creneaux = DAO().liste_creneaux()
        parties = []
        for c in creneaux:
            parties = parties + DAO().chercher_parties_par_creneau(c)
        return parties

    def supprimer_partie(self, partie):
        res = DAO().supprimer_partie(partie)
        return res

    def desinscrire_personnage(self, perso, partie):
        pass

    def inscrire_personnage(self, perso, partie):
        pass