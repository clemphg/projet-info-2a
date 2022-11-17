import imp
from pprint import pprint
import regex

from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator

from vues.session import Session
from vues.abstract_vue import AbstractVue


class ValidationNom(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Za-z'eèàù ]{5,25}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un nom valide (entre 5 et 25 caractères, sans caractères spéciaux)',
                cursor_position=len(document.text)
            )

class ValidationDescription(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Za-z.,;!?' êîûéèàù]{0,200}$", document.text)
        if not ok:
            raise ValidationError(
                message="Les caractères spéciaux autorisés sont : ,.;!?'",
                cursor_position=len(document.text)
            )

class ValidationEntier(Validator):
    def validate(self, document):
        ok = regex.match("^\d{1,}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un entier',
                cursor_position=len(document.text)
            )

class VueCreationScenarioMJ(AbstractVue):
    def __init__(self) -> None:
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
        print("Création d'un scénario.\n")

    def make_choice(self):
        if len(Session().utilisateur.scenarios)<2:
            reponses = prompt(self.__questions[0:4])

            if reponses['validation'] == 'Créer le scénario':
                Session().utilisateur.creer_scenario(nom=reponses['choix_nom'],
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