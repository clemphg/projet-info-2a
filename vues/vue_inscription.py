from pprint import pprint

import regex
from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator

from vues.abstract_vue import AbstractVue
from vues.session import Session

class ValidationMDP(Validator):
    def validate(self, document):
        ok = regex.match(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{10,}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un mot de passe valide',
                cursor_position=len(document.text)
            )

class VueInscription(AbstractVue):

    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'list',
                'name': 'type_de_profil',
                'message': 'Type de profil souhaité',
                'choices': [
                    'Joueur',
                    'Maître de jeu'
                ]
            },
            {
                'type': 'input',
                'name': 'pseudo',
                'message': 'Pseudo (au moins 6 caractères en minuscules, sans caractères spéciaux)'
            },
            {
                'type': 'input',
                'name': 'age',
                'message': 'Age'
            },
            {
                'type': 'password',
                'name': 'mot_de_passe',
                'message': 'Mot de passe (au moins 10 caractères, au moins une capitale, un nombre et un caractère spécial)',
                'validate': ValidationMDP
            }
        ]

    def display_info(self):
        print("Compléter le formulaire")

    def make_choice(self):
        reponses = prompt(self.__questions)
        pprint("Inscription réussie !")
        from vues.accueil_vue import VueAccueil
        return VueAccueil()