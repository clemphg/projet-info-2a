from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue
from vues.maitre_de_jeu.vue_creation_scenario_mj import VueCreationScenarioMJ
from vues.maitre_de_jeu.vue_creation_partie_mj import VueCreationPartieMJ
from vues.maitre_de_jeu.vue_scenarios_mj import VueScenariosMJ
from vues.maitre_de_jeu.vue_parties_mj import VuePartiesMJ
from vues.maitre_de_jeu.vue_notifications_mj import VueNotificationsMJ

from vues.session import Session

class VuePrincipaleMJ(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un sous-menu',
                'choices': [
                    'Créer un scénario',
                    "Créer une partie",
                    'Mes scénarios',
                    'Mes parties',
                    'Mes notifications',
                    'Me déconnecter'
                ]
            }
        ]

    def display_info(self):
        print("Bienvenue",Session().utilisateur.pseudo,"!\n")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Créer un scénario' :
            return VueCreationScenarioMJ()
        elif reponse['choix'] == "Créer une partie":
            return VueCreationPartieMJ()
        elif reponse['choix'] == 'Mes scénarios':
            return VueScenariosMJ()
        elif reponse['choix'] == 'Mes parties':
            return VuePartiesMJ()
        elif reponse['choix'] == 'Mes notifications':
            return VueNotificationsMJ()
        elif reponse['choix'] == 'Me déconnecter':
            Session().utilisateur = None
            from vues.vue_accueil import VueAccueil
            return VueAccueil()
        else:
            pass
