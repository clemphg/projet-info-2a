from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session

class VuePrincipaleOrganisateur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un sous-menu',
                'choices': [
                    'Me déconnecter'
                ]
            }
        ]

    def display_info(self):
        print("Bienvenue",Session().utilisateur.pseudo,"!")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Me déconnecter':
            Session.utilisateur = None
            from vues.vue_accueil import VueAccueil
            return VueAccueil()