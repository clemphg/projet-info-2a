from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue
from vues.joueur.vue_creation_personnage_joueur import VueCreationPersonnageJoueur
from vues.joueur.vue_inscription_partie_joueur import VueInscriptionPartieJoueur
from vues.joueur.vue_personnages_joueur import VuePersonnagesJoueur
from vues.joueur.vue_parties_joueur import VuePartiesJoueur
from vues.joueur.vue_notifications_joueur import VueNotificationsJoueur

from vues.session import Session

class VuePrincipaleJoueur(AbstractVue):
    "Création d'une vue avec la défintion d'une variable questions qui va stocker les intéractions du joueur. Ici, le joueur pourra créer un personnage, s'inscrire à une partie, consulter ses parties, ses personnages ainsi que ses notifications et enfin se déconnecter, s'il sélectionne le sous-menu correspondant. "
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un sous-menu',
                'choices': [
                    'Créer un personnage',
                    "M'inscrire à une partie",
                    'Mes personnages',
                    'Mes parties',
                    'Mes notifications',
                    'Me déconnecter'
                ]
            }
        ]

    def display_info(self):
        "Affiche Bienvenue ainsi que le pseudo de l'utilisateur"
        print("Bienvenue",Session().utilisateur.pseudo,"!\n")

    def make_choice(self):
        "Retourne la vue du joueur correspondant à ce qu'il aura choisi de sélectionner comme sous-menu "
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Créer un personnage' :
            return VueCreationPersonnageJoueur()
        elif reponse['choix'] == "M'inscrire à une partie":
            return VueInscriptionPartieJoueur()
        elif reponse['choix'] == 'Mes personnages':
            return VuePersonnagesJoueur()
        elif reponse['choix'] == 'Mes parties':
            return VuePartiesJoueur()
        elif reponse['choix'] == 'Mes notifications':
            return VueNotificationsJoueur()
        elif reponse['choix'] == 'Me déconnecter':
            Session().utilisateur = None
            from vues.vue_accueil import VueAccueil
            return VueAccueil()
        else:
            pass

