from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session
from dao.dao import DAO
class VueMJsOrganisateur(AbstractVue):
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
        print("-- Liste des maîtres de jeu --\n")
        mjs = DAO().liste_mjs()
        for mj in mjs:
            print("> Pseudo          :",mj.pseudo,"\n  Age             :",mj.age,"\n  Nb de scénarios :",len(mj.scenarios),"\n")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()