from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session
from vues.organisateur.vue_notifications_organisateur import VueNotificationsOrganisateur
class VuePrincipaleOrganisateur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un sous-menu',
                'choices': [
                    'Mes notifications',
                    'Me déconnecter'
                ]
            }
        ]

    def display_info(self):
        print("Bienvenue",Session().utilisateur.pseudo,"!")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Mes notifications':
            return VueNotificationsOrganisateur()
        elif reponse['choix'] == 'Me déconnecter':
            Session().utilisateur = None
            from vues.vue_accueil import VueAccueil
            return VueAccueil()