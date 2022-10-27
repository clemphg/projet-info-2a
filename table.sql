DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

/* Création de la table des créneaux */
CREATE TABLE Creneaux (
    id_creneau INT PRIMARY KEY NOT NULL ,
    Date_debut DATE,
    Date_fin DATE
);

/* Création de la table maître du jeu */
CREATE TABLE Maitre_de_jeu(
    pseudo_mj VARCHAR(25) PRIMARY KEY,
    motdepasse_mj TEXT,
    age INT
);

/* Création de la table scénario */

CREATE TABLE scenario(
    id_scenario INT PRIMARY KEY NOT NULL ,
    nom VARCHAR(40),
    descrip TEXT,
    niveau INT,
    pseudo_mj VARCHAR(25) REFERENCES Maitre_de_jeu(pseudo_mj)
);

/* Création de la table partie */
CREATE TABLE partie(
    id_partie INT PRIMARY KEY NOT NULL ,
    id_scenario INT REFERENCES scenario(id_scenario),
    id_creneau INT REFERENCES Creneaux(id_creneau)
);

/* Création de la table joueur */
CREATE TABLE joueur(
    pseudo_j VARCHAR(25) PRIMARY KEY,
    motdepasse_j TEXT,
    age INT
);

/* Création de la table personnage */
CREATE TABLE personnage(
    id_perso INT PRIMARY KEY NOT NULL ,
    nom VARCHAR(20),
    age INT,
    niveau INT,
    race VARCHAR(15),
    classe VARCHAR(15),
    pseudo_j VARCHAR(25) REFERENCES joueur(pseudo_j)
);

/* Création de la table inscription personnage à une partie */

CREATE TABLE inscription_perso(
    id_partie INT REFERENCES partie(id_partie) ,
    id_perso INT REFERENCES personnage(id_perso),
    PRIMARY KEY(id_partie,id_perso)
);

/* Création table organisateur */
CREATE TABLE organisateur(
    pseudo_organisateur VARCHAR(25) PRIMARY KEY
);

/* Création table journal: inventaire des messages envoyés aux utilisateurs*/
CREATE TABLE journal(
    id_message INT PRIMARY KEY ,
    pseudo VARCHAR(25),
    date DATE,
    msg TEXT
);

/* Création table mdp: pseudos et mots de passe des utilisateurs*/
CREATE TABLE mdp(
    pseudo VARCHAR(25) PRIMARY KEY ,
    mdp TEXT
);

INSERT INTO joueur (pseudo_j, motdepasse_j, age)
 VALUES
 ('Rébecca70', 'Armandblabla34', 24),
 ('Aimée20', 'Hebertblublu20', 36),
 ('Marielle90', 'Ribeiro38', 27),
 ('Hilaire100', 'Savary86', 58);

INSERT INTO maitre_de_jeu (pseudo_mj, motdepasse_mj, age)
 VALUES
 ('GiGi', 'Armand38', 25),
 ('Amy10', 'Heb2000', 22),
 ('Marie18', 'Rib380', 28),
 ('Hil100', 'Sava86', 60);

INSERT INTO organisateur (pseudo_organisateur, motdepasse_organisateur)
 VALUES
 ('Amima20', 'Arm380'),
 ('Amira100', 'Hello2001'),
 ('Maria180', 'Riban388'),
 ('Hihi100', 'Savane863');

INSERT INTO personnage (id_perso, nom, age, niveau, race, classe, pseudo_j)
 VALUES
 (1,'Elyanna', 200, 200,'elf', 'enchantresse','Rébecca70'),
 (2, 'Emir', 18, 200, 'humain','épéiste','Rébecca70'),
 (3, 'Elliot', 500, 200, 'démon','épéiste','Rébecca70'),
 (4,'Blondinet', 200, 50, 'nain', 'enchanteur','Aimée20'),
 (5,'Erys', 30, 100, 'humain','roi','Aimée20'),
 (6, 'Lucifer', 800, 300, 'démon','enchanteur','Aimée20'),
 (7,'Elodie', 200, 20,'elf', 'enchantresse','Marielle90'),
 (8, 'Aymen', 180, 200, 'dragon','combattant','Marielle90'),
 (9, 'Amor', 20, 200, 'humain','enchantresse','Marielle90'),
 (10,'Isabella', 200, 20,'elf','enchantresse','Hilaire100'),
 (11, 'Arthur', 18, 200, 'humain','prince','Hilaire100'),
 (12, 'Orifice', 500, 200, 'démon', 'forgeron', 'Hilaire100');

INSERT INTO scenario (id_scenario, nom, descrip, niveau, pseudo_mj)
 VALUES
 (1,'Désert de cadavres','Le jeu se déroulera dans un désert infesté de scorpions mortels', 200,'GiGi'),
 (2, 'Volcan enflammé',' Le jeu se déroulera dans un volcan en éruption', 200,'GiGi'),
 (3, 'Mer enchantée','Le jeu se déroulera dans une mer infestée de sirènes croqueuses d hommes', 200,'Amy10'),
 (4,'Montagne à dents de scie', 'Le jeu se déroulera dans une montagne infestée d ours mutants', 50,'Amy10'),
 (5,'Bataille navale', 'Le jeu se déroulera sous l eau',100,'Marie18'),
 (6, 'Bataille dans le ciel', 'Le jeu se déroulera dans le ciel mais attention aux licornes armées',50,'Marie18'),
 (7,'Sable bouillant', 'Le but est de traverser le désert mais le sable est bouillant', 20, 'Hil100'),
 (8, 'Sauver la princesse', 'Le but est de sauver la princesse Emily mais attention aux ogres', 80,'Hil100');

INSERT INTO creneaux (id_creneau,date_debut,date_fin)
VALUES
(1,'03/12/2022 08:00','03/12/2022 12:00'),
(2,'03/12/2022 14:00','03/12/2022 18:00'),
(3,'04/12/2022 08:00','04/12/2022 12:00'),
(4,'04/12/2022 14:00','04/12/2022 18:00');

INSERT INTO partie (id_partie,id_scenario,id_creneau)
VALUES
(1,1,1),
(2,3,2),
(3,5,3),
(4,6,4);

INSERT INTO inscription_perso (id_partie,id_perso)
VALUES
(1,1),
(1,6 ),
(1,8 ),
(1,12 ),
(2,3),
(2,6),
(2,9 ),
(2,11 ),
(3, 2),
(3, 4),
(3,7 ),
(3,11 ),
(4, 1),
(4,5 ),
(4,8 ),
(4,12);


