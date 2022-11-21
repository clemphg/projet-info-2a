from pprint import pprint

from PyInquirer import Separator, prompt
from objets_metiers.joueur import Joueur

from vues.abstract_vue import AbstractVue

from vues.session import Session

from service.service_organisateur import ServiceOrganisateur


class VueJoueursOrganisateur(AbstractVue):
    def __init__(self) -> None:
        "Création JoueursOrganisateur avec la définiton d'une variable questions qui va stocker toutes les intéractions de l'organisateur. Il va pouvoir consulter sélectionner un joueur, consulter son profil de façon détaillé et/ou retourner au menu principal."
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Voir un joueur en détails',
                    'Retourner au menu principal'
                ]
            },
                        {
                'type': 'list',
                'name': 'choix_j',
                'message': 'Sélectionner un joueur',
                'choices': [j.pseudo for j in ServiceOrganisateur().liste_joueurs()]
            }
        ]

    def display_info(self):
        "S'affiche la liste des joueurs avec leur pseudo, leur âge et leur nombre de personnages. "
        print("-- Liste des joueurs --\n")
        joueurs = ServiceOrganisateur().liste_joueurs()
        for joueur in joueurs:
            print("> Pseudo            :",joueur.pseudo,
                  "\n  Age               :",joueur.age,
                  "\n  Nb de personnages :",len(joueur.personnages),"\n")

    def make_choice(self):
        "Si l'organisateur fait le choix de voir un joueur en détail, il lui sera proposé de selectionner un joueur parmi la liste à disposition. Après avoir terminé la selection, il lui sera retourné une nouvelle vue VueDetailsJoueurOrganisateurs. Dans le cas contraire, il fait le choix de retourner à son menu principal: il lui sera retourné la vue VuePrincipalOrganisateur."
        reponse = prompt(self.__questions[0])
        if reponse['choix'] == 'Voir un joueur en détails':
            choix_j = prompt(self.__questions[1])
            pseudo = choix_j['choix_j']
            joueurs = ServiceOrganisateur().liste_joueurs()
            joueur = [j for j in joueurs if j.pseudo == pseudo][0]
            from vues.organisateur.vue_details_joueur_organisateur import VueDetailsJoueurOrganisateur
            return VueDetailsJoueurOrganisateur(joueur)
        elif reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()
