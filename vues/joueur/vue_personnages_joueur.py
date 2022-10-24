from pprint import pprint

from PyInquirer import Separator, prompt
from objets_metiers.personnage import Personnage


from vues.abstract_vue import AbstractVue
from vues.session import Session

class VuePersonnagesJoueur(AbstractVue):
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
        if Session.utilisateur.personnages:
            for perso in Session.utilisateur.personnages:
                print("personnage")
        else:
            print("Vous n'avez pas encore créé de personnage.")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Retourner au menu principal':
            from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
            return VuePrincipaleJoueur()