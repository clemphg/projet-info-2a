import os
import dotenv
import requests

from utils.singleton import Singleton

class ClientPersonnage(metaclass=Singleton):

    def __init__(self):
        dotenv.load_dotenv(override=True)
        self.__urlapi = os.environ["HOST_WEBSERVICE"]

    def races_possibles(self):
        """Retourne l'ensemble des races possibles que peut avoir un personnage dans le jeu"""
        res = requests.get(os.path.join(self.__urlapi,"races"))
        races = [row['name'] for row in res.json()["results"]]
        return races

    def classes_possibles(self):
        """Retourne l'ensemble des classes possibles que peut avoir un personnage dans le jeu"""
        res = requests.get(os.path.join(self.__urlapi,"classes"))
        classes = [row['name'] for row in res.json()["results"]]
        return classes
