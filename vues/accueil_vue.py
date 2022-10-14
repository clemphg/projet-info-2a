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
                'message': 'Bienvenue sur cette application',
                'choices': [
                    'Next'
                    , 'Inscription'
                    , 'Connexion'

                ]
            }
        ]

    def display_info(self):
        print("Hello there!")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Next':
            pass
        elif reponse['choix'] == 'Inscription':
            from vues.vue_inscription import VueInscription
            return VueInscription()
        elif reponse['choix'] == 'Connexion':
            from vues.vue_connexion import VueConnexion
            return VueConnexion()
