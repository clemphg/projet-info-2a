import os

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor


dotenv.load_dotenv(override=True)

connection=psycopg2.connect(
    host=os.environ["HOST"],
    port=os.environ["PORT"],
    database=os.environ["DATABASE"],
    user=os.environ["USER"],
    password=os.environ["PASSWORD"],
    cursor_factory=RealDictCursor)

def test_pseudo_libre(pseudo):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM mdp WHERE pseudo=%(pseudo)s;",
                    {
                        "pseudo":pseudo
                    })
        test = cursor.fetchone()['count']
    if test == 1:
        return False
    else:
        return True

with connection.cursor() as cursor :
    cursor.execute("INSERT INTO joueur (pseudo_j , age) VALUES (%(pseudo)s,%(age)s);"
            ,{
                "pseudo" : "clem",
                "age" : 17,
            })

print(test_pseudo_libre("clementine"))