import os
from tkinter import E

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.singleton import Singleton
from joueur import Joueur 

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

    def creer_joueur(joueur: Joueur, mot_de_passe):
        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO joueur (pseudo_j , mot_de_passe, age)"
            "VALUES (%(pseudo)s, %(mdp)s,%(age)s) RETURNING id_joueur;"
            ,{
                "pseudo" : joueur.pseudo,
                "mdp" : mot_de_passe
                "age" : joueur.age
                })
            joueur.id = cursor.fetchone()[0]
        return joueur.id

    def chercher_par_pseudo(pseudo):
        with CONNECTION.cursor() as cursor:
            cursor.execute("SELECT age"
            "FROM joueur "
            "WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo})
            res=cursor.fetchone()
        
        with CONNECTION.cursor() as cursor2:
            cursor2.execute("SELECT nom"
            "FROM personnage JOIN joueur ON personnage.pseudo_j=joueur.pseudo_j"
            "WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo})
             res2=cursor2.fetchone()
        
         if res is not None :
            joueur=Joueur(pseudo,res[0],res2)
            return joueur
        else :
            print("pas de pseudo correspondant")

    def liste_joueur():
        with CONNECTION.cursor() as cursor :
            cursor.execute("SELECT pseudo_j,age"
            "FROM joueur"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(Joueur(row[0],row[2]))
                row=cursor.fetchone()
        return l

    
    def creer_partie(partie: Partie):
        with CONNECTION.cursor() as cursor :
            cursor.execute("SELECT id_creneau"
            "FROM creneaux"
            "WHERE Date_debut=%(date)s"
            , {"date": partie.date})
            res=cursor.fetchone()
        
        with CONNECTION.cursor() as cursor2:
            cursor2.execute("SELECT id_scenario"
            "FROM scenario"
            "WHERE nom=%(nom)s"
            , {"nom": partie.scenario})
            res2=cursor2.fetchone()
        
        if res is None:
            print "pas de crenau corrspondant"
        
        elif res2 is None:
            print "le scenario n'existe pas en base"

        else :

            with CONNECTION.cursor() as cursor3:
                cursor3.execute("INSERT INTO partie (id_scenario, id_creneau)"
                "VALUES (%(id_scen)s, %(id_cren)s) RETURNING id_partie;"
                ,{
                "id_scen" : res2[0],
                "id_cren" : res[0]
                })
                partie.id = cursor3.fetchone()[0]
            return parie.id
    
    


