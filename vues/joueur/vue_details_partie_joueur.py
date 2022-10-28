

from vues.abstract_vue import AbstractVue
from vues.abstract_vue import AbstractVue

from dao.dao import DAO

from vues.session import Session

class VueDetailsPartieJoueur(AbstractVue):
    def __init__(self, id_partie) -> None:
        self.__id_partie = id_partie
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    "Se désinscrire d'un partie"
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        print("--- Vue détaillée d'une partie ---\n")
        # à remplacer par un appel à un service
        partie = DAO().chercher_partie_par_id(self.__id_partie)

        print()



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