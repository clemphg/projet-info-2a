from PyInquirer import Separator, prompt


from vues.abstract_vue import AbstractVue
from vues.session import Session

from service.service_maitre_de_jeu import ServiceMaitreDeJeu

class VueNotificationsMJ(AbstractVue):
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
        messages = ServiceMaitreDeJeu().messages(Session().utilisateur.pseudo)
        if messages:
            for message in messages:
                print("Message du ",message['date'],"\n>>> ",message['message'],"\n")
        else:
            print("Pas de notifications\n")

    def make_choice(self):

        # utiliser la DAO pour trouver les messages

        reponse = prompt(self.__questions)
        if reponse['choix']=='Retourner au menu principal':
            from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
            return VuePrincipaleMJ()