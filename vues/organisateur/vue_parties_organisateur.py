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
                'name': 'choix_action',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Voir une partie en détails',
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'choix_retour',
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
                  "\n  Nom du scénario : ", partie.scenario.nom,
                  "\n  Description de la partie : ", partie.scenario.description,
                  "\n  Nombre de joueurs inscrits : ", len(partie.liste_persos))

    def make_choice(self):

        parties = ServiceOrganisateur().liste_parties()

        if len(parties)>0:
            reponse = prompt(self.__questions[0])
            if reponse['choix_action']=='Voir une partie en détails':
                reponse = prompt(
                    {
                        'type': 'list',
                        'name': 'choix',
                        'message': 'Sélectionner une partie',
                        'choices':
                            [str(partie.id) for partie in parties]
                    }
                )
                id_partie = int(reponse['choix'])
                partie = [partie for partie in parties if partie.id == id_partie][0]
                # ouvrir la vue détail de partie
                from vues.organisateur.vue_details_partie_organisateur import VueDetailsPartieOrganisateur
                return VueDetailsPartieOrganisateur(partie)
            elif reponse['choix_action']=='Retourner au menu principal':
                from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
                return VuePrincipaleOrganisateur()
        else :
            print("\nIl n'y a aucune partie prévue pour l'instant.\n")
            reponse = prompt(self.__questions[1])
            if reponse['choix_retour']=='Retourner au menu principal':
                from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
                return VuePrincipaleOrganisateur()