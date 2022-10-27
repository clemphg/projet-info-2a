from pprint import pprint

from PyInquirer import Separator, prompt


from vues.abstract_vue import AbstractVue

from vues.session import Session

class VueScenariosMJ(AbstractVue):
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
        if Session().utilisateur.scenarios:
            for scenar in Session().utilisateur.scenarios:
                print("Nom :",scenar.nom,"\nNiveau minimum :",scenar.niveau_min,"\nDescription :",scenar.description,"\n")
        else:
            print("Vous n'avez pas encore créé de scénario.")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Retourner au menu principal':
            from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
            return VuePrincipaleMJ()