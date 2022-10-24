from pprint import pprint

from PyInquirer import Separator, prompt


from vues.abstract_vue import AbstractVue

class VuePartiesJoueur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        pass

    def make_choice(self):
        reponse = prompt(self.__questions)