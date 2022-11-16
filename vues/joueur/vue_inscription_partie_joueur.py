from pprint import pprint

from PyInquirer import Separator, prompt

#importation des vues
from vues.session import Session
from vues.abstract_vue import AbstractVue

#importation des services
from service.service_joueur import ServiceJoueur
class VueInscriptionPartieJoueur(AbstractVue):
    def __init__(self) -> None:
        '''Création de la vue VueInscriptionPartieJoueur, définition de la variable questions qui va stocker les
        intéractions du joueur. Il peut séléctionner un créneau en séléctionnant un créneau parmi la liste disponible,
        ou retourner au menu principal en séléctionnant "retourner au menu principal" ou valider l'inscription en
        séléctionnant "valider l'inscription" ou retourner à la vue précédente en séléctionnant "abandonner"
        '''
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
        '''Permet d'afficher sur la console "Inscription à une partie" ainsi que les créneaux qui restent disponibles.
        S'il ne reste aucun créneau, le message suivant s'affiche : "Vous êtes déjà occupé sur tous les créneaux
        Veuillez vous désinscrire d'une partie pour vous inscrire à une autre"
        '''

        print("--- Inscription à une partie ---\n")

        creneaux_dispo = [str(creneau) for creneau in ServiceJoueur().liste_creneaux_dispos(Session().utilisateur)]

        if len(creneaux_dispo)==0:
            print("Vous êtes déjà occupé sur tous les créneaux. Veuillez vous désinscrire d'une partie pour vous inscrire à une autre.\n")


    def make_choice(self):
        '''Permet d'afficher le menu à partir de la variable question. Ce qui s'affichera dépendra du choix
        du joueur. S'il choisit "séléctionner un créneau", il pourra choisir le créneau d'inscription de la partie.
        L'écran affiche l’ensemble des parties disponibles à ce créneau, avec une description associée à
        chacune de ces parties. Lorsque la partie est sélectionnée, le personnage doit être séléctionné, parmi ceux
        déjà créés. Si aucun personnage de niveau suffisant pour la partie n'a encore été créé, un message d'erreur
        s'affiche. Le joueur peut ensuite valider ou annuler l'inscription ou encore retourner au menu principal.
        '''

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
                    'message': 'Sélectionner une partie',
                    'choices': ["ID : "+str(partie.id)+" \n   Scénario : "+
                                partie.scenario.nom+"\n   Description : "+
                                partie.scenario.description+"\n   Niveau minimum : "+
                                str(partie.scenario.niveau_min) for partie in parties]
                    }
                )

                id_partie = int(reponse['choix_partie'].split(' ')[2])
                partie_sel = [partie for partie in parties if partie.id==int(id_partie)][0]

                # choix du personnage
                persos_ok = ServiceJoueur().persos_niv_sup_a(Session().utilisateur, partie_sel.scenario.niveau_min)

                if persos_ok:
                    reponse = prompt(
                        {
                        'type': 'list',
                        'name': 'choix_perso',
                        'message': 'Sélectionner un personnage',
                        'choices': ["ID : "+str(perso.id)+" : "+perso.nom+", "+str(perso.age)+" ans, "+perso.race+", niveau "+str(perso.niveau)+", "+perso.classe+")" for perso in persos_ok]
                        }
                    )

                    q_val = prompt(self.__questions[2])
                    if q_val['validation']=="Valider l'inscription":
                        id_perso = int(reponse['choix_perso'].split(' ')[2])
                        ServiceJoueur().inscription_perso(id_perso, id_partie)
                    elif q_val['validation']=='Abandonner':
                        print("Inscription abandonnée.\n")


                else:
                    #pas de personnage créé de niveau suffisant
                    print("Vous n'avez aucun personnage de niveau suffisant.\n")
                    reponse = prompt(self.__questions[1])
                    if reponse['choix_retour']=='Retourner au menu principal':
                        from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                        return VuePrincipaleJoueur()

            else :
                print("Aucune partie disponible sur ce créneau.\n")

            reponse = prompt(self.__questions[1])
            #retour au menu principal
            if reponse['choix_retour']=='Retourner au menu principal':
                from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                return VuePrincipaleJoueur()
        else:
            reponse = prompt(self.__questions[1])
            #retour au menu principal
            if reponse['choix_retour']=='Retourner au menu principal':
                from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
                return VuePrincipaleJoueur()
