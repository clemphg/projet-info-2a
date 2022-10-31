from pprint import pprint

import regex
from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator

# import des vues
from vues.abstract_vue import AbstractVue
from vues.session import Session

# import des services
from service.service_inscription_connexion import ServiceInscriptionConnexion

class ValidationPseudo(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Za-z0-9_.]{6,25}$", document.text)
        if ok:
            # vérifier que le pseudo n'est pas déjà dans la base
            libre = ServiceInscriptionConnexion().verifier_pseudo_libre(document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un pseudo valide',
                cursor_position=len(document.text)
            )
        elif not libre:
            raise ValidationError(
                message='Pseudo déjà utilisé. Veuillez en entrer un autre',
                cursor_position=len(document.text)
            )

class ValidationAge(Validator):
    def validate(self, document):
        if regex.match("^\d{2,3}$", document.text):
            ok = 13<int(document.text)<120
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

        ServiceInscriptionConnexion().creer_utilisateur(reponses['pseudo'],
                                                        reponses['age'],
                                                        reponses['mot_de_passe'],
                                                        reponses['type_de_profil'])

        print("Inscription réussie ! Vous pouvez désormais vous connecter avec vos identifiants.")
        from vues.vue_accueil import VueAccueil
        return VueAccueil()