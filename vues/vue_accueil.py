from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue
from vues.session import Session

from vues.vue_connexion import VueConnexion
from vues.vue_inscription import VueInscription

class VueAccueil(AbstractVue):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Bienvenue ! Veuillez vous connecter si vous avez un compte, et le cas échéant vous inscrire.',
                'choices': [
                    'Inscription',
                    'Connexion',
                    'Quitter'
                ]
            }
        ]

    def display_info(self):
        with open('graphiques/nom_banniere.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())


    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Inscription':
            from vues.vue_inscription import VueInscription
            return VueInscription()
        elif reponse['choix'] == 'Connexion':
            from vues.vue_connexion import VueConnexion
            return VueConnexion()
        else:
            pass
