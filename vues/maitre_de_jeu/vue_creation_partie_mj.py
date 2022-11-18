from pprint import pprint

from PyInquirer import Separator, prompt
from objets_metiers.scenario import Scenario


from vues.abstract_vue import AbstractVue
from vues.session import Session

from service.service_maitre_de_jeu import ServiceMaitreDeJeu

from objets_metiers.partie import Partie

class VueCreationPartieMJ(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
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
                'name': 'choix_scenario',
                'message': 'Sélectionner un scénario',
                'choices': [
                    "Scénario "+str(scenario.id)+
                    "\n     Nom : "+scenario.nom+
                    "\n     Description : "+scenario.description+
                    "\n     Niveau minimum : "+str(scenario.niveau_min) for scenario in Session().utilisateur.scenarios
                ]
            },
            {
                'type': 'list',
                'name': 'validation',
                'message': 'Sélectionner un choix',
                'choices': [
                    "Valider et créer la partie",
                    "Abandonner"
                ]
            }
        ]

    def display_info(self):
        print("--- Créer une nouvelle partie ---")

    def make_choice(self):
        creneaux_dispo = ServiceMaitreDeJeu().liste_creneaux_dispos(Session().utilisateur)
        if len(creneaux_dispo)>0:
            reponse = prompt(
                {
                'type': 'list',
                'name': 'choix_creneau',
                'message': 'Sélectionner un créneau',
                'choices': [str(creneau) for creneau in creneaux_dispo]
                }
            )
            creneau = int(reponse['choix_creneau'])
            if ServiceMaitreDeJeu().verifier_nvlle_partie_possible(creneau):
                reponse = prompt(self.__questions[1])
                id_scenario = int(reponse['choix_scenario'].split(' ')[1])
                scenario = [scenario for scenario in Session().utilisateur.scenarios if scenario.id==id_scenario][0]
                reponse = prompt(self.__questions[2])
                if reponse['validation']=="Valider et créer la partie":
                    partie = Partie(creneau = creneau, scenario=scenario)
                    ServiceMaitreDeJeu().creer_partie(partie)
                    print('Partie créée !\n')
                elif reponse['validation']=="Abandonner":
                    print("Abandon.\n")
                reponse = prompt(self.__questions[0])
                if reponse['choix_retour'] == 'Retourner au menu principal':
                    from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
                    return VuePrincipaleMJ()

            else:
                print("\nCe créneau est déjà complet, veuillez en choisir un autre.\n")
                reponse = prompt(self.__questions[0])
                if reponse['choix_retour'] == 'Retourner au menu principal':
                    from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
                    return VuePrincipaleMJ()
        else:
            print("\nVous n'avez pas de disponibilité.\nVous pouvez vous désinscrire (i.e. supprimer) une partie via le menu 'Mes parties'.\n")
            reponse = prompt(self.__questions[0])
            if reponse['choix_retour'] == 'Retourner au menu principal':
                from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
                return VuePrincipaleMJ()