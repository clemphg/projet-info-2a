from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session

from dao.dao import DAO

class VueJoueursOrganisateur(AbstractVue):
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
        print("-- Liste des joueurs --\n")
        joueurs = DAO().liste_joueurs()
        for joueur in joueurs:
            print("> Pseudo            :",joueur.pseudo,"\n  Age               :",joueur.age,"\n  Nb de personnages :",len(joueur.personnages),"\n")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()