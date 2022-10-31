from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO

import hashlib

from objets_metiers.joueur import Joueur
from objets_metiers.maitre_de_jeu import MaitreDeJeu

class ServiceInscriptionConnexion(metaclass=Singleton):

    def verifier_pseudo_libre(self, pseudo_a_tester):
        return DAO().verifier_pseudo_libre(pseudo_a_tester)

    def verifier_mdp_correct(self, pseudo, mdp_a_tester):
        mdp_hache = hashlib.sha256(pseudo.encode() + mdp_a_tester.encode()).hexdigest()
        return DAO().verifier_mdp(pseudo, mdp_hache)

    def creer_utilisateur(self, pseudo, age, mdp, type_de_profil):
        mdp_hache = hashlib.sha256(pseudo.encode() + mdp.encode()).hexdigest()
        if type_de_profil=='Joueur':
            DAO().creer_joueur(Joueur(pseudo=pseudo,
                                      age=age),
                               mot_de_passe=mdp_hache)
        elif type_de_profil=='Maître de jeu':
            DAO().creer_mj(MaitreDeJeu(pseudo=pseudo,
                                       age=age),
                           mot_de_passe=mdp_hache)
