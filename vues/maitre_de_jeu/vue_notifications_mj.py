from pprint import pprint

from PyInquirer import Separator, prompt


from vues.abstract_vue import AbstractVue

class VueNotificationsMJ(AbstractVue):
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

        # utiliser la DAO pour trouver les messages
        
        reponse = prompt(self.__questions)