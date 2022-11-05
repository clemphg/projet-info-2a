from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session

from service.service_organisateur import ServiceOrganisateur
class VuePartiesOrganisateur(AbstractVue):
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
        print(" --- Liste des parties --- \n")
        parties = ServiceOrganisateur().liste_parties()

        for partie in parties :
            print("> Partie ", partie.id,
                  "  Nom du scénario : ", partie.scenario.nom,
                  "  Description de la partie : ", partie.scenario.description,
                  "  Nombre de joueurs inscrits : ", len(partie.liste_persos))

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()