from pprint import pprint

from PyInquirer import Separator, prompt

from vues.session import Session
from vues.abstract_vue import AbstractVue

from dao.dao import DAO

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
        print(DAO().liste_inscriptions_joueur(Session().utilisateur.pseudo))

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix']=='Retourner au menu principal':
            from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
            return VuePrincipaleJoueur()