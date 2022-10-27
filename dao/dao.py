import os
from tkinter import INSERT

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from objets_metiers.maitre_de_jeu import MaitreDeJeu
from objets_metiers.partie import Partie
from objets_metiers.scenario import Scenario
from utils.singleton import Singleton
from objets_metiers.joueur import Joueur
from objets_metiers.personnage import Personnage
from objets_metiers.organisateur import Organisateur

from utils.singleton import Singleton


class DAO(metaclass=Singleton):
    def __init__(self):
        dotenv.load_dotenv(override=True)
        self.__connection=psycopg2.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor)
        self.__connection.autocommit = True

    def creer_joueur(self, joueur: Joueur, mot_de_passe):
        """Ajouter un joueur dans la base de données

        Parameters
        ----------
        joueur : Joueur
            Joueur à ajouter dans la base
        mot_de_passe : str
            Mot de passe haché du joueur

        Returns
        -------
        bool
            True si le pseudo du joueur est bien retrouvé dans les tables, False sinon
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("INSERT INTO joueur (pseudo_j , age)"
            "VALUES (%(pseudo)s,%(age)s);"
            ,{
                "pseudo" : joueur.pseudo,
                "age" : joueur.age,
                })
            cursor.execute("INSERT INTO mdp (pseudo, mdp)"
            "VALUES (%(pseudo)s,%(mdp)s);"
            ,{
                "pseudo" : joueur.pseudo,
                "mdp" : mot_de_passe,
                })
        # on vérifie l'insertion
        with self.__connection.cursor() as cursor :
            cursor.execute("SELECT COUNT(*) FROM joueur WHERE pseudo_j=%(pseudo)s;"
            ,{"pseudo" : joueur.pseudo})
            test1 = cursor.fetchone()['count']

            cursor.execute("SELECT COUNT(*) FROM mdp WHERE pseudo=%(pseudo)s;"
            ,{"pseudo" : joueur.pseudo})
            test2 = cursor.fetchone()['count']

        if test1==1 and test2==1:
            return True
        else :
            return False


    def creer_perso(self,perso: Personnage, pseudo_j):
        """Ajouter un personnage en base de données

        Parameters
        ----------
        perso : Personnage
            Personnage à ajouter dans la base
        pseudo_j : str
            Pseudo du joueur a qui appartient le personnage

        Returns
        -------
        int
            id du personnage ajouté en base
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("INSERT INTO personnage (nom, age, niveau,race,classe,pseudo_j)"
            "VALUES (%(nom)s, %(age)s,%(niveau)s,%(race)s,%(classe)s,%(pseudo_j)s) RETURNING id_perso;"
            ,{
                "nom" : perso.nom,
                "age" : perso.age,
                "niveau" : perso.niveau,
                "race" : perso.race,
                "classe" : perso.classe,
                "pseudo_j" : pseudo_j
                })
            res=cursor.fetchone()['id_perso']
        return res


    def creer_mj(self, mj: MaitreDeJeu, mot_de_passe):
        """Ajouter un maitre de jeu en base

        Parameters
        ----------
        mj : MaitreDeJeu
            Maitre de jeu à ajouter dans la base
        mot_de_passe : str
            Mot de passe haché du maitre de jeu

        Returns
        -------
        bool
            True si le maitre de jeu a bien été ajouté, false sinon
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("INSERT INTO maitre_de_jeu (pseudo_mj, age)"
            "VALUES (%(pseudo)s, %(age)s);"
            ,{
                "pseudo" : mj.pseudo,
                "age" : mj.age,
                })

            cursor.execute("INSERT INTO mdp (pseudo, mdp)"
            "VALUES (%(pseudo)s,%(mdp)s);"
            ,{
                "pseudo" : mj.pseudo,
                "mdp" : mot_de_passe,
                })

            # on vérifie que le mj a bien été ajouté
            cursor.execute("SELECT COUNT(*) FROM maitre_de_jeu WHERE pseudo_mj = %(pseudo)s;"
            ,{
                "pseudo" : mj.pseudo,
                })
            test1 = cursor.fetchone()['count']
            cursor.execute("SELECT COUNT(*) FROM mdp WHERE pseudo = %(pseudo)s;"
            ,{
                "pseudo" : mj.pseudo,
                })
            test2 = cursor.fetchone()['count']
        if test1==1 and test2==1:
            return True
        else:
            return False

    def creer_scenario(self,scenario: Scenario, pseudo_mj):
        """Ajouter un scenario en base

        Parameters
        ----------
        scenario : Scenario
            Scénario à ajouter en base
        pseudo_mj : str
            Pseudo du maitre de jeu a qui le scénario appartient

        Returns
        -------
        int
            id du scénario
        """
        with self.__connection.cursor() as cursor :
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

    def creer_partie(self, partie: Partie):
        """Ajouter une nouvelle partie dans la base

        Parameters
        ----------
        partie : Partie
            Partie à ajouter dans la base

        Returns
        -------
        id
            id de la partie
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("INSERT INTO partie (id_scenario, id_creneau)"
            "VALUES (%(id_scen)s, %(id_cren)s) RETURNING id_partie;"
            ,{
            "id_scen" : partie.scenario.id,
            "id_cren" : partie.creneau
            })
            partie.id = cursor.fetchone()[0]
        return partie.id

    def chercher_par_pseudo_j(self,pseudo_j):
        """Chercher un joueur selon son pseudo

        Parameters
        ----------
        pseudo_j : str
            Pseudo du joueur à chercher

        Returns
        -------
        Joueur
            Joueur si le joueur est trouvé, None sinon
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("SELECT age"
            " FROM joueur "
            " WHERE pseudo_j=%(pseudo)s"
            , {"pseudo": pseudo_j})
            age=cursor.fetchone()

            if age is not None :
                cursor.execute("SELECT id_perso, nom, age ,niveau , race, classe "
                "FROM personnage "
                "WHERE pseudo_j=%(pseudo)s"
                , {"pseudo": pseudo_j})
                row=cursor.fetchone()
                l=[]
                while row is not None:
                    l.append(Personnage(row['id_perso'],row['nom'],row['age'],row['race'],row['niveau'],row['classe']))
                    row=cursor.fetchone()

                joueur=Joueur(pseudo_j,age['age'],l)
                return joueur
        return None

    def chercher_par_pseudo_mj(self,pseudo_mj):
        """Chercher un maitre de jeu par son pseudo

        Parameters
        ----------
        pseudo_mj : str
            Pseudo du maitre de jeu

        Returns
        -------
        MaitreDeJeu
            Retourne le MJ s'il existe, None sinon
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("SELECT age"
            " FROM Maitre_de_jeu "
            " WHERE pseudo_mj=%(pseudo)s"
            , {"pseudo": pseudo_mj})
            age=cursor.fetchone()

            if age is not None :
                cursor.execute("SELECT id_scenario, nom , descrip, niveau "
                "FROM scenario "
                "WHERE pseudo_mj=%(pseudo)s"
                ,{"pseudo": pseudo_mj})
                row=cursor.fetchone()
                l=[]
                while row is not None:
                    l.append(Scenario(row['id_scenario'],row['nom'],row['descrip'],row['niveau']))
                    row=cursor.fetchone()

                mj=MaitreDeJeu(pseudo_mj,age['age'],l)
                return mj
        return None

    def chercher_par_id_perso(self, id_perso):
        """Chercher un personnage par son

        Parameters
        ----------
        id_perso : int
            id du personnage

        Returns
        -------
        Personnage
            Personnage s'il existe, None sinon
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("SELECT id, nom, age ,niveau, race, classe "
            "FROM personnage "
            "WHERE id=%(id_perso)s"
            , {"id_perso": id_perso})
            res=cursor.fetchone()
        if res is not None :
            perso=Personnage(id_perso, res[1],res[2],res[4],res[3],res[5])
            return perso
        else :
            return None


    def inscription_personnage(self, perso, id_partie):
        """Inscrire un personnage à une partie

        Parameters
        ----------
        perso : Personnage
            Personnage à inscrire
        id_partie : int
            id de la partie à laquelle inscrire le personnage
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("INSERT INTO inscription_perso (id_perso,id_partie)"
            "VALUES (%(id_perso)s, %(id_partie)s);"
            ,{
                "id_perso" : perso.id,
                "id_partie" : id_partie,
                 })

    def chercher_parties_creneaux(self,creneau):
        """Chercher les parties se déroulant sur un creneau donné

        Parameters
        ----------
        creneau : int
            id du créneau

        Returns
        -------
        List[Partie]
            Liste de parties ou None si aucune partie
        """
        with self.__connection.cursor() as cursor:

            # liste des scénarios
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
        with self.__connection.cursor() as cursor2:
            cursor2.execute("SELECT id_partie"
            "FROM partie "
            "WHERE id_creneau=%(creneau)s"
            , {"creneau": creneau})
            res=cursor2.fetchone()
            while res is not None:
                with self.__connection.cursor() as cursor3:
                    cursor3.execute("SELECT id_personnage"
                    "FROM inscription perso "
                    "WHERE id_partie=%(id_partie)s"
                    , {"id_partie": res[0]})
                    idperso=cursor3.fetchone()
                    while perso is not None:
                        with self.__connection.cursor() as cursor4:
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
        with self.__connection.cursor() as cursor2:
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
        """Liste des joueurs

        Returns
        -------
        List[Joueur]
            Liste de tous les joueurs
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("SELECT pseudo_j"
            "FROM joueur"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(row[0])
                row=cursor.fetchone()

        liste_j=[self.chercher_par_pseudo_j(pseudo) for pseudo in l if pseudo is not None]
        return liste_j


    def bannir_joueur(self,pseudo):
        """Bannir un joueur (le supprimer définitivement)

        Parameters
        ----------
        pseudo : str
            Pseudo du joueur à bannir

        Returns
        -------
        bool
            True s'il est bien supprimé, False sinon
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("DELETE FROM joueur"
            "WHERE pseudo_j=%(pseudo)s RETURNING TRUE"
            , {"pseudo": pseudo})
            sup_joueur=cursor.fetchone()
            cursor.execute("DELETE FROM mdp"
            "WHERE pseudo=%(pseudo)s RETURNING TRUE"
            , {"pseudo": pseudo})
            sup_mdp=cursor.fetchone()
        return sup_joueur and sup_mdp

    def bannir_mj(self,pseudo):
        """Supprimer (bannir) un maitre de jeu

        Parameters
        ----------
        pseudo : str
            Pseudo du maitre de jeu à bannir

        Returns
        -------
        bool
            True si MJ bien supprimé, False sinon
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("DELETE FROM Maitre_de_jeu"
            "WHERE pseudo_mj=%(pseudo)s RETURNING TRUE"
            , {"pseudo": pseudo})
            sup_mj=cursor.fetchone()
            cursor.execute("DELETE FROM mdp"
            "WHERE pseudo=%(pseudo)s RETURNING TRUE"
            , {"pseudo": pseudo})
            sup_mdp=cursor.fetchone()
        return sup_mj and sup_mdp

    def liste_mj(self):
        """Liste des maitres de jeu

        Returns
        -------
        List[MaitreDeJeu]
            Liste des maitres de jeu
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("SELECT pseudo_mj"
            "FROM Maitre_de_jeu"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(row[0])
                row=cursor.fetchone()

        liste_j=[self.chercher_par_pseudo_mj(pseudo) for pseudo in l if pseudo is not None]

        return liste_j

    def liste_personnage(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        with self.__connection.cursor() as cursor :
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

    def maj_classe(self, personnage, nvlle_classe):
        """Changer la classe d'un personnage

        Parameters
        ----------
        personnage : Personnage
            Personnage dont il faut changer la classe
        nvlle_classe : str
            Nouvelle classe à attribuer
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("UPDATE personnage SET classe=%(nvlle_classe)s"
            "WHERE id_perso=%(id)s"
            ,{
                "nvlle_classe" : nvlle_classe,
                "id" : personnage.id
                })

    def test_pseudo_libre(self, pseudo):
        """Teste si un pseudo est déjà utilisé ou non

        Parameters
        ----------
        pseudo : str
            Pseudo à tester

        Returns
        -------
        bool
            True si le pseudo est libre, False s'il est déjà utilisé
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM mdp WHERE pseudo=%(pseudo)s;",
                           {
                               "pseudo":pseudo
                           })
            test = cursor.fetchone()['count']
        if test == 1:
            return False
        else:
            return True

    def verifier_mdp(self, pseudo, mdp_a_tester):
        """Vérifier qu'un mot de passe est bien le bon

        Parameters
        ----------
        pseudo : str
            Pseudo
        mdp_a_tester : str
            Mot de passe haché à tester

        Returns
        -------
        bool
            True si les mots de passe sont égaux, False sinon
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("SELECT mdp FROM mdp WHERE pseudo=%(pseudo)s;",
                           {
                               "pseudo":pseudo
                           })
            mdp_base = cursor.fetchone()['mdp']
        return mdp_base==mdp_a_tester

    def chercher_par_pseudo_org(self,pseudo_o):
        """Chercher un organisateur selon son pseudo

        Parameters
        ----------
        pseudo_o : str
            Pseudo de l'organisateur à chercher

        Returns
        -------
        Organisateur
            Organisateur si l'organisateur est trouvé, None sinon
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*)"
            " FROM organisateur "
            " WHERE pseudo_organisateur=%(pseudo)s"
            , {"pseudo": pseudo_o})
            res=cursor.fetchone()

        if res['count'] == 1:
            return Organisateur(pseudo_o)
        return None

    def chercher_messages_par_pseudo(self, pseudo:str):
        """Obtenir les messages destinés à un certain utilisateur

        Parameters
        ----------
        pseudo : str
            Pseudo de l'utilisateur

        Returns
        -------
        List[Dict]
            Liste de dictionnaires ayant deux clés ('date' et 'message')
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("SELECT *"
            " FROM journal "
            " WHERE pseudo=%(pseudo)s"
            , {"pseudo": pseudo})

        row=cursor.fetchone()
        messages = []

        while row is not None:
            messages.append({"date":row['date'], "message":row['msg']})
            row=cursor.fetchone()

        return messages

    def supprimer_partie(self,partie:Partie):
        """Suprimer une partie de la table de donnée
        Parameters
        ------------
        partie: Partie
            la partie à supprimer

        Returns
        -----------
        booléen
            True si la partie à bien été supprimée
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("DELETE FROM partie"
            "WHERE id=%(id)s RETURNING TRUE"
            , {"id": partie.id})
            sup_partie=cursor.fetchone()
        return sup_partie

    def supprimer_scenario(self,scenario:Scenario):
        """Suprimer un scenario de la table de donnée
        Parameters
        ------------
        scenario: Partie
            la partie à supprimer

        Returns
        -----------
        booléen
            True si le scenario à bien été supprimé
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("DELETE FROM scenario"
            "WHERE id=%(id)s RETURNING TRUE"
            , {"id": scenario.id})
            sup_scenario=cursor.fetchone()
        return sup_scenario

    def ajouter_joueur_partie(self,partie:Partie,perso:Personnage):
        """Rajoute à la base de données les joueurs inscrits dans la partie;
        Parameters
        ------------
        partie:Partie
            la partie qu'il faut mettre à jour dans la bdd

        Returns
        -----------
        booléen
            retourne True si la maj à bien été faite
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("INSERT INTO inscription_perso (id_partie , id_perso)"
            "VALUES (%(id_partie)s,%(id_perso)s) RETURNING TRUE;"
            ,{
                "id_partie" : partie.id,
                "id_perso" : perso.id,
                })
            inscription=cursor.fetchone()
        return inscription

