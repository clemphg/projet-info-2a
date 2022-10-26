import os
from tkinter import E

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.partie import Partie
from objets_metiers.scenario import Scenario
from utils.singleton import Singleton
from objets_metiers.joueur import Joueur

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

    def creer_joueur(self,joueur: Joueur, mot_de_passe):
        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO joueur (pseudo_j , age)"
            "VALUES (%(pseudo)s,%(age)s) RETURNING id_joueur;"
            ,{
                "pseudo" : joueur.pseudo,
                "age" : joueur.age,
                })
            joueur.id = cursor.fetchone()[0]
        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO mdp (pseudo, mdp)"
            "VALUES (%(pseudo)s,%(mdp)s);"
            ,{
                "pseudo" : joueur.pseudo,
                "mdp" : mot_de_passe,
                })
        return joueur.id


    def creer_perso(self,perso: Personnage, pseudo_j):
        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO personnage (nom, age, niveau,race,classe,pseudo_j)"
            "VALUES (%(nom)s, %(age)s,%(niveau)s,%(race)s,%(classe)s,%(pseudo_j)s,) RETURNING id_perso;"
            ,{
                "nom" : perso.nom,
                "age" : perso.age,
                "niveau" : perso.niveau,
                "niveau" : perso.race,
                "niveau" : perso.classe,
                "niveau" : pseudo_j
                })
        return perso.id
    
    
    def creer_mj(self,mj: MaitreDeJeu, mot_de_passe):
        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO Maitre_de_jeu (pseudo_mj, age)"
            "VALUES (%(pseudo)s, %(age)s) RETURNING id_joueur;"
            ,{
                "pseudo" : mj.pseudo,
                "age" : mj.age,
                })
        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO mdp (pseudo, mdp)"
            "VALUES (%(pseudo)s,%(mdp)s);"
            ,{
                "pseudo" : mj.pseudo,
                "mdp" : mot_de_passe,
                })
            mj.id = cursor.fetchone()[0]
        return mj.id    

    def creer_scenario(self,scenario: Scenario, pseudo_mj):
        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO scenario (nom , descrip, niveau, pseudo_mj)"
            "VALUES (%(nom)s, %(descrip)s,%(niveau)s,%(pseudo_mj)s) RETURNING id_scenario;"
            ,{
                "nom" : scenario.nom,
                "descripp" : scenario.description,
                "niveau" : scenario.niveau_min,
                "pseudo_mj" : pseudo_mj
                })
            scenario.id = cursor.fetchone()[0]
        return scenario.id
    
    def creer_partie(self,partie: Partie):
        with CONNECTION.cursor() as cursor:
            cursor.execute("SELECT id_scenario"
            "FROM scenario"
            "WHERE nom=%(nom)s"
            , {"nom": partie.scenario})
            res=cursor.fetchone()
        
        if res is None:
            return None


        else:
            with CONNECTION.cursor() as cursor2:
                cursor2.execute("INSERT INTO partie (id_scenario, id_creneau)"
                "VALUES (%(id_scen)s, %(id_cren)s) RETURNING id_partie;"
                ,{
                "id_scen" : res[0],
                "id_cren" : partie.creneau
                })
                partie.id = cursor2.fetchone()[0]
            return parie.id

    def chercher_par_pseudo_j(self,pseudo_j):
        with CONNECTION.cursor() as cursor:
            cursor.execute("SELECT age"
            "FROM joueur "
            "WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo_j})
            res=cursor.fetchone()

        with CONNECTION.cursor() as cursor2:
            cursor2.execute("SELECT id, nom, age ,niveau , race, classe "
            "FROM personnage "
            "WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo_j})
            row=cursor2.fetchone()
            l=[]
            while row is not None:
                l.append(Personnage(row[0],row[1],row[2],row[4],row[3],row[5]))
                row=cursor2.fetchone()


        if res is not None :
            joueur=Joueur(pseudo,res[0],res2)
            return joueur
        else :
            print("pas de pseudo correspondant")

    def chercher_par_pseudo_mj(self,pseudo_mj):
        with CONNECTION.cursor() as cursor:
            cursor.execute("SELECT age"
            "FROM Maitre_de_jeu "
            "WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo_j})
            res=cursor.fetchone()
        
        with CONNECTION.cursor() as cursor2:
            cursor2.execute("SELECT id, nom , descrip, niveau "
            "FROM scenario "
            "WHERE pseudo_mj=%(pseudo)s"
            ,{"pseudo": pseudo_mj})
            row=cursor2.fetchone()
            l=[]
            while row is not None:
                l.append(Scenario(row[0],row[1],row[2],row[3]))
                row=cursor2.fetchone()

        if res is not None :
            mj=MaitreDeJeu(pseudo,res[0],l)
            return mj
        else :
            return None
    
    def chercher_par_nom_perso(self,nom_perso):
        with CONNECTION.cursor() as cursor:
            cursor2.execute("SELECT id, nom, age ,niveau, race, classe "
            "FROM personnage "
            "WHERE nom=%(nom_perso)s"
            , {"nom": nom_perso})
            res=cursor.fetchone()
        if res is not None :
            perso=Personnage(res[0],nom_perso,res[2],res[4],res[3],res[5])
            return perso
        else :
            return None
    
    
    def inscription_personnage(self,perso,id_partie):

        with CONNECTION.cursor() as cursor :
            cursor.execute("INSERT INTO inscription_perso (id_perso,id_partie)"
            "VALUES (%(id_perso)s, %(id_partie)s);"
            ,{
                "id_perso" : perso.id,
                "id_partie" : id_partie,
                 })
        
            
    
    def chercher_partie_creneaux(self,creneau):
        with CONNECTION.cursor() as cursor:
            cursor.execute("SELECT id_scenario, nom, descrip, niveau"
            "FROM scenario JOIN scenario.id_scenario ON partie.id_scenario"
            "WHERE partie.id_creneau=%(creneau)s"
            , {"creneau": creneau})
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append([row[0],Scenario(row[1],row[2],row[3])])
                row=cursor.fetchone()
        
        d=[]
        with CONNECTION.cursor() as cursor2:
            cursor2.execute("SELECT id_partie"
            "FROM partie "
            "WHERE id_creneau=%(creneau)s"
            , {"creneau": creneau})
            res=cursor2.fetchone()
            while res is not None:
                with CONNECTION.cursor() as cursor3:
                    cursor3.execute("SELECT id_personnage"
                    "FROM inscription perso "
                    "WHERE id_partie=%(id_partie)s"
                    , {"id_partie": res[0]})
                    idperso=cursor3.fetchone()
                    while perso is not None:
                        with CONNECTION.cursor() as cursor4:
                            cursor4.execute("SELECT id,nom, age ,niveau, race, classe"
                            "FROM inscription perso "
                            "WHERE id_perso=%(id_perso)s"
                            , {"id_perso": idperso[0]})
                            perso=cursor4.fetchone()
                            d.apppend([res[0],Personnage(perso[0],perso[1],perso[3],perso[2],perso[4],perso[5])])
                        idperso=cursor3.fetchone()
                res=cursor2.fetchone()
        p=[] #on intialise la liste qui va contenir des couples (id_partie,listes des perso de la partie)
        t=[]
        for i in range(len(d)):
            if d[i][0] not in s: #on parcours la liste composé de (id_partie,personnage)
                p_i=[d[i][0]]
                t.append(d[i][0]) #on intialise une liste contenant l'id de la partie 
                for l in d: 
                    p_l=[]#on initialise la liste qui va contenir tous les personnages inscrit à la partie id correspondant à [d[i][0]]
                    if l[0]==d[i][0]:
                        p_l.append(l[1]) #ajoute tous les personnages inscrits à d[i][0]
                p_i.append(p_l)
                p.append(p_i)
        s=[]
        with CONNECTION.cursor() as cursor2:
            cursor2.execute("SELECT id_partie,id_scenario"
            "FROM partie "
            "WHERE id_creneau=%(creneau)s"
            , {"creneau": creneau})
            res=cursor2.fetchone()
            while res is not None:
                s.append(res)
                res=cursor2.fetchone()
        p_c=[]
        for i in l:
            partie=Partie(creneau,i[1])
            for j in p:
                if i[0]==j[0]:
                    partie.liste_perso=j[1]
            p_c.append(partie)
    
    

    def liste_joueur(self):
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
            liste_j.append(self.chercher_par_pseudo_j(pseudo))
        return liste_j

    
    def supprimer_joueur(self,pseudo):
        with CONNECTION.cursor() as cursor:
            cursor.execute("DELETE FROM joueur"
            "WHERE pseudo_j=%(pseudo)s RETURNING TRUE"
            , {"pseudo": pseudo})
            sup_joueur=cursor.fetchone()
        with CONNECTION.cursor() as cursor:
            cursor.execute("DELETE FROM mdp"
            "WHERE pseudo=%(pseudo)s RETURNING TRUE"
            , {"pseudo": pseudo})
            sup_mdp=cursor.fetchone()
        return sup_joueur,sup_mdp
    
    def supprimer_mj(self,pseudo):
        with CONNECTION.cursor() as cursor:
            cursor.execute("DELETE FROM Maitre_de_jeu"
            "WHERE pseudo_mj=%(pseudo)s RETURNING TRUE"
            , {"pseudo": pseudo})
            sup_mj=cursor.fetchone()
        with CONNECTION.cursor() as cursor:
            cursor.execute("DELETE FROM mdp"
            "WHERE pseudo=%(pseudo)s RETURNING TRUE"
            , {"pseudo": pseudo})
            sup_mdp=cursor.fetchone()
        return sup_mj,sup_mdp

    def liste_mj(self):
        with CONNECTION.cursor() as cursor :
            cursor.execute("SELECT pseudo_mj"
            "FROM Maitre_de_jeu"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(row[0])
                row=cursor.fetchone()
        
        liste_j=[]
        for pseudo in l:
            liste_j.append(self.chercher_par_pseudo_mj(pseudo))
        return liste_j
    
    def liste_personnage(self):
        with CONNECTION.cursor() as cursor :
            cursor.execute("SELECT name"
            "FROM personnage"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(row[0])
                row=cursor.fetchone()
        
        liste_j=[]
        for name in l:
            liste_j.append(self.chercher_par_nom_perso(name))
        return liste_j

    def maj_classe(self,personnage,nvlle_classe):
        id=personnage.
        with CONNECTION.cursor() as cursor:
            cursor.execute("UPDATE personnage SET classe=%(nvlle_classe)s"
            "WHERE id_perso=%(id)s"
            ,{
                "nvlle_classe" : nvlle_classe,
                "id" : personnage.id
                })



