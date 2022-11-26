from PyInquirer import Separator, prompt

from vues.session import Session
from vues.abstract_vue import AbstractVue

from service.service_maitre_de_jeu import ServiceMaitreDeJeu
class VueDetailsPartieMJ(AbstractVue):
    def __init__(self, id_partie) -> None:
        self.__id_partie = id_partie
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    "Supprimer la partie",
                    "Retour à la liste des parties",
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        print("--- Vue détaillée d'une partie ---\n")
        partie = ServiceMaitreDeJeu().details_partie(self.__id_partie)
        print(partie,"\n")

    def make_choice(self):
        partie = ServiceMaitreDeJeu().details_partie(self.__id_partie)
        reponse = prompt(self.__questions)
        if reponse['choix']=="Supprimer la partie":
            ServiceMaitreDeJeu().supprimer_partie(partie)
            print("\nPartie supprimée.\n")
            from vues.maitre_de_jeu.vue_parties_mj import VuePartiesMJ
            return VuePartiesMJ()
        elif reponse['choix']=='Retour à la liste des parties':
            from vues.maitre_de_jeu.vue_parties_mj import VuePartiesMJ
            return VuePartiesMJ()
        elif reponse['choix']=='Retourner au menu principal':
            from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
            return VuePrincipaleMJ()
        else:
            pass