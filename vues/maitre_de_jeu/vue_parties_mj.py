from pprint import pprint

from PyInquirer import Separator, prompt


from vues.abstract_vue import AbstractVue

from dao.dao import DAO
from vues.session import Session

class VuePartiesMJ(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Voir une partie en détail',
                    'Retourner au menu principal'
                ]
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
        print("--- Liste de mes parties ---\n")
        # à remplacer par un appel à un service
        inscriptions = DAO().liste_inscriptions_mj(Session().utilisateur.pseudo)

        if inscriptions :
            for ins in inscriptions:
                print(
                    ">  Créneau              :",ins['id_creneau'],"\n",
                    "  ID de partie         :",ins['id_partie'],"\n",
                    "  Scénario             :",ins['nom_scenario'],"\n",
                    "  Niveau minimum       :",ins['niv_min_scenario'],"\n"
                    )
        else:
            print(
                "Vous n'avez créé aucune partie.\n"
                "Vous pouvez en créer une via l'onglet 'Créer une partie' du menu principal.\n")

    def make_choice(self):
        inscriptions = DAO().liste_inscriptions_mj(Session().utilisateur.pseudo)
        if inscriptions:
            reponse = prompt(self.__questions[0])
            if reponse['choix']=='Voir une partie en détail':
                q_partie = prompt(
                    {
                        'type': 'list',
                        'name': 'choix',
                        'message': 'Sélectionner une partie (selon son ID)',
                        'choices': [str(ins['id_partie']) for ins in inscriptions]
                    }
                )
                from vues.maitre_de_jeu.vue_details_partie_mj import VueDetailsPartieMJ
                return VueDetailsPartieMJ(int(q_partie['choix']))
            elif reponse['choix']=='Retourner au menu principal':
                from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
                return VuePrincipaleMJ()
            else:
                pass
        else :
            reponse = prompt(self.__questions[1])
            if reponse['choix']=='Retourner au menu principal':
                from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
                return VuePrincipaleMJ()
            else:
                pass