import os
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


    def creer_perso(self,perso: Personnage):
        """Ajouter un personnage en base de données

        Parameters
        ----------
        perso : Personnage
            Personnage à ajouter dans la base

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
                "pseudo_j" : perso.pseudo_j
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

    def creer_scenario(self,scenario: Scenario):
        """Ajouter un scenario en base

        Parameters
        ----------
        scenario : Scenario
            Scénario à ajouter en base

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
                "descrip" : scenario.description,
                "niveau" : scenario.niveau_min,
                "pseudo_mj" : scenario.pseudo_mj
                })
            scenario.id = cursor.fetchone()['id_scenario']
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
            partie.id = cursor.fetchone()['id_partie']
        return partie.id

    def creer_org(self, org: Organisateur, mot_de_passe):
        """Ajouter un organisateur en base

        Parameters
        ----------
        org : Organisateur
            Organisateur à ajouter dans la base
        mot_de_passe : str
            Mot de passe haché de l'organisateur

        Returns
        -------
        bool
            True si l'organisateur a bien été ajouté, false sinon
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("INSERT INTO organisateur (pseudo_organisateur)"
            "VALUES (%(pseudo)s);"
            ,{
                "pseudo" : org.pseudo
                })

            cursor.execute("INSERT INTO mdp (pseudo, mdp)"
            "VALUES (%(pseudo)s,%(mdp)s);"
            ,{
                "pseudo" : org.pseudo,
                "mdp" : mot_de_passe,
                })

            # on vérifie que le mj a bien été ajouté
            cursor.execute("SELECT COUNT(*) FROM organisateur WHERE pseudo_organisateur = %(pseudo)s;"
            ,{
                "pseudo" : org.pseudo,
                })
            test1 = cursor.fetchone()['count']
            cursor.execute("SELECT COUNT(*) FROM mdp WHERE pseudo = %(pseudo)s;"
            ,{
                "pseudo" : org.pseudo,
                })
            test2 = cursor.fetchone()['count']
        if test1==1 and test2==1:
            return True
        else:
            return False

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
            " WHERE pseudo_j=%(pseudo)s;"
            , {"pseudo": pseudo_j})
            age=cursor.fetchone()

            if age is not None :
                cursor.execute("SELECT id_perso, nom, age ,niveau , race, classe, pseudo_j "
                "FROM personnage "
                "WHERE pseudo_j=%(pseudo)s;"
                , {"pseudo": pseudo_j})
                row=cursor.fetchone()
                l=[]
                while row is not None:
                    l.append(Personnage(row['id_perso'],row['nom'],row['age'],row['race'],row['niveau'],row['classe'], row['pseudo_j']))
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
            " WHERE pseudo_mj=%(pseudo)s;"
            , {"pseudo": pseudo_mj})
            age=cursor.fetchone()

            if age is not None :
                cursor.execute("SELECT id_scenario, nom , descrip, niveau, pseudo_mj"
                " FROM scenario"
                " WHERE pseudo_mj=%(pseudo)s;"
                ,{"pseudo": pseudo_mj})
                row=cursor.fetchone()
                l=[]
                while row is not None:
                    l.append(Scenario(row['id_scenario'],row['nom'],row['descrip'],row['niveau'], row['pseudo_mj']))
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
            cursor.execute("SELECT id_perso, nom, age ,niveau, race, classe, pseudo_j"
            " FROM personnage"
            " WHERE id_perso=%(id_perso)s;"
            , {"id_perso": id_perso})
            res=cursor.fetchone()
        if res is not None :
            perso=Personnage(id_perso, res['nom'],res['age'],res['race'],res['niveau'],res['classe'],res['pseudo_j'])
            return perso
        else :
            return None


    def inscription_personnage(self, id_perso, id_partie):
        """Inscrire un personnage à une partie

        Parameters
        ----------
        id_perso : int
            ID du Personnage à inscrire
        id_partie : int
            id de la partie à laquelle inscrire le personnage

        Returns
        -------
        boolean
            True si l'opération a bien été réalisée
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("INSERT INTO inscription_perso (id_perso,id_partie)"
            " VALUES (%(id_perso)s, %(id_partie)s)"
            " RETURNING TRUE AS status;"
            ,{
                "id_perso" : id_perso,
                "id_partie" : id_partie,
                 })
            status = cursor.fetchone()
        if status:
            return status
        else:
            return False


    def liste_joueurs(self):
        """Liste des joueurs

        Returns
        -------
        List[Joueur]
            Liste de tous les joueurs
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("SELECT pseudo_j"
            " FROM joueur;"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(row['pseudo_j'])
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
            " WHERE pseudo_j=%(pseudo)s RETURNING TRUE;"
            , {"pseudo": pseudo})
            sup_joueur=cursor.fetchone()
            cursor.execute("DELETE FROM mdp"
            " WHERE pseudo=%(pseudo)s RETURNING TRUE;"
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
            " WHERE pseudo_mj=%(pseudo)s RETURNING TRUE;"
            , {"pseudo": pseudo})
            sup_mj=cursor.fetchone()
            cursor.execute("DELETE FROM mdp"
            " WHERE pseudo=%(pseudo)s RETURNING TRUE;"
            , {"pseudo": pseudo})
            sup_mdp=cursor.fetchone()
        return sup_mj and sup_mdp

    def liste_mjs(self):
        """Liste des maitres de jeu

        Returns
        -------
        List[MaitreDeJeu]
            Liste des maitres de jeu
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("SELECT pseudo_mj"
            " FROM Maitre_de_jeu;"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(row['pseudo_mj'])
                row=cursor.fetchone()

        liste_j=[self.chercher_par_pseudo_mj(pseudo) for pseudo in l if pseudo is not None]

        return liste_j

    def liste_personnages(self):
        """Liste des personnages

        Returns
        -------
        List[Personnage]
            Liste des personnages
        """
        with self.__connection.cursor() as cursor :
            cursor.execute("SELECT id_perso"
            " FROM personnage;"
            )
            row=cursor.fetchone()
            l=[]
            while row is not None:
                l.append(row['id_perso'])
                row=cursor.fetchone()

        l_perso=[self.chercher_par_id_perso(id) for id in l]
        return l_perso

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
            " WHERE id_perso=%(id)s"
            " RETURNING TRUE as status;"
            ,{
                "nvlle_classe" : nvlle_classe,
                "id" : personnage.id
                })
            res=cursor.fetchone()
        if res:
            return True
        else:
            return False

    def verifier_pseudo_libre(self, pseudo):
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
            " WHERE pseudo_organisateur=%(pseudo)s;"
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
            Liste de dictionnaires ayant deux clés ('date' et 'message'), None si pas de message pour l'utilisateur
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("SELECT *"
            " FROM journal "
            " WHERE pseudo=%(pseudo)s"
            " ORDER BY date ASC;"
            , {"pseudo": pseudo})

            row=cursor.fetchone()
            messages = []

            while row is not None:
                messages.append({"date":row['date'], "message":row['msg']})
                row=cursor.fetchone()

        if len(messages)>0:
            return messages
        else:
            return None

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

            # suppression des inscriptions à la partie
            cursor.execute(
                "DELETE FROM inscription_perso"
                " WHERE id_partie=%(id)s"
                " RETURNING TRUE AS status;"
            , {"id": partie.id})
            sup_inscription=cursor.fetchone()

            # suppression de la partie dans la table des parties
            cursor.execute(
                "DELETE FROM partie"
                " WHERE id_partie=%(id)s"
                " RETURNING TRUE AS status;"
            , {"id": partie.id})
            sup_partie=cursor.fetchone()

        if sup_partie and sup_inscription:
            return True
        else:
            return False

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
            " WHERE id_scenario=%(id)s RETURNING TRUE;"
            , {"id": scenario.id})
            sup_scenario=cursor.fetchone()
        return sup_scenario

    def supprimer_personnage(self,perso:Personnage):
        """Suprimer un personnage de la table de données

        Parameters
        ------------
        perso: Personnage
            Le personnage à supprimer

        Returns
        -----------
        booléen
            True si le personnage à bien été supprimé
        """
        with self.__connection.cursor() as cursor:
            cursor.execute("DELETE FROM personnage"
            " WHERE id_perso=%(id)s RETURNING TRUE;"
            , {"id": perso.id})
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
        if inscription:
            return True
        else:
            return False

    def liste_inscriptions_joueur(self, pseudo):
        """Liste des inscriptions d'un joueur

        Parameters
        ----------
        pseudo : str
            Pseudo du joueur en question

        Returns
        -------
        List[Dict]
            Chaque élément de la liste est un dictionnaire décrivant l'inscription (id_creneau, id_partie, id_scenario, nom_scenario, niv_min_scenario, pseudo_mj, id_perso, nom_perso, niv_perso).
            Retourne None si pas d'inscriptions.
        """
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT id_creneau, inscription_perso.id_partie, scenario.id_scenario, scenario.nom AS nom_scenario, scenario.niveau AS niv_min_scenario,"
                " maitre_de_jeu.pseudo_mj, personnage.id_perso, personnage.nom AS nom_perso, personnage.niveau AS niv_perso"
                " FROM personnage"
                " JOIN inscription_perso ON personnage.id_perso=inscription_perso.id_perso"
                " JOIN partie ON partie.id_partie=inscription_perso.id_partie"
                " JOIN scenario ON partie.id_scenario=scenario.id_scenario"
                " JOIN maitre_de_jeu ON scenario.pseudo_mj=maitre_de_jeu.pseudo_mj"
                " WHERE pseudo_j=%(pseudo)s"
                " ORDER BY id_creneau ASC;"
            ,{
                "pseudo" : pseudo
                })
            row=cursor.fetchone()
            inscriptions = []
            while row is not None:
                inscriptions.append({
                    "id_creneau": row['id_creneau'],
                    "id_partie": row['id_partie'],
                    "id_scenario": row['id_scenario'],
                    "pseudo_mj": row['pseudo_mj'],
                    "nom_scenario": row['nom_scenario'],
                    "niv_min_scenario": row['niv_min_scenario'],
                    "id_perso": row["id_perso"],
                    "nom_perso": row['nom_perso'],
                    "niv_perso": row['niv_perso']
                })
                row=cursor.fetchone()
        if len(inscriptions)>0:
            return inscriptions
        else:
            return None

    def liste_inscriptions_mj(self, pseudo):
        """Liste des inscriptions d'un mj

        Parameters
        ----------
        pseudo : str
            Pseudo du mj en question

        Returns
        -------
        List[Dict]
            Chaque élément de la liste est un dictionnaire décrivant l'inscription (id_creneau, id_partie, nom_scenario, niv_min_scenario).
            Retourne None si pas d'inscriptions.
        """
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT id_creneau, partie.id_partie, scenario.id_scenario, scenario.nom AS nom_scenario, scenario.niveau AS niv_min_scenario"
                " FROM scenario"
                " JOIN partie ON partie.id_scenario=scenario.id_scenario"
                " WHERE pseudo_mj=%(pseudo)s"
                " ORDER BY id_creneau ASC;"
            ,{
                "pseudo" : pseudo
                })
            row=cursor.fetchone()
            inscriptions = []
            while row is not None:
                inscriptions.append({
                    "id_creneau": row['id_creneau'],
                    "id_partie": row['id_partie'],
                    "id_scenario": row['id_scenario'],
                    "nom_scenario": row['nom_scenario'],
                    "niv_min_scenario": row['niv_min_scenario']
                })
                row=cursor.fetchone()
        if len(inscriptions)>0:
            return inscriptions
        else:
            return None

    def chercher_partie_par_id(self, id_partie:int):
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT partie.id_partie, partie.id_creneau, scenario.id_scenario, scenario.pseudo_mj, scenario.nom AS nom_scenario,"
                " scenario.descrip AS des_scenario, scenario.niveau AS niv_min_scenario"
                " FROM partie"
                " JOIN scenario ON partie.id_scenario = scenario.id_scenario"
                " WHERE partie.id_partie = %(id_partie)s;"
            ,{
                "id_partie" : id_partie
                })
            row=cursor.fetchone()
            partie = None
            if row:
                id=row['id_partie']
                creneau=row['id_creneau']
                scenario=Scenario(id=row['id_scenario'],
                                  nom=row['nom_scenario'],
                                  description=row['des_scenario'],
                                  niveau_min=row['niv_min_scenario'],
                                  pseudo_mj=row['pseudo_mj'])
                persos = self.chercher_persos_par_partie(id)
                partie = Partie(id=id,
                                creneau=creneau,
                                scenario=scenario,
                                liste_persos=persos)
        return partie

    def desinscription_personnage(self, id_perso, id_partie):
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM inscription_perso"
                " WHERE id_perso = %(id_perso)s AND id_partie = %(id_partie)s"
                " RETURNING TRUE AS status;",
                {
                    "id_perso": id_perso,
                    "id_partie": id_partie
                }
            )
            status = cursor.fetchone()
        if status:
            return status
        else:
            return False

    def liste_creneaux(self):
        """Liste des creneaux
        """
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT id_creneau"
                " FROM creneaux;"
            )
            l_creneaux = []
            res = cursor.fetchone()
            if res:
                while res is not None:
                    l_creneaux.append(res['id_creneau'])
                    res = cursor.fetchone()
        return l_creneaux

    def liste_creneaux_dispos_joueur(self, joueur):
        """Liste des creneaux

        Returns
        -------
        List[int]
            Liste des créneaux
        """
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT id_creneau"
                " FROM creneaux"
                " EXCEPT"
                " SELECT creneaux.id_creneau"
                " FROM creneaux"
                " JOIN partie ON partie.id_creneau=creneaux.id_creneau"
                " JOIN inscription_perso ON partie.id_partie=inscription_perso.id_partie"
                " JOIN personnage ON inscription_perso.id_perso=personnage.id_perso"
                " WHERE pseudo_j=%(pseudo)s"
                " ORDER BY id_creneau ASC",
                {
                    "pseudo": joueur.pseudo
                }
            )
            l_creneaux = []
            res = cursor.fetchone()
            if res:
                while res is not None:
                    l_creneaux.append(res['id_creneau'])
                    res = cursor.fetchone()
        return l_creneaux

    def chercher_persos_par_partie(self, id_partie):
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT personnage.id_perso, nom, age, race, niveau, classe, pseudo_j"
                " FROM inscription_perso"
                " JOIN personnage ON inscription_perso.id_perso=personnage.id_perso"
                " WHERE id_partie=%(id_partie)s;",
                {
                    "id_partie": id_partie
                }
            )
            l_persos = []
            res = cursor.fetchone()
            if res:
                while res is not None:
                    l_persos.append(Personnage(id = res['id_perso'],
                                               nom = res['nom'],
                                               age = res['age'],
                                               race = res['race'],
                                               niveau = res['niveau'],
                                               classe = res['classe'],
                                               pseudo_j = res['pseudo_j']))
                    res = cursor.fetchone()
            return l_persos


    def chercher_parties_par_creneau(self, id_creneau):
        """Chercher les parties se déroulant sur un créneau donné

        Parameters
        ----------
        id_creneau : int
            ID du créneau

        Returns
        -------
        list
            liste des parties
        """
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT partie.id_partie, scenario.id_scenario, nom, descrip, niveau, pseudo_mj"
                " FROM partie"
                " JOIN scenario ON partie.id_scenario=scenario.id_scenario"
                " WHERE id_creneau=%(creneau)s;",
                {
                    "creneau": id_creneau
                }
            )
            res = cursor.fetchone()
            parties = []
            if res:
                while res is not None:
                    l_persos = self.chercher_persos_par_partie(res['id_partie'])
                    partie = Partie(id=res['id_partie'],
                                    creneau=id_creneau,
                                    scenario = Scenario(id=res['id_scenario'],
                                                        nom=res['nom'],
                                                        description=res['descrip'],
                                                        niveau_min=res['niveau'],
                                                        pseudo_mj=res['pseudo_mj']),
                                    liste_persos=l_persos)
                    parties.append(partie)
                    res = cursor.fetchone()
            return parties

    def ajouter_message(self, pseudo, date, msg):
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO journal (pseudo , date, msg)"
                " VALUES (%(pseudo)s,%(date)s,%(msg)s)"
                " RETURNING TRUE AS status;",
                {
                    "pseudo": pseudo,
                    "date": date,
                    "msg": msg
                }
            )
            status = cursor.fetchone()['status']
        if status:
            return status
        else:
            return False



    def liste_creneaux_dispos_mj(self, mj):
        """Liste des creneaux

        Returns
        -------
        List[int]
            Liste des créneaux
        """
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT id_creneau"
                " FROM creneaux"
                " EXCEPT"
                " SELECT creneaux.id_creneau"
                " FROM creneaux"
                " JOIN partie ON partie.id_creneau=creneaux.id_creneau"
                " JOIN scenario ON scenario.id_scenario=partie.id_scenario"
                " WHERE pseudo_mj=%(pseudo)s"
                " ORDER BY id_creneau ASC;",
                {
                    "pseudo": mj.pseudo
                }
            )
            l_creneaux = []
            res = cursor.fetchone()
            if res:
                while res is not None:
                    l_creneaux.append(res['id_creneau'])
                    res = cursor.fetchone()
        return l_creneaux

    def liste_perso_possibles(self, partie:Partie):
        """Liste des personnages possibles

        Liste des personnages pouvant être inscrits à une partie.
        Cherche les personnages des joueurs disponibles sur le créneau et garde ceux de niveau suffisant.

        Returns
        -------
        List[Personnage]
            Liste des personnages
        """
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "SELECT id_perso"
                " FROM personnage"
                " WHERE pseudo_j IN"
                " (SELECT DISTINCT pseudo_j"
                " FROM personnage"
                " EXCEPT"
                " SELECT pseudo_j"
                " FROM inscription_perso"
                " JOIN personnage ON personnage.id_perso=inscription_perso.id_perso"
                " WHERE id_partie=%(id_partie)s) AND niveau>=%(niv_min)s;",
                {
                    "id_partie": partie.id,
                    "niv_min": partie.scenario.niveau_min
                }
            )
            persos = []
            res = cursor.fetchone()
            if res:
                while res is not None:
                    perso = self.chercher_par_id_perso(res['id_perso'])
                    persos.append(perso)
                    res = cursor.fetchone()
        return persos

