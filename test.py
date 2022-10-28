import os

import dotenv
import psycopg2

from psycopg2.extras import RealDictCursor


connection=psycopg2.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor)
connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT id_creneau, inscription_perso.id_partie, scenario.nom AS nom_scenario, maitre_de_jeu.pseudo_mj, personnage.nom AS nom_perso"
        " FROM personnage"
        " JOIN inscription_perso ON personnage.id_perso=inscription_perso.id_perso"
        " JOIN partie ON partie.id_partie=inscription_perso.id_partie"
        " JOIN scenario ON partie.id_scenario=scenario.id_scenario"
        " JOIN maitre_de_jeu ON scenario.pseudo_mj=maitre_de_jeu.pseudo_mj"
        " WHERE pseudo_j=%(pseudo)s"
        " ORDER BY id_creneau ASC;"
        ,{
            "pseudo" : 'Aimee20'
        })

    row=cursor.fetchone()
    print(row)
    inscriptions = []

    while row is not None:
        inscriptions.append({
                "id_creneau": row['id_creneau'],
                "id_partie": row['id_partie'],
                "scenario": row['nom_scenario'],
                "pseudo_mj": row['pseudo_mj'],
                "nom_perso": row['nom_perso']
            })
        row=cursor.fetchone()
print(inscriptions)