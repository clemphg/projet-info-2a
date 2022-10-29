from pprint import pprint

from PyInquirer import Separator, prompt

from vues.session import Session
from vues.abstract_vue import AbstractVue

from dao.dao import DAO

class VueDetailsPartieMJ(AbstractVue):
    def __init__(self, id_partie) -> None:
        self.__id_partie = id_partie
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    "Supprimer la partie",
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
        if reponse['choix']=="Supprimer la partie":
            res = DAO().supprimer_partie(Session().utilisateur, self.__id_partie)
            from vues.maitre_de_jeu.vue_parties_mj import VuePartiesMJ
            return VuePartiesMJ()
        elif reponse['choix']=='Retourner au menu principal':
            from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
            return VuePrincipaleMJ()
        else:
            pass