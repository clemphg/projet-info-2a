import os
from tkinter import E

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from objets_metiers.maitre_de_jeu import MaitreDeJeu
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
                "mdp" : mot_de_passe,
                "age" : joueur.age,
                })
            joueur.id = cursor.fetchone()[0]

        for i in range len(joueur.personnage):
            perso=joueur.personnage[i]
            with CONNECTION.cursor() as cursor2 :
                cursor2.execute("INSERT INTO personnage (nom , age, race, niveau,classe)"
                "VALUES (%(nom)s, %(age)s,%(race)s,%(niveau)s,%(classe)s) RETURNING id_personnage;"
                ,{
                    "nom" : perso.nom,
                    "age" :perso.age,
                    "race" : perso.race,
                    "niveau":perso.niveau,
                    "classe":perso.classe
                    })
        
        return joueur.id

    def chercher_par_pseudo(pseudo):
        with CONNECTION.cursor() as cursor:
            cursor.execute("SELECT age"
            "FROM joueur "
            "WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo})
            res=cursor.fetchone()
        
        with CONNECTION.cursor() as cursor2:
            cursor2.execute("SELECT nom, age ,race , niveau, classe "
            "FROM personnage JOIN joueur ON personnage.pseudo_j=joueur.pseudo_j"
            "WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo})
            row=cursor2.fetchone()
            l=[]
            while row is not None:
                l.append(Personnage(row[0],row[1],row[2],row[3],row[4]))
                row=cursor2.fetchone()

        if res is not None :
            joueur=Joueur(pseudo,res[0],l)
            return joueur
        else :
            print("pas de pseudo correspondant")

    
    def liste_joueur():
        with CONNECTION.cursor() as cursor :
            cursor.execute("SELECT pseudo_j"
            "FROM joueur"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(row[0])
                row=cursor.fetchone()
        
        liste_j=[]
        for pseudo in l:
            liste_j.append(chercher_par_pseudo(pseudo))
        return liste_j

    
    def supprimer_joueur(pseudo):
        with CONNECTION.cursor() as cursor:
            cursor.execute("DELETE FROM joueur"
            "WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo})
    


     def MaitreDeJeu(mj: MaitreDeJeu, mot_de_passe):
        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO joueur (pseudo_j , mot_de_passe, age)"
            "VALUES (%(pseudo)s, %(mdp)s,%(age)s) RETURNING id_joueur;"
            ,{
                "pseudo" : joueur.pseudo,
                "mdp" : mot_de_passe,
                "age" : joueur.age,
                })
            joueur.id = cursor.fetchone()[0]

        for i in range len(joueur.personnage):
            perso=joueur.personnage[i]
            with CONNECTION.cursor() as cursor2 :
                cursor2.execute("INSERT INTO personnage (nom , age, race, niveau,classe)"
                "VALUES (%(nom)s, %(age)s,%(race)s,%(niveau)s,%(classe)s) RETURNING id_personnage;"
                ,{
                    "nom" : perso.nom,
                    "age" :perso.age,
                    "race" : perso.race,
                    "niveau":perso.niveau,
                    "classe":perso.classe
                    })
    
    
    
    def creer_partie(partie: Partie):
        with CONNECTION.cursor() as cursor:
            cursor.execute("SELECT id_scenario"
            "FROM scenario"
            "WHERE nom=%(nom)s"
            , {"nom": partie.scenario})
            res=cursor.fetchone()
        
        with CONNEXION.CURSOR 
        if res2 is None:
            print "le scenario n'existe pas en base"

        else:
            with CONNECTION.cursor() as cursor2:
                cursor2.execute("INSERT INTO partie (id_scenario, id_creneau)"
                "VALUES (%(id_scen)s, %(id_cren)s) RETURNING id_partie;"
                ,{
                "id_scen" : res[0],
                "id_cren" : partie.date
                })
                partie.id = cursor3.fetchone()[0]
            return parie.id

    
    
    
    


