from pprint import pprint

from PyInquirer import Separator, prompt
from objets_metiers.personnage import Personnage


from vues.abstract_vue import AbstractVue
from vues.session import Session

class VuePersonnagesJoueur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix_menu',
                'message': 'Sélectionner un choix',
                'choices': [
                    "Modifier la classe de l'un de mes personnages",
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'choix_perso',
                'message': 'Sélectionner un personnage',
                'choices':
                    [perso.nom for perso in Session().utilisateur.personnages]
            }
        ]

    def display_info(self):
        if Session().utilisateur.personnages:
            for perso in Session().utilisateur.personnages:
                print("Nom :",perso.nom,"\nAge :",perso.age,"\nNiveau :",perso.niveau,"\nRace :",perso.race,"\nClasse :",perso.classe,"\n")
        else:
            print("Vous n'avez pas encore créé de personnage.")

    def make_choice(self):

        # si le joueur a des personnages il peut modifier leur classe
        if Session().utilisateur.personnages:
            reponse = prompt(self.__questions[0])
            if reponse['choix_menu'] == "Modifier la classe de l'un de mes personnages":
                pass

        from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
        return VuePrincipaleJoueur()