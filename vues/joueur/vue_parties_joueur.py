from PyInquirer import Separator, prompt

from vues.session import Session
from vues.abstract_vue import AbstractVue

from service.service_joueur import ServiceJoueur
class VuePartiesJoueur(AbstractVue):
    def __init__(self) -> None:
        " Création de la vue avec la définition d'une variable questions qui va stocker les intéractions du joueur. Il peut voir une partie en détail s'il sélectionne 'Voir une partie en détail' ou bien retourner au menu principal en sélectionnant 'Retourner sur le menu principal' "
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Voir une partie en détail',
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
        " Permet d'afficher la liste des personnages inscrits à la liste des parties auxquelles le joueur est inscrit. Il sera affiché pour chaque personnage: le créneau de la partie, l'id de la partie, le maître du jeu, le scénario, le niveau minimum requis du scénario, le nom du personnage et son niveau. Si la liste des inscriptions est vide, le message suivant s'affiche: 'Vous n'avez aucun personnage inscrit à une partie. Vous pouvez en inscrire un via l'onglet 'M'inscrire à une partie du menu principal'"
        print("--- Liste des inscriptions de mes personnages ---\n")
        # à remplacer par un appel à un service
        inscriptions = ServiceJoueur().liste_parties(Session().utilisateur.pseudo)

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
        " Permet de voir une partie si le joueur le désire. Il pourra sélectionner ensuite la partie qu'il souhaiterait voir en détail et aura les informations de celle-ci affichées sur la console. Ensuite, il peut retourner au menu principal s'il le souhaite. Dans le cas où sa liste d'inscriptions aux parties est vide, il lui est directement proposé de retourner au menu principal."
        inscriptions = ServiceJoueur().liste_parties(Session().utilisateur.pseudo)
        if inscriptions:
            reponse = prompt(self.__questions[0])
            if reponse['choix']=='Voir une partie en détail':
                q_partie = prompt(
                    {
                        'type': 'list',
                        'name': 'choix',
                        'message': 'Sélectionner une partie (selon son ID)',
                        'choices': [str(ins['id_partie']) for ins in inscriptions]
                    }
                )
                from vues.joueur.vue_details_partie_joueur import VueDetailsPartieJoueur
                return VueDetailsPartieJoueur(int(q_partie['choix']))
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
