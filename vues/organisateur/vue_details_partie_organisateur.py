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
                'message': 'Sélectionner une action',
                'choices': [
                    'Inscrire un personnage à cette partie',
                    'Désinscrire un personnage de cette partie',
                    'Retourner à la liste des parties',
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner une action',
                'choices': [
                    'Inscrire un personnage à cette partie',
                    'Retourner à la liste des parties',
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner une action',
                'choices': [
                    'Désinscrire un personnage de cette partie',
                    'Retourner à la liste des parties',
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        print(" --- Détails d'une partie --- \n")

        print(self.__partie,"\n")

    def make_choice(self):

        nb_persos = len(self.__partie.liste_persos)

        if nb_persos == 0:
            reponse = prompt(self.__questions[1])
        elif 0 < nb_persos < 4:
            reponse = prompt(self.__questions[0])
        elif nb_persos == 4:
            reponse = prompt(self.__questions[2])

        if reponse['choix'] == 'Inscrire un personnage à cette partie':
            choix_perso = prompt(
                {
                    'type': 'list',
                    'name': 'choix',
                    'message': 'Sélectionner un personnage selon son nom',
                    'choices':
                        [str(p.id) for p in self.__partie.liste_persos]
                }
            )
        elif reponse['choix'] == 'Désinscrire un personnage de cette partie':
            choix_perso = prompt(
                {
                    'type': 'list',
                    'name': 'choix',
                    'message': 'Sélectionner un personnage selon son nom',
                    'choices':
                        [str(p.id) for p in self.__partie.liste_persos]
                }
            )
        elif reponse['choix']=='Retourner à la liste des parties':
            from vues.organisateur.vue_parties_organisateur import VuePartiesOrganisateur
            return VuePartiesOrganisateur()
        elif reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()