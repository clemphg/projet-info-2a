from PyInquirer import Separator, prompt
import hashlib

# import vues
from vues.abstract_vue import AbstractVue
from vues.session import Session

from vues.joueur.vue_principale_joueur import VuePrincipaleJoueur
from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur

# import services
from service.service_inscription_connexion import ServiceInscriptionConnexion

class VueConnexion(AbstractVue):

    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'type_de_profil',
                'message': 'Type de profil',
                'choices': [
                    'Joueur',
                    'Maître de jeu',
                    'Organisateur'
                ]
            },
            {
                'type': 'input',
                'name': 'pseudo',
                'message': 'Pseudo'
            },
            {
                'type': 'password',
                'name': 'mot_de_passe',
                'message': 'Mot de passe'
            }
        ]

    def display_info(self):
        print("Renseignez vos identifiants")

    def make_choice(self):
        nb_essais = 3 # nombre d'essais de couples pseudo+mdp à faire avant d'etre redirigé vers page d'accueil
        vrai_pseudo = False
        vrai_mdp = False
        reponses = None

        while nb_essais>0 and (not(vrai_pseudo) or not(vrai_mdp)):
            nb_essais -= 1 # comptage du nombre d'essais

            reponses = prompt(self.__questions)

            # instanciation de l'utilisateur selon son type. si pseudo invalide pour le type on a None
            utilisateur = ServiceInscriptionConnexion().instancier_utilisateur(reponses['pseudo'],reponses['type_de_profil'])

            if utilisateur:
                vrai_pseudo = True
                vrai_mdp = ServiceInscriptionConnexion().verifier_mdp_correct(utilisateur.pseudo, reponses['mot_de_passe'])

            if vrai_pseudo and vrai_mdp:
                print("Authentification réussie")
            elif vrai_pseudo and not(vrai_mdp):
                print("Mot de passe incorrect. Il vous reste",nb_essais,"essais.")
            elif not(vrai_pseudo) and vrai_mdp:
                print("Mot de passe incorrect. Il vous reste",nb_essais,"essais.")
            else:
                print("Pseudo et mot de passe incorrects. Il vous reste",nb_essais,"essais.")

        # Si l'authentification a échoué
        if (not(vrai_pseudo) or not(vrai_mdp)):
            from vues.vue_accueil import VueAccueil
            return VueAccueil()

        # si l'authentification est réussie
        Session().utilisateur = utilisateur
        if reponses['type_de_profil']=='Joueur':
            return VuePrincipaleJoueur()
        elif reponses['type_de_profil']=='Maître de jeu':
            return VuePrincipaleMJ()
        elif reponses['type_de_profil']=='Organisateur':
            return VuePrincipaleOrganisateur()