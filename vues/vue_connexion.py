from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue
from vues.session import Session


class VueConnexion(AbstractVue):

    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'type_de_profil',
                'message': 'Type de profil',
                'choices': [
                    'Joueur',
                    'Maître de jeu'
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


        pprint("Inscription réussie !")
        from vues.vue_accueil import VueAccueil
        return VueAccueil()