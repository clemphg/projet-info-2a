from pprint import pprint

from PyInquirer import Separator, prompt

from vues.session import Session
from vues.abstract_vue import AbstractVue

from dao.dao import DAO

class VuePartiesJoueur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Voir une partie en détail'
                    'Retourner au menu principal'
                ]
            },
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
        print("--- Liste des inscriptions de mes personnages ---\n")
        # à remplacer par un appel à un service
        inscriptions = DAO().liste_inscriptions_joueur(Session().utilisateur.pseudo)

        if inscriptions :
            for ins in inscriptions:
                print(
                    ">  Créneau              :",ins['id_creneau'],"\n",
                    "  ID de partie         :",ins['id_partie'],"\n",
                    "  Maître de jeu        :",ins['pseudo_mj'],"\n",
                    "  Scénario             :",ins['nom_scenario'],"\n",
                    "  Niveau minimum       :",ins['niv_min_scenario'],"\n",
                    "  Nom du personnage    :",ins['nom_perso'],"\n",
                    "  Niveau du personnage :",ins['niv_perso'],"\n",
                    )
        else:
            print(
                "Vous n'avez aucun personnage inscrit à une partie.\n"
                "Vous pouvez en inscrire un via l'onglet 'M'inscrire à une partie' du menu principal.\n")

    def make_choice(self):
        inscriptions = DAO().liste_inscriptions_joueur(Session().utilisateur.pseudo)
        if inscriptions:
            reponse = prompt(self.__questions[0])
            if reponse['choix']=='Voir une partie en détail':
                from vues.joueur.vue_details_partie_joueur import VueDetailsPartieJoueur
                return VueDetailsPartieJoueur()
            elif reponse['choix']=='Retourner au menu principal':
                from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                return VuePrincipaleJoueur()
            else:
                pass
        else :
            reponse = prompt(self.__questions[1])
            if reponse['choix']=='Retourner au menu principal':
                from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                return VuePrincipaleJoueur()
            else:
                pass