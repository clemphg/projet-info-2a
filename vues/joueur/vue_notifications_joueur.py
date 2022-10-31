from pprint import pprint

from PyInquirer import Separator, prompt


from vues.session import Session
from vues.abstract_vue import AbstractVue

from service.service_messages import ServiceMessages


class VueNotificationsJoueur(AbstractVue):
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
        messages = ServiceMessages().chercher_messages(Session().utilisateur.pseudo)
        if messages:
            for message in messages:
                print("Message du ",message['date'],"\n>>>",message['message'],"\n")
        else :
            print("Pas de notifications\n")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix']=='Retourner au menu principal':
            from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
            return VuePrincipaleJoueur()