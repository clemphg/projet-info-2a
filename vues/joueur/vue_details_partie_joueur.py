from pprint import pprint

from PyInquirer import Separator, prompt

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
                    "Se désinscrire de la partie",
                    'Retour à la liste des inscriptions',
                    'Retourner au menu principal'
                ]
            }
        ]

    def display_info(self):
        print("--- Vue détaillée d'une partie ---\n")
        # à remplacer par un appel à un service
        partie = DAO().chercher_partie_par_id(self.__id_partie)

        print(
            "    ID          :",partie.id,"\n",
            "   Créneau     :", partie.creneau,"\n",
            "   Scénario    :\n",
            "       Nom            :",partie.scenario.nom,"\n",
            "       Niveau minimum :",partie.scenario.niveau_min,"\n",
            "       Description    :",partie.scenario.description,"\n",
            "   Personnages :\n"
        )
        for perso in partie.liste_persos:
            print(
                "      > ID :",perso.id,"\n",
                "       Nom :",perso.nom,"\n",
                "       Age :",perso.age,"\n",
                "       Niveau :",perso.niveau,"\n",
                "       Race :",perso.race,"\n",
                "       Classe :",perso.classe,"\n"
            )


    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix']=="Se désinscrire de la partie":
            res = DAO().desinscription_joueur(Session().utilisateur, self.__id_partie)
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