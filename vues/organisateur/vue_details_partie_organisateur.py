from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session

from service.service_organisateur import ServiceOrganisateur

class VueDetailsPartieOrganisateur(AbstractVue):
    def __init__(self, partie) -> None:
        self.__partie = partie
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Retourner à la liste des parties',
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        print(" --- Détails d'une partie --- \n")

        print("> Partie ", self.__partie.id,
              "\n  Nom du scénario : ", self.__partie.scenario.nom,
              "\n  Description de la partie : ", self.__partie.scenario.description,
              "\n  Personnages : ")

        for perso in self.__partie.liste_persos:
            print("\n     Nom ", perso.nom,
                  "\n     Age : ", perso.id,
                  "\n     Rage : ", perso.race,
                  "\n     Niveau : ", perso.niveau,"\n")

    def make_choice(self):

        reponse = prompt(self.__questions)
        if reponse['choix']=='Retourner à la liste des parties':
            from vues.organisateur.vue_parties_organisateur import VuePartiesOrganisateur
            return VuePartiesOrganisateur()
        elif reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()