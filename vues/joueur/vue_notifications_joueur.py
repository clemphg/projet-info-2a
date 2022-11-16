from pprint import pprint

from PyInquirer import Separator, prompt


from vues.session import Session
from vues.abstract_vue import AbstractVue

from service.service_messages import ServiceMessages


class VueNotificationsJoueur(AbstractVue):
    def __init__(self) -> None:
        " Création d'une vue Notifications avec la définition d'une variable questions qui va pouvoir indiquer les actions du joueur lorsqu'il est sur la vue en question. En l'occurrence ici, le joueur peut décider de rester sur la page Notifications ou retourner au menu principal en sélectionnant 'Retourner au menu principal'"
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
        "Permet d'afficher sur la console les différentes notifications du joueur avec la date de celles-ci. S'il n'a aucun message, il sera affiché sur la console le message suivant : 'Pas de notifications'"
        messages = ServiceMessages().chercher_messages(Session().utilisateur.pseudo)
        if messages:
            for message in messages:
                print("Message du ",message['date'],"\n>>>",message['message'],"\n")
        else :
            print("Pas de notifications\n")

    def make_choice(self):
        "Permet au joueur de retourner sur son menu principal s'il le souhaite/en fait le choix"
        reponse = prompt(self.__questions)
        if reponse['choix']=='Retourner au menu principal':
            from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
            return VuePrincipaleJoueur()
