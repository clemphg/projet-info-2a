from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue
from vues.session import Session

from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur

from objets_metiers.joueur import Joueur

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

        # ajouter l'utilisateur créé dans la base

        if reponses['type_de_profil']=='Joueur':
            Session.utilisateur = Joueur("nono",12)
            return VuePrincipaleJoueur()