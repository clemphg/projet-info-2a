# Roleplay convention management app

## Table of contents

1. [Context](#context)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Commands](#commands)

## Context<a name="context" />

This app was made in 2022 as as a part of ENSAI's second year computer science project.

Prior to a roleplay convention, the games that will be held there have to be planned. Gamemasters and players need to have a way to enroll and create games with scripts and characters.
This app aims to provide such a tool to roleplay amateurs.

Three types of users can have an accoutn on the app : players, gamemasters and organisers. The first two have to register and create an account before accessing the app.
Gamemasters are able to create scripts and players characters. Gamemasters can plan a game with a specific script and players are then able to enroll in that game with a character of a high enough level. Organisers have a pre-made account and have options to manage players, gamemasters, scripts characters as well as games.


## Architecture<a name="architecture" />

This Python app has five major parts :

- **Client** : calls D&D 5 API.
- **DAO (Data Access Object)** : link between Python code and database.
- **Objets métier** : modelisation of users, games, characters, ... of the app.
- **Service** : link between views, DAO, client, objets métiers. Handles interactions, applies the inputs and choices of the user onto objects and data.
- **Vues** : display modules of the app.

It also has a **tests** package. Those allow for the installer to test if the app was correctly installed or not.

The user will be presented views and will be able to choose inputs through them. Views are then calling services which call the DAO and create, update or delete business objects according to user inputs.

### Technologies used

This app is coded using **Python 3.9**. It uses a SQL relational database to store user data, information about games,...

#### API

This app uses the [API Dungeons and Dragons (5th edition)](https://www.dnd5eapi.co/). When creating a character, the player has to choose its class and race within a list obtained with the API. This allows for characters to only have valid races and classes.

## Installation<a name="installation" />
### Downloading the app

This app can be installed locally. You can fork this project and then clone it in your choosen directory. You can also simply download it.

An installation of [Python](https://www.python.org/downloads/) is needed. You can also download an IDE such as [Visual Studio Code](https://code.visualstudio.com/) in order to set up and launch the app more easily.

Packages requirements are listed in the **requirements.txt** file. These packages are necessary in order for the app to work. They will have to be downloaded before any launching attempt. You can install them all in one go using the following terminal command :

```
pip install -r requirements.txt
```

### Initialising the database

You must have an SQL relational database wich will be used to store user data, games,... For instance, you can install a [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) database locally.

Once you have a database, you have to update the following information in the **.env** file at the root of the project :

- HOST : databse host,
- DATABASE : database name,
- USER : username,
- PASSWORD : password.

This information will allow to establish the connection from the Python code to your database.

You now have to initialise the database by creating the necessary tables for data to be stored the proper way. The SQL filling script is named **init_db.sql** and is located at the root of the project. Copy-paste its content in the SQL query tool of you database management system (DBMS). In pgAdmin, this tool in located in Tools>Query tool

### Installation test

Once everything has been installed, you need to test the installation. Within the file **db_test_remplissage.sql** at the root of the project there are some SQL insert queries which will allow you to fill your database in order to test the app's installation. Please enter the file's content in your DBMS query tool and launch the tests with the following command (in the terminal) :

```
python -m unittest
```
Please be aware that you will have to re-initialise completely your database if you wish to test it several times. As inserts and deletes are tested, the information in the data base changes and will make your following test fail if you do not reinitialise it.


### Games time slots and organiser's accounts setup

#### Organisers's accounts

If players and gamemasters can create an account by themselves, organisers's accounts must be created prior to launching the app.

You have to use the designated script to enter their pseudonyms and passwords into the database. Please keep passwords into a password safe of some sort (such as KeePass, Bitwarden or Dashlane) as it will not be possible to recover a lost password.

#### Games time slots

Game time slots are defined using your DBMS's SQL query tool. You can take the insert query for the **creneaux table** into **db_test_remplissage.sql** as an example.

You can also update the maximum number of games for each time slot in the file **service/service_maitre_de_jeu**.

A configuration file (config.json) would be adapted to define quickly the environment variables, such as the maximum number of games per time slot or time slots themselves.
## Commands<a name="commands" />

Run the **main.py** file to launch the app. The home menu is displayed in the terminal.

Inputs, whether they are choices or text input, will be made using the keyboard.

To select an option, use the up and down arrows. Position youself on the desired choice and enter.

Some fields require a textual input, type in your answer. If it is not valid, an error message will appear and invite you to enter another answer. For instance, the password has a minimum length, and requires some caracters of certain types.

