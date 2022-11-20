from pprint import pprint

from PyInquirer import Separator, prompt
from objets_metiers.scenario import Scenario


from vues.abstract_vue import AbstractVue
from vues.session import Session

from service.service_maitre_de_jeu import ServiceMaitreDeJeu

from objets_metiers.partie import Partie

class VueCreationPartieMJ(AbstractVue):
    def __init__(self) -> None:
        "Création de la vue avec la définition d'une variable questions qui va stocker toutes les intéractions du maître de jeu. Ici, il va pouvoir choisir de sélectionner un scénario et créer une partie en validant la sélection, il peut abandonner et même retourner au menu principal. "
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
        " Affiche 'Créer une nouvelle partie '"
        print("--- Créer une nouvelle partie ---")

    def make_choice(self):
        " Le maître du jeu va sélectionner un ou plusieurs créneaux parmi ses créneaux de libre. S'il est possible pour lui de créer une nouvelle partie sur les créneaux choisis, il aura le choix de sélectionner un de ses scénarios, de le valider et de créer donc une nouvelle partie, s'affichera doncle message suivant:'Partie créée' . Mais il pourra également abandonner son processus de création de partie et donc s'affichera sur l'écran 'Abandon'. Sinon, il peut tout à fait faire le choix de retourner au menu principal, la vue principale sera retournée. Dans le cas où il lui est impossible de créer une nouvelle partie sur les créneaux choisis, le message suivant s'affichera: 'Ce créneau est déjà complet, veuillez en choisir un autre.' et il pourra faire le choix de retourner au menu principal, dans ce cas-là sera retournée sa vue principale. Dans le cas où il n'a pas de créneaux disponibles, il sera affiché le message suivant: 'Vous n'avez pas de disponibilité.\nVous pouvez vous désinscrire (i.e. supprimer) une partie via le menu 'Mes parties'' et il pourra faire le choix de retourner au menu prncipal: la vue principale sera retournée "
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
