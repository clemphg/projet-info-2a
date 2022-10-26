from pprint import pprint

from PyInquirer import Separator, prompt

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
        reponses = prompt(self.__questions)

        if reponses['type_de_profil']=='Joueur':
            DAO.creer_joueur()
        elif reponses['type_de_profil']=='Maître de jeu':
            pass
        elif reponses['type_de_profil']=='Organisateur':
            pass


        if reponses['type_de_profil']=='Joueur':
            Session.utilisateur = Joueur("nono",12)
            return VuePrincipaleJoueur()
        elif reponses['type_de_profil']=='Maître de jeu':
            Session.utilisateur = MaitreDeJeu("nono",12)
            return VuePrincipaleMJ()
        elif reponses['type_de_profil']=='Organisateur':
            Session.utilisateur = Organisateur("nono",12)
            return VuePrincipaleOrganisateur()