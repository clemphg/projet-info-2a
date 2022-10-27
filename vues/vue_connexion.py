from pprint import pprint
from PyInquirer import Separator, prompt
import hashlib

from vues.abstract_vue import AbstractVue
from vues.session import Session

from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur

from objets_metiers.joueur import Joueur
from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.organisateur import Organisateur

from dao.dao import DAO

class VueConnexion(AbstractVue):

    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'type_de_profil',
                'message': 'Type de profil',
                'choices': [
                    'Joueur',
                    'Maître de jeu',
                    'Organisateur'
                ]
            },
            {
                'type': 'input',
                'name': 'pseudo',
                'message': 'Pseudo'
            },
            {
                'type': 'password',
                'name': 'mot_de_passe',
                'message': 'Mot de passe'
            }
        ]

    def display_info(self):
        print("Renseignez vos identifiants")

    def make_choice(self):
        nb_essais = 3 # nombre d'essais de couples pseudo+mdp à faire avant d'etre redirigé vers page d'accueil
        vrai_pseudo = False
        vrai_mdp = False
        reponses = None

        while nb_essais>0 and (not(vrai_pseudo) or not(vrai_mdp)):
            nb_essais -= 1 # comptage du nombre d'essais

            reponses = prompt(self.__questions)

            # hachage du mot de passe
            mdp_hache = hashlib.sha256(reponses['pseudo'].encode() + reponses['mot_de_passe'].encode()).hexdigest()

            # instanciation de l'utilisateur selon son type. si pseudo invalide pour le type on a None
            if reponses['type_de_profil']=='Joueur':
                utilisateur = DAO().chercher_par_pseudo_j(reponses['pseudo'])
            elif reponses['type_de_profil']=='Maître de jeu':
                utilisateur = DAO().chercher_par_pseudo_mj(reponses['pseudo'])
            elif reponses['type_de_profil']=='Organisateur':
                utilisateur = DAO().chercher_par_pseudo_organisateur(reponses['pseudo'])

            if utilisateur:
                vrai_pseudo = True
                vrai_mdp = DAO().verifier_mdp(utilisateur.pseudo, mdp_hache)

            if vrai_pseudo and vrai_mdp:
                print("Authentification réussie")
            elif vrai_pseudo and not(vrai_mdp):
                print("Mot de passe incorrect")
            elif not(vrai_pseudo) and vrai_mdp:
                print("Mot de passe incorrect")
            else:
                print("Pseudo et mot de passe incorrects")

        # Si l'authentification a échoué
        if (not(vrai_pseudo) or not(vrai_mdp)):
            from vues.vue_accueil import VueAccueil
            return VueAccueil()

        # si l'authentification est réussie
        Session().utilisateur = utilisateur
        if reponses['type_de_profil']=='Joueur':
            return VuePrincipaleJoueur()
        elif reponses['type_de_profil']=='Maître de jeu':
            return VuePrincipaleMJ()
        elif reponses['type_de_profil']=='Organisateur':
            return VuePrincipaleOrganisateur()