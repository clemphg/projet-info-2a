from pprint import pprint

from PyInquirer import Separator, prompt

#importation des vues
from vues.session import Session
from vues.abstract_vue import AbstractVue

#importation des services
from service.service_joueur import ServiceJoueur

class VueDetailsPartieJoueur(AbstractVue):
    def __init__(self, id_partie) -> None:
        '''Création de la vue VueDétailsPartieJoueur, dont
        les méthodes nécessiteront l'attribut identifiant
        de la partie et la définition de la variable
        questions qui va stocker les intéractions du joueur.
        Il peut se désinscrire de la partie en séléctionnant
        "Se désinscrire de la partie", retourner à la liste
        des inscriptions en séléctionnant "Retour à la
        liste des inscriptions" et/ou retourner au
        menu principal en séléctionnant "Retourner au
        menu principal".
        '''
        self.__id_partie = id_partie
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    "Se désinscrire de la partie",
                    'Retour à la liste des inscriptions',
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        '''Permet d'afficher sur la console "Vue
        détaillée d'une partie" ainsi que l'identifiant,
        le créneau, le scénario, le nom, le niveau minimum,
        la description du scénario, les personnages de
        la partie et, pour chacun de ces personnages :
        l'identifiant, le nom, l'âge, le niveau, la race et
        la classe.
        '''
        print("--- Vue détaillée d'une partie ---\n")
        # à remplacer par un appel à un service
        partie = ServiceJoueur().details_partie(self.__id_partie)
        print(partie,"\n")


    def make_choice(self):
        '''Permet d'afficher le menu à partir de la variable
        question. Ce qui s'affichera dépendra du choix
        du joueur. S'il séléctionne "Se désinscrire de la
        partie", il sera désinscrit et retournera sur la vue
        VuePartieJoueur. S'il séléctionne "Retour à la liste
        des inscriptions", il retournera également sur la vue
        VuePartieJoueur. S'il sélectionne "Retourner au menu
        principal", il sera amené sur la vue VuePrincipalJoueur.
        '''
        partie = ServiceJoueur().details_partie(self.__id_partie)
        perso = [perso for perso in partie.liste_persos if perso.pseudo_j == Session().utilisateur.pseudo][0]

        reponse = prompt(self.__questions)
        if reponse['choix']=="Se désinscrire de la partie":
            res = ServiceJoueur().desinscription_personnage(perso.id, self.__id_partie)
            from vues.joueur.vue_parties_joueur import VuePartiesJoueur
            return VuePartiesJoueur()
        elif reponse['choix']=='Retour à la liste des inscriptions':
            from vues.joueur.vue_parties_joueur import VuePartiesJoueur
            return VuePartiesJoueur()
        elif reponse['choix']=='Retourner au menu principal':
            from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
            return VuePrincipaleJoueur()
        else:
            pass
