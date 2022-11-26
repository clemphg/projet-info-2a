
--CREATE SCHEMA D_and_D;

DROP TABLE inscription_perso CASCADE;
DROP TABLE partie CASCADE;
DROP TABLE creneaux CASCADE;
DROP TABLE personnage CASCADE;
DROP TABLE scenario CASCADE;
DROP TABLE joueur CASCADE;
DROP TABLE maitre_de_jeu CASCADE;
DROP TABLE organisateur CASCADE;
DROP TABLE mdp;
DROP TABLE journal;

DROP SEQUENCE partie_seq, personnage_seq, journal_seq, scenario_seq;


CREATE SEQUENCE partie_seq;
CREATE SEQUENCE personnage_seq;
CREATE SEQUENCE journal_seq;
CREATE SEQUENCE scenario_seq;

CREATE TABLE Creneaux (
    id_creneau INT PRIMARY KEY NOT NULL,
    date_debut TIMESTAMP,
    date_fin TIMESTAMP
);

CREATE TABLE joueur(
    pseudo_j VARCHAR(25) PRIMARY KEY,
    age INT
);

CREATE TABLE Maitre_de_jeu(
    pseudo_mj VARCHAR(25) PRIMARY KEY,
    age INT
);

CREATE TABLE scenario(
    id_scenario INT PRIMARY KEY NOT NULL
    DEFAULT nextval ('scenario_seq'),
    nom VARCHAR(40),
    descrip TEXT,
    niveau INT,
    pseudo_mj VARCHAR(25) REFERENCES Maitre_de_jeu(pseudo_mj)
);

CREATE TABLE partie(
    id_partie INT PRIMARY KEY NOT NULL
    DEFAULT nextval('partie_seq'),
    id_scenario INT REFERENCES scenario(id_scenario),
    id_creneau INT REFERENCES Creneaux(id_creneau)
);

CREATE TABLE personnage(
    id_perso INT PRIMARY KEY NOT NULL
    DEFAULT nextval ('personnage_seq'),
    nom VARCHAR(20),
    age INT,
    niveau INT,
    race VARCHAR(15),
    classe VARCHAR(15),
    pseudo_j VARCHAR(25) REFERENCES joueur(pseudo_j)
);

CREATE TABLE inscription_perso(
    id_partie INT REFERENCES partie(id_partie) ,
    id_perso INT REFERENCES personnage(id_perso),
    PRIMARY KEY(id_partie,id_perso)
);

CREATE TABLE organisateur(
    pseudo_organisateur VARCHAR(25) PRIMARY KEY
);

CREATE TABLE journal(
    id_message INT PRIMARY KEY
    DEFAULT nextval ('journal_seq'),
    pseudo VARCHAR(25),
    date TIMESTAMP,
    msg TEXT
);

CREATE TABLE mdp(
    pseudo VARCHAR(25) PRIMARY KEY,
    mdp TEXT
);
