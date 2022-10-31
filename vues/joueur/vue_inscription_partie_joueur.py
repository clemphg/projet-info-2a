from pprint import pprint

from PyInquirer import Separator, prompt

from vues.session import Session
from vues.abstract_vue import AbstractVue

from service.service_joueur import ServiceJoueur
class VueInscriptionPartieJoueur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix_creneau',
                'message': 'Sélectionner un créneau',
                'choices':
                    [str(creneau) for creneau in ServiceJoueur().liste_creneaux_dispos(Session().utilisateur)]
            },
            {
                'type': 'list',
                'name': 'choix_retour',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'validation',
                'message': 'Sélectionner un choix',
                'choices': [
                    "Valider l'inscription",
                    "Abandonner"
                ]
            }
        ]

    def display_info(self):
        print("--- Inscription à une partie ---\n")

        creneaux_dispo = [str(creneau) for creneau in ServiceJoueur().liste_creneaux_dispos(Session().utilisateur)]

        if len(creneaux_dispo)==0:
            print("Vous êtes déjà occupé sur tous les créneaux. Veillez vous désinscrire d'une partie pour vous inscrire à une autre.\n")


    def make_choice(self):
        creneaux_dispo = [str(creneau) for creneau in ServiceJoueur().liste_creneaux_dispos(Session().utilisateur)]
        if len(creneaux_dispo)>0:

            # choix du créneau
            reponse = prompt(self.__questions[0])
            creneau = reponse['choix_creneau']

            # choix de la partie
            parties = ServiceJoueur().parties_dispos_creneau(creneau)
            if len(parties)>0:
                for partie in parties:
                    "    ID          :",partie.id,"\n",
                    "   Créneau     :", partie.creneau,"\n",
                    "   Scénario    :\n",
                    "       Nom            :",partie.scenario.nom,"\n",
                    "       Niveau minimum :",partie.scenario.niveau_min,"\n",
                    "       Description    :",partie.scenario.description,"\n"

                reponse = prompt(
                    {
                    'type': 'list',
                    'name': 'choix_partie',
                    'message': 'Sélectionner une partie (selon leur ID)',
                    'choices': [str(partie.id)+" \n   Scénario : "+
                                partie.scenario.nom+"\n   Description : "+
                                partie.scenario.description+"\n   Niveau minimum : "+
                                str(partie.scenario.niveau_min) for partie in parties]
                    }
                )

                id_partie = int(reponse['choix_partie'].split(' ')[0])
                partie_sel = [partie for partie in parties if partie.id==int(id_partie)][0]

                # choix du personnage
                persos_ok = ServiceJoueur().persos_niv_sup_a(Session().utilisateur, partie_sel.scenario.niveau_min)

                if persos_ok:
                    reponse = prompt(
                        {
                        'type': 'list',
                        'name': 'choix_perso',
                        'message': 'Sélectionner un personnage',
                        'choices': [str(perso.id)+" : "+perso.nom+", "+str(perso.age)+" ans, "+perso.race+", niveau "+str(perso.niveau)+", "+perso.classe+")" for perso in persos_ok]
                        }
                    )

                    q_val = prompt(self.__questions[2])
                    if q_val['validation']=="Valider l'inscription":
                        id_perso = int(reponse['choix_perso'].split(' ')[0])
                        ServiceJoueur().inscription_perso(id_perso, id_partie)
                    elif q_val['validation']=='Abandonner':
                        print("Inscription abandonnée.\n")


                else:
                    print("Vous n'avez aucun personnage de niveau suffisant.\n")
                    reponse = prompt(self.__questions[1])
                    if reponse['choix_retour']=='Retourner au menu principal':
                        from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                        return VuePrincipaleJoueur()

            else :
                print("Aucune partie disponible sur ce créneau.\n")

            reponse = prompt(self.__questions[1])
            if reponse['choix_retour']=='Retourner au menu principal':
                from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                return VuePrincipaleJoueur()
        else:
            reponse = prompt(self.__questions[1])
            if reponse['choix_retour']=='Retourner au menu principal':
                from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                return VuePrincipaleJoueur()