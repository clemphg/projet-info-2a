from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session
from service.service_organisateur import ServiceOrganisateur


class VueMJsOrganisateur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Voir un maître de jeu en détails',
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'choix_mj',
                'message': 'Sélectionner un maître de jeu',
                'choices': [mj.pseudo for mj in ServiceOrganisateur().liste_mjs()]
            }
        ]

    def display_info(self):
        print("-- Liste des maîtres de jeu --\n")
        mjs = ServiceOrganisateur().liste_mjs()
        for mj in mjs:
            print("> Pseudo          :",mj.pseudo,
                  "\n  Age             :",mj.age,
                  "\n  Nb de scénarios :",len(mj.scenarios),"\n")

    def make_choice(self):
        reponse = prompt(self.__questions[0])
        if reponse['choix'] == 'Voir un maître de jeu en détails':
            choix_mj = prompt(self.__questions[1])
            pseudo = choix_mj['choix_mj']
            mjs = ServiceOrganisateur().liste_mjs()
            mj = [mj for mj in mjs if mj.pseudo == pseudo][0]
            from vues.organisateur.vue_details_mj_organisateur import VueDetailsMJOrganisateur
            return VueDetailsMJOrganisateur(mj)
        elif reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()