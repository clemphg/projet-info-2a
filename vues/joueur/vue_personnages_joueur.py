from pprint import pprint

from PyInquirer import Separator, prompt
from objets_metiers.personnage import Personnage

from utils.singleton import Singleton

from vues.abstract_vue import AbstractVue
from vues.session import Session

from client.client_personnage import ClientPersonnage

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
                'name': 'choix_nvlle_classe',
                'message': 'Sélectionner une nouvelle classe',
                'choices':
                    ClientPersonnage().classes_possibles()
            },
            {
                'type': 'list',
                'name': 'choix_menu',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        print("--- Mes personnages ---\n")
        if Session().utilisateur.personnages:
            for perso in Session().utilisateur.personnages:
                print(perso,"\n")
        else:
            print("Vous n'avez pas encore créé de personnage.\n")

    def make_choice(self):

        # si le joueur a des personnages il peut modifier leur classe
        if Session().utilisateur.personnages:
            reponse = prompt(self.__questions[0])

            while reponse['choix_menu'] == "Modifier la classe de l'un de mes personnages":
                # question choix perso définie ici pour que les caractéristiques soient à jour ds les questions si jamais on change plusieurs classes
                rep_perso = prompt(
                    {
                'type': 'list',
                'name': 'choix_perso',
                'message': 'Sélectionner un personnage',
                'choices':
                    ["ID : "+str(perso.id)+" (nom : "+perso.nom+", classe : "+perso.classe+")" for perso in Session().utilisateur.personnages]
                })
                rep_classe = prompt(self.__questions[1])
                id = rep_perso['choix_perso'].split(' ')[2]
                for perso in Session().utilisateur.personnages:
                    if perso.id == int(id):
                        perso.classe = rep_classe['choix_nvlle_classe']

                # on affiche la nouvelle liste des personnages
                for perso in Session().utilisateur.personnages:
                    print(perso,"\n")

                # on repose la question : modifier classe ou retour au menu principal
                reponse = prompt(self.__questions[0])
            from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
            return VuePrincipaleJoueur()

        else:
            reponse = prompt(self.__questions[2])
            if reponse['choix_menu']=='Retourner au menu principal':
                    from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                    return VuePrincipaleJoueur()
