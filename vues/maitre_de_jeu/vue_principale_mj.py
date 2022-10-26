from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue
from vues.joueur.vue_creation_personnage_joueur import VueCreationPersonnageJoueur
from vues.joueur.vue_inscription_partie_joueur import VueInscriptionPartieJoueur
from vues.joueur.vue_personnages_joueur import VuePersonnagesJoueur
from vues.joueur.vue_parties_joueur import VuePartiesJoueur
from vues.joueur.vue_notifs_joueur import VueNotificationsJoueur

from vues.session import Session

class VuePrincipaleMJ(AbstractVue):
    pass