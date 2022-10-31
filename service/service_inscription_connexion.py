from utils.singleton import Singleton

from vues.session import Session

from dao.dao import DAO

import hashlib

from objets_metiers.joueur import Joueur
from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.organisateur import Organisateur

class ServiceInscriptionConnexion(metaclass=Singleton):

    def verifier_pseudo_libre(self, pseudo_a_tester):
        """Vérifier si le pseudo donné est déjà libre (=non utilisé) ou non

        Parameters
        ----------
        pseudo_a_tester : str
            Pseudo

        Returns
        -------
        bool
            True si le pseudo est libre, False sinon
        """
        return DAO().verifier_pseudo_libre(pseudo_a_tester)

    def verifier_mdp_correct(self, pseudo, mdp_a_tester):
        """Vérifier si le mot de passe donné correspond à celui du pseudo donné

        Parameters
        ----------
        pseudo : str
            Pseudo de l'utilisateur
        mdp_a_tester : str
            Mot de passe à tester

        Returns
        -------
        bool
            True si le mot de passe est correct, False sinon
        """
        mdp_hache = hashlib.sha256(pseudo.encode() + mdp_a_tester.encode()).hexdigest()
        return DAO().verifier_mdp(pseudo, mdp_hache)

    def creer_utilisateur(self, pseudo, age, mdp, type_de_profil):
        """Créer un nouvel utilisateur

        Utilisé lors de l'inscription

        Parameters
        ----------
        pseudo : str
            Pseudo du nouvel utilisateur
        age : int
            Age du nouvel utilisateur
        mdp : str
            Mot de passe du nouvel utilisateur
        type_de_profil : str
            Type du nouvel utilisateur ('Joueur' ou 'Maître de jeu')
        """
        mdp_hache = hashlib.sha256(pseudo.encode() + mdp.encode()).hexdigest()
        if type_de_profil=='Joueur':
            DAO().creer_joueur(Joueur(pseudo=pseudo,
                                      age=age),
                               mot_de_passe=mdp_hache)
        elif type_de_profil=='Maître de jeu':
            DAO().creer_mj(MaitreDeJeu(pseudo=pseudo,
                                       age=age),
                           mot_de_passe=mdp_hache)

    def instanciation_utilisateur(self, pseudo, type_de_profil):
        """Instancier un utilisateur qui deviendra l'utilisateur courant de la session

        Utilité lors de la connexion

        Parameters
        ----------
        pseudo : str
            Pseudo du nouvel utilisateur
        type_de_profil : str
            Type de l'utilisateur

        Returns
        -------
        Joueur or MaitreDeJeu or Organisateur of None
            Utilisateur correspondant (None si l'utilisateur n'existe pas)
        """
        if type_de_profil=='Joueur':
            utilisateur = DAO().chercher_par_pseudo_j(pseudo)
        elif type_de_profil=='Maître de jeu':
            utilisateur = DAO().chercher_par_pseudo_mj(pseudo)
        elif type_de_profil=='Organisateur':
            utilisateur = DAO().chercher_par_pseudo_org(pseudo)
        return utilisateur
