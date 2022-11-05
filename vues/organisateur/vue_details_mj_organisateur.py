from pprint import pprint

from PyInquirer import Separator, prompt

from vues.abstract_vue import AbstractVue

from vues.session import Session

from service.service_organisateur import ServiceOrganisateur


class VueDetailsMJOrganisateur(AbstractVue):
    def __init__(self, mj) -> None:
        self.__mj = mj
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Bannir ce maître de jeu',
                    "Supprimer l'un de ses scénarios",
                    'Retour à la liste des maîtres de jeu',
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'retour',
                'message': 'Sélectionner un choix',
                'choices': [
                    'Retourner au menu principal'
                ]
            },
            {
                'type': 'list',
                'name': 'choix_scenario',
                'message': 'Sélectionner un scénario (selon son id)',
                'choices': [
                    str(scenario.id) for scenario in self.__mj.scenarios
                ]
            }
        ]

    def display_info(self):
        print("-- Détails sur un joueur --\n")

        print(
            "   Pseudo      :",self.__joueur.pseudo,"\n",
            "   Âge         :",self.__joueur.age,"\n",
            "   Scenarios   :\n"
        )
        for scenario in self.__mj.scenarios:
            print(
                "      > ID :",scenario.id,"\n",
                "       Nom :",scenario.nom,"\n",
                "       Description :",scenario.description,"\n",
                "       Niveau minimum :",scenario.niveau_min,"\n"
            )

    def make_choice(self):
        reponse = prompt(self.__questions[0])

        if reponse['choix'] == "Bannir ce maître de jeu":
            res = ServiceOrganisateur().bannir_mj(self.__mj)
            if res:
                print("Le maître de jeu ", self.__mj.pseudo," a bien été banni.")
            reponse = prompt(self.__questions[1])
            if reponse['retour']=='Retourner au menu principal':
                from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
                return VuePrincipaleOrganisateur()
        elif reponse['choix'] == "Supprimer l'un de ses scénarios":
            if len(self.__mj.scenarios)==0:
                print("Ce maître de jeu n'a aucun scénario.")
                reponse = prompt(self.__questions[1])
                if reponse['retour']=='Retourner au menu principal':
                    from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
                    return VuePrincipaleOrganisateur()
            else:
                reponse = prompt(self.__questions[2])
                id_s = reponse['choix_scenario']
                scenario = [s for s in self.__mj.scenarios if scenario.id==int(id_s)][0]
                res = ServiceOrganisateur().supprimer_scenario(scenario, self.__mj)
                if res:
                    print("Le scénario a bien été supprimé.")
                reponse = prompt(self.__questions[1])
                if reponse['retour']=='Retourner au menu principal':
                    from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
                    return VuePrincipaleOrganisateur()

        elif reponse['choix'] == 'Retour à la liste des maîtres de jeu':
            from vues.organisateur.vue_mjs_organisateur import VueMJsOrganisateur
            return VueMJsOrganisateur()
        elif reponse['choix']=='Retourner au menu principal':
            from vues.organisateur.vue_principale_organisateur import VuePrincipaleOrganisateur
            return VuePrincipaleOrganisateur()
        else:
            pass