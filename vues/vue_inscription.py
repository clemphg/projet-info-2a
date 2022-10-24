from pprint import pprint

import regex
from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator

from vues.abstract_vue import AbstractVue
from vues.session import Session


class ValidationPseudo(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Za-z][A-Za-z0-9_.]{6,25}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un pseudo valide',
                cursor_position=len(document.text)
            )

class ValidationAge(Validator):
    def validate(self, document):
        if regex.match("^\d{2,3}$", document.text):
            ok = 13<document.text<120
        else :
            ok = False
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un age valide',
                cursor_position=len(document.text)
            )

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
                'message': 'Pseudo (de 6 à 25 caractères, caractères spéciaux autorisés : ._ )',
                'validate': ValidationPseudo
            },
            {
                'type': 'input',
                'name': 'age',
                'message': 'Age',
                'validate': ValidationAge
            },
            {
                'type': 'password',
                'name': 'mot_de_passe',
                'message': 'Mot de passe (au moins 10 caractères, une capitale, un nombre et un caractère spécial parmi @$!%*#?&)',
                'validate': ValidationMDP
            }
        ]

    def display_info(self):
        print("Compléter le formulaire")

    def make_choice(self):
        reponses = prompt(self.__questions)

        # ajouter l'utilisateur créé dans la base


        pprint("Inscription réussie !")
        from vues.accueil_vue import VueAccueil
        return VueAccueil()