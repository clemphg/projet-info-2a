import imp
from pkgutil import ImpImporter
from pprint import pprint
import dotenv
import os
import requests
import regex

from PyInquirer import Separator, prompt
from prompt_toolkit.validation import ValidationError, Validator
from utils.singleton import Singleton

from vues.session import Session
from vues.abstract_vue import AbstractVue

from objets_metiers.personnage import Personnage

from dao.dao import DAO


class ValidationInput(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Z]{0,1}[a-z]{5,25}$", document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez entrer un nom valide (entre 5 et 25 caractères, majuscule uniquement pour la première lettre)',
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

class AppelAPI(Singleton):
    def __init__(self):
        dotenv.load_dotenv(override=True)
        self.__urlapi = os.environ["HOST_WEBSERVICE"]

    def races_possibles(self):
        res = requests.get(os.path.join(self.__urlapi,"races"))
        races = [row['name'] for row in res.json()["results"]]
        return races

    def classes_possibles(self):
        res = requests.get(os.path.join(self.__urlapi,"classes"))
        classes = [row['name'] for row in res.json()["results"]]
        return classes


class VueCreationPersonnageJoueur(AbstractVue):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'choix_nom',
                'message': 'Nom',
                'validate': ValidationInput
            },
            {
                'type': 'input',
                'name': 'choix_age',
                'message': 'Age',
                'validate': ValidationEntier
            },
            {
                'type': 'list',
                'name': 'choix_race',
                'message': 'Race',
                'choices': AppelAPI.races_possibles()
            },
            {
                'type': 'input',
                'name': 'choix_niveau',
                'message': 'Niveau',
                'validate': ValidationEntier
            },
            {
                'type': 'list',
                'name': 'choix_classe',
                'message': 'Classe',
                'choices': AppelAPI.classes_possibles()
            },
            {
                'type': 'list',
                'name': 'validation',
                'message': 'Classe',
                'choices': [
                    'Créer le personnage',
                    'Abandonner'
                ]
            }
        ]

    def display_info(self):
        print("Création d'un personnage")

    def make_choice(self):
        reponses = prompt(self.__questions)

        if reponses['validation'] == 'Créer le personnage':
            perso = Personnage(nom=reponses['choix_nom'],
                               age=reponses['choix_age'],
                               race=reponses['choix_race'],
                               niveau=reponses['choix_niveau'],
                               classe=reponses['classe'])
            id = DAO().creer_perso(perso,
                                 Session().utilisateur.pseudo)
            perso.id = id
            Session().utilisateur.creer_personnage(perso)
            print('Le personnage a bien été créé !')

        from vues.vue_accueil import VueAccueil
        return VueAccueil()