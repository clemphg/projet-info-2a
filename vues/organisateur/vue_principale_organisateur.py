from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session
from vues.organisateur.vue_joueurs_organisateur import VueJoueursOrganisateur
from vues.organisateur.vue_mjs_organisateur import VueMJsOrganisateur
from vues.organisateur.vue_parties_organisateur import VuePartiesOrganisateur
from vues.organisateur.vue_notifications_organisateur import VueNotificationsOrganisateur

class VuePrincipaleOrganisateur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un sous-menu',
                'choices': [
                    'Liste des joueurs',
                    'Liste des maîtres de jeu',
                    'Liste des parties',
                    'Mes notifications',
                    'Me déconnecter'
                ]
            }
        ]

    def display_info(self):
        print("Bienvenue",Session().utilisateur.pseudo,"!\n")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Liste des joueurs':
            return VueJoueursOrganisateur()
        elif reponse['choix'] == 'Liste des maîtres de jeu':
            return VueMJsOrganisateur()
        elif reponse['choix'] == 'Liste des parties':
            return VuePartiesOrganisateur()
        elif reponse['choix'] == 'Mes notifications':
            return VueNotificationsOrganisateur()
        elif reponse['choix'] == 'Me déconnecter':
            Session().utilisateur = None
            from vues.vue_accueil import VueAccueil
            return VueAccueil()
        else :
            pass