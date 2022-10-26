CREATE TABLE Creneaux (
    id_creneau INT PRIMARY KEY NOT NULL ,
    Date_debut DATE,
    Date_fin DATE
);


CREATE TABLE Maitre_de_jeu(
    pseudo_mj VARCHAR(25) PRIMARY KEY,
    age INT
);

CREATE TABLE scenario(
    id_scenario INT PRIMARY KET NOT NULL ,
    nom VARCHAR(40),
    descrip TEXT,
    niveau INT,
    pseudo_mj VARCHAR(25) REFERENCES Maitre_de_jeu(pseudo_mj)
);

CREATE TABLE partie(
    id_partie INT PRIMARY KEY NOT NULL ,
    id_scenatio INT REFERENCES scenario(id_scenario),
    id_creneau INT REFERENCES Creneaux(id_creneau)
);

CREATE TABLE joueur(
    pseudo_j VARCHAR(25) PRIMARY KEY,
    age INT
);

CREATE TABLE personnage(
    id_perso INT PRIMARY KEY NOT NULL ,
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
    pseudo_organisateur VARCHAR(25) PRIMARY KEY,
);

CREATE TABLE journal(
    id_message INT PRIMARY KEY ,
    pseudo VARCHAR(25),
    date DATE,
    msg TEXT
);
CREATE TABLE mdp(
    pseudo VARCHAR(25) PRIMARY KEY,
    mdp TEXT
);