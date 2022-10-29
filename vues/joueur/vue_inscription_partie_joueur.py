from pprint import pprint

from PyInquirer import Separator, prompt

from vues.session import Session
from vues.abstract_vue import AbstractVue

from dao.dao import DAO

class VueInscriptionPartieJoueur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix_creneau',
                'message': 'Sélectionner un créneau',
                'choices':
                    [str(creneau) for creneau in DAO().liste_creneaux_dispos_joueur(Session().utilisateur)]
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
        print("--- Inscription à une partie ---\n")

        creneaux_dispo = [str(creneau) for creneau in DAO().liste_creneaux_dispos_joueur(Session().utilisateur)]

        if len(creneaux_dispo)==0:
            print("Vous êtes déjà occupé sur tous les créneaux. Veillez vous désinscrire d'une partie pour vous inscrire à une autre.\n")


    def make_choice(self):
        creneaux_dispo = [str(creneau) for creneau in DAO().liste_creneaux_dispos_joueur(Session().utilisateur)]
        if len(creneaux_dispo)>0:

            # choix du créneau
            reponse = prompt(self.__questions[0])
            creneau = reponse['choix_creneau']

            # choix de la partie
            parties = DAO().chercher_parties_par_creneau(creneau)
            for partie in parties:
                "    ID          :",partie.id,"\n",
                "   Créneau     :", partie.creneau,"\n",
                "   Scénario    :\n",
                "       Nom            :",partie.scenario.nom,"\n",
                "       Niveau minimum :",partie.scenario.niveau_min,"\n",
                "       Description    :",partie.scenario.description,"\n",
                "   Personnages :\n"

            # choix du personnage

            # une fois que l'inscription est bien faite
            reponse = prompt(self.__questions[1])
            if reponse['choix']=='Retourner au menu principal':
                from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                return VuePrincipaleJoueur()
        else:
            reponse = prompt(self.__questions[1])
            if reponse['choix']=='Retourner au menu principal':
                from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                return VuePrincipaleJoueur()