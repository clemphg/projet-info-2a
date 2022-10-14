import os

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.singleton import Singleton


from utils.singleton import Singleton


class DAO(Singleton):
    dotenv.load_dotenv(override=True)
    CONNECTION=psycopg2.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor)

    def creer_joueur(joueur: Joueur):
        with CONNECTION.cursor() as cursor :
            curseur.execute("INSERT INTO joueur (pseudo_j , mot_de_passe, age)"
            "VALUES (%(pseudo)s, %(mdp)s,%(age)s) RETURNING id_joueur;"
            ,{
                "pseudo" : joueur.pseudo,
                "name" : joueur.mot_de_passe
                "description" : joueur.description
                })
            joueur.id = curseur.fetchone()[0]
        return joueur.id


