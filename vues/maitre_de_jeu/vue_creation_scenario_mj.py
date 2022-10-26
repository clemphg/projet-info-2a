import imp
from pprint import pprint
import regex

from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator

from vues.session import Session
from vues.abstract_vue import AbstractVue

from objets_metiers.scenario import Scenario

from dao.dao import DAO


class ValidationNom(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Za-z'eèàù]{5,25}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un nom valide (entre 5 et 25 caractères, sans caractères spéciaux)',
                cursor_position=len(document.text)
            )

class ValidationDescription(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Za-z.,;!?' éèàù]{0,200}$", document.text)
        if not ok:
            raise ValidationError(
                message="Les caractères spéciaux autorisés sont : ,.;!?'",
                cursor_position=len(document.text)
            )

class ValidationEntier(Validator):
    def validate(self, document):
        ok = regex.match("^\d{2,3}$", document.text)
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
                'message': 'Classe',
                'choices': [
                    'Créer le scénario',
                    'Abandonner'
                ]
            },
            {
                'type': 'list',
                'name': 'retour',
                'message': 'Classe',
                'choices': [
                    "Retour à l'accueil"
                ]
            }
        ]

    def display_info(self):
        print("Création d'un scénario")

    def make_choice(self):
        if len(Session.utilsateur.scenarios)<2:
            reponses = prompt(self.__questions[0:4])

            if reponses['validation'] == 'Créer le personnage':
                scenar = Scenario(nom=reponses['choix_nom'],
                                age=reponses['choix_description'],
                                niveau_min=reponses['choix_niveau'])
                id = DAO.creer_scenario(scenar,
                                        Session.utilisateur.pseudo)
                scenar.id = id
                Session.utilisateur.creer_scenario(scenar)
                print('Le scénario a bien été créé !')
        else:
            print("Vous avez déjà deux scénarios, vous ne pouvez plus en créer.")

        choix_retour = prompt(self.__questions[4])
        if choix_retour['retour'] == "Retour à l'accueil":
            from vues.vue_accueil import VueAccueil
            return VueAccueil()
        else:
            pass