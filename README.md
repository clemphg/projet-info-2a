# Application de gestion de conférence de jeu de rôle

## Sommaire

1. [Contexte](#contexte)
2. [Fonctionnement général](#fonctionnement-general)
3. [Mise en place de l'application](#mep-application)
4. [Instructions d'utilisation](#instructions-utilisation)

## Contexte

Cette application à été réalisée en 2022 dans le cadre du projet d'informatique de deuxième année de l'ENSAI.

En amont de la tenue d'une convention de jeux de rôle, il faut organiser les parties qui s'y tiendront. Via cette application, des joueurs et des maîtres de jeu créent personnages et scénarios. Après qu'une partie ait été créée par un maître de jeu, les joueurs peuvent s'y inscrire avec un personnage si celui-ci est compatible.  Des organisateurs ont également accès à l'application et gèrent joueurs, maîtres de jeu, personnages, scénarios et parties.


## Fonctionnement général<a name="fonctionnement-general" />

L'application Python est divisée en cinq grandes parties :

- **Client** : appel à l'API D&D 5.
- **DAO (Data Access Object)** : lien entre le code en Python et la base de données.
- **Objets métier** : modélisation des utilisateurs, parties, personnages, ... de l'application.
- **Service** : fait le lien entre les vues et la DAO. Gère les interactions. Partie métier de l'application.
- **Vues** : modules d'affichage de l'application.

Elle compte des modules de tests regroupées dans le package **tests**. Ceux-ci permettent de vérifier si l'installation de l'application a été effectuée correctement.

L'utilisateur va interagir avec les vues, qui font appel aux services. Ces derniers appellent la DAO et créent, modifient ou suppriment des objets métiers selon les choix et inputs de l'utilisateur.

### Technologies utilisées

Cette application est codée en Python 3.9. Elle s'appuie sur une base de données relationnelle pour le stockage des données.

#### Base de données

Les données des utilisateurs sont gardées en mémoire grace à une base de données relationnelle.

#### API

Cette application utilise l'[API Dungeons and Dragons (5th edition)](https://www.dnd5eapi.co/). Lors de la création d'un personnage, le joueur doit choisir la classe et la race du personnage dans des listes obtenues via l'API.

## Mise en place de l'application<a name="mep-application" />
### Téléchargement de l'application

Cette application s'installe en local via ce dossier. Vous pouvez cloner ce projet dans le dossier de votre choix ou simplement le télécharger. Vous devez disposer d'une installaton de [Python](https://www.python.org/downloads/). Vous pouvez également télécharger un IDE tel que [Visual Studio Code](https://code.visualstudio.com/) afin de mettre en place et lancer l'application plus facilement.

La liste des dépendances se trouve dans le fichier **requirements.txt**. Ces packages sont nécessaires au fonctionnement de l'application et devront être téléchargés avant sa mise en fonctionnement. Vous pouvez les installer en entrant la commande suivante dans le terminal :

```
pip install -r requirements.txt
```

### Initialisation de la base de données

Vous devez disposer d'un accès à une base de données SQL qui servira au stockage des données des utilisateurs et parties. Vous pouvez par exemple installer une base [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) en local.

Une fois que vous disposez d'une base, vous devrez mettre à jour dans le fichier .env :

- HOST : l'host de la database
- DATABASE : le nom de la base de données
- USER : le nom d'utilisateur
- PASSWORD : le mot de passe

Ces informations permettront d'établir la connexion à votre base de données.

Vous devez maintenant initialiser la base de données en créant les tables nécessaires au stockage des données. Le script SQL de remplissage est nommé **init_base.sql**. Copier-coller son contenu dans l'outil de requête SQL de votre système de gestion de base de données (SGBD). Par exemple, le query tool sur PgAdmin.

### Test d'installation

Une fois que tout est mis en place, vous allez tester l'application. Vous disposez du fichier **base_test_remplissage.sql** qui propose un pré-remplissage de la base de données sur lequel s'appuient les tests unitaires. Rentrez le contenu de ce fichier dans l'outil de requête de votre SGBD. Vous devrez ensuite lancer les tests avec la commande suivante dans le terminal.

```
python -m unittest
```

### Définition des créneaux de parties et initialisation des comptes des organisateurs

#### Comptes des organisateurs
Si les joueurs et les maîtres de jeu pouvent s'inscrirent eux-mêmes, ce n'est pas le cas des organisateurs. Les comptes de ces derniers sont créés lors de la mise en place de l'application afin de resteindre l'accès aux fonctionnalités avancées.


#### Créneaux de parties

Les créneaux des parties sont définis grâce à l'outil de requête SQL de votre SGBD. En vous inspirant de la requête de remplissage de la table *creneaux* dans le fichier *base_test_remplissage.sql*, définissez vos créneaux selon les dates de votre convention.

Vous pouvez également modifier le nombre maximum de parties par créneau dans le fichier **service_maitre_de_jeu**.

Un fichier de configuration json (config.json) serait adapté pour définir rapidement les variables d'environnement tel que le nombre de parties ou les créneaux de parties.

## Instructions d'utilisation<a name="instructions-utilisation" />

Executer le main.py lance l'aplication. Le menu d'accueil de l'application s'affiche dans le terminal.

Toute la navigation dans l'application s'effectue via le clavier.

Pour sélectionner une option, utiliser les flèches haut et bas du clavier pour vous positionner dessus puis appuyer sur la touche Entrer.

Certains champs requièrent une entrée dactylographiée : tapez alors votre réponse au clavier. Si le texte rentré n'est pas conforme,
vous serez contraint de retaper une autre réponse jusqu'à ce que vous entriez une chaîne de caractères correcte. Par exemple, le mot de passe se doit de respecter une certaine longueur minimum avec des contraintes de caractères spéciaux. Tant que le mot de passe proposé ne sera pas conforme, vous en serez averti par un message et vous devrez en entrer un autre.

