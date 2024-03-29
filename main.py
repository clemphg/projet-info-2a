"""Main

Point d'entrée de l'application. Fichier à executer pour accéder à l'app.
"""

from vues.vue_accueil import VueAccueil

# Point d'entrée de l'application

if __name__ == '__main__':
    # lancer la vue d'accueil
    current_view = VueAccueil()

    # Tant que la vue actuelle n'est pas nulle, on continue à l'afficher
    while current_view:
        # séparateur entre les vues
        with open('graphiques/separateur.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
        # infos de la vue
        current_view.display_info()

        # demander à l'utilisateur de faire un choix
        current_view = current_view.make_choice()

    # s affiche lorsqu'on quitte l'application
    with open('graphiques/a_bientot.txt', 'r', encoding="utf-8") as asset:
        print(asset.read())
