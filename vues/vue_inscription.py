from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue
from vues.session import Session


class VueInscription(AbstractVue):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Retour à l accueil',
                'choices': [
                    'Next'
                    , 'Accueil'

                ]
            }
        ]

    def display_info(self):
        print("S'inscrire")

    def make_choice(self):
        pass