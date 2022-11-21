import imp
from pprint import pprint
import regex

from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator

from vues.session import Session
from vues.abstract_vue import AbstractVue

from service.service_maitre_de_jeu import ServiceMaitreDeJeu
from objets_metiers.scenario import Scenario


class ValidationNom(Validator):
    def validate(self, document):
        " Permet de vérifier que le texte rentré ici défini comme document ait un nombre de caractères entre 5 et 25 caractères, sans caractères spéciaux, et affiche un message d'erreur si ce n'est pas le cas"
        ok = regex.match("^[A-Za-z'eèàù ]{5,25}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un nom valide (entre 5 et 25 caractères, sans caractères spéciaux)',
                cursor_position=len(document.text)
            )

class ValidationDescription(Validator):
    def validate(self, document):
        " Permet de vérifier que le texte rentré ici défini comme document n'ait pas de caractères spéciaux qui ne seraient pas autorisés, et affiche un message d'erreur si ce n'est pas le cas"
        ok = regex.match("^[A-Za-z.,;!?' êîûéèàù]{0,200}$", document.text)
        if not ok:
            raise ValidationError(
                message="Les caractères spéciaux autorisés sont : ,.;!?'",
                cursor_position=len(document.text)
            )

class ValidationEntier(Validator):
    def validate(self, document):
        " Permet de vérifier que le texte rentré ici défini comme document soit bien un nombre entier sinon s'affiche un message d'erreur."
        ok = regex.match("^\d{1,}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un entier',
                cursor_position=len(document.text)
            )

class VueCreationScenarioMJ(AbstractVue):
    def __init__(self) -> None:
        "Création d'une vue Création Scénario avec la défintion d'une variable questions, qui va stocker l'ensemble des intéractions du maître de jeu. Il pourra choisir de créer un scénario et valider le nom du scénario, le niveau minimum recquis des personnages ainsi que la description du scénario. Le maître de jeu peut également choisir d'abandonner la création de scénario et/ou retourner sur son menu principal. "
        self.__questions = [
            {
                'type': 'input',
                'name': 'choix_nom',
                'message': 'Nom',
                'validate': ValidationNom
            },
            {
                'type': 'input',
                'name': 'choix_description',
                'message': 'Description',
                'validate': ValidationDescription
            },
            {
                'type': 'input',
                'name': 'choix_niveau_min',
                'message': 'Niveau minimum des personnages',
                'validate': ValidationEntier
            },
            {
                'type': 'list',
                'name': 'validation',
                'message': 'Sélectionner une choix',
                'choices': [
                    'Créer le scénario',
                    'Abandonner'
                ]
            },
            {
                'type': 'list',
                'name': 'retour',
                'message': '',
                'choices': [
                    "Retour à l'accueil"
                ]
            }
        ]

    def display_info(self):
        "Affiche sur l'écran 'Création d'un scénario'"
        print("Création d'un scénario.\n")

    def make_choice(self):
        "Permet d'afficher le menu à partir de la variable questions. Ce qui s'affichera dépendra des choix du maître de jeu. Si celui-ci décide de créer son scénario, il pourra le faire à condition qu'il ait validé le nom de son scénario, la description correspondante et le niveau minimum requis pour les personnages. Il s'affichera un message comme quoi le scénario a bien été créé. De plus, le scénario nouvellement créé sera stocké dans la base de données. Dans le cas où il a plus de deux scénarions, il sera affiché un message comme quoi le maître de jeu ne peut pas créer un nouveau scénario car il en a dejà deux. Finalement, il lui sera proposé de retourner au menu principal, et sera donc retournée sa vue principale.'"
        if len(Session().utilisateur.scenarios)<2:
            reponses = prompt(self.__questions[0:4])

            if reponses['validation'] == 'Créer le scénario':
                scenario = Scenario(nom=reponses['choix_nom'],
                                    description=reponses['choix_description'],
                                    niveau_min=int(reponses['choix_niveau_min']),
                                    pseudo_mj=Session().utilisateur.pseudo)
                id = ServiceMaitreDeJeu().creer_scenario(scenario)
                Session().utilisateur.creer_scenario(id=id,
                                                     nom=reponses['choix_nom'],
                                                     description=reponses['choix_description'],
                                                     niveau_min=int(reponses['choix_niveau_min']))
                print('Le scénario a bien été créé !')
        else:
            print("Vous avez déjà deux scénarios, vous ne pouvez pas en créer plus.\n")

        choix_retour = prompt(self.__questions[4])
        if choix_retour['retour'] == "Retour à l'accueil":
            from vues.maitre_de_jeu.vue_principale_mj import VuePrincipaleMJ
            return VuePrincipaleMJ()
        else:
            pass
