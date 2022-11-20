# Conférence de jeu de rôle

## Sommaire

1. [Contexte](#contexte)
2. [Fonctionnement général](#fonctionnement-general)
3. [Mise en place de l'application](#mep-application)
4. [Instructions d'utilisation](#instruction-utilisation)

## Contexte

Cette application à été réalisée en 2022 dans le cadre du projet d'informatique de deuxième année de l'ENSAI.

En amont de la tenue d'une convention de jeux de rôle, il faut organiser les parties qui s'y tiendront. Via cette application, des joueurs et des maîtres de jeu peuvent créer personnages et scénarios. Après qu'une partie ait été créée par un maître de jeu, les joueurs peuvent s'y inscrire avec un personnage si celui-ci est compatible.  Des organisateurs ont également accès à l'application et peuvent gérer joueurs, maîtres de jeu, personnages, scénarios et parties.


## Fonctionnement général



### Technologies utilisées

Cette application est codée en Python .

architecture générale
technologies utilisées (bdd, python, ...)

#### Base de données

Les données des utilisateurs sont gardées en mémoire grace à une base de données relationnelle.

#### API

Cette application utilise l'[API Dungeons and Dragons (5th edition)](https://www.dnd5eapi.co/). Lors de la création d'un personnage, le joueur doit choisir la classe et la race du personnage dans des listes obtenues via l'API.

## Mise en place de l'application

### Téléchargement de l'application

Cette application s'installe en local via ce dossier

### Initialisation de la base de données

Vous devez disposer d'un accès à une base de données SQL. Vous pouvez par exemple installer une base [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) en local.

Une fois que vous disposez d'une base, vous devrez mettre à jour dans le fichier .env :

- HOST : l'host de la database
- DATABASE : le nom de la base de données
- USER : le nom d'utilisateur
- PASSWORD : le mot de passe

Ces informations permettront d'établir la connexion à votre base de données.



éventuellement ajouter fichier config json pour les variables globales

## Instructions d'utilisation

Afin de lancer l'application, il faut executer le main.py. Le menu d'accueil de l'application s'affiche.

Toute la navigation dans l'application s'effectue via le clavier

pour naviguer entre les options, utiliser les flèches haut et bas du clavier.
pour sélectionner une option, se positionner dessus et touche entrer

certains champs requièrent une entrée dactylographiée : taper votre réponse au clavier. Si le texte rentré n'est pas conforme,
vous serez contraint de retaper une autre réponse jusqu'à ce que vous entriez un text correct (par exemple pour le mot de passe qui doit vérifier certaines caractéristiques)

