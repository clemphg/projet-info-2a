
--CREATE SCHEMA D_and_D;

CREATE SEQUENCE partie_seq;
CREATE SEQUENCE personnage_seq;
CREATE SEQUENCE journal_seq;
CREATE SEQUENCE scenario_seq;

CREATE TABLE Creneaux (
    id_creneau INT PRIMARY KEY NOT NULL,
    Date_debut DATE,
    Date_fin DATE
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
    date DATE,
    msg TEXT
);

CREATE TABLE mdp(
    pseudo VARCHAR(25) PRIMARY KEY,
    mdp TEXT
)

INSERT INTO joueur (pseudo_j, motdepasse_j, age)
 VALUES
 ('Rébecca70', 24),
 ('Aimée20', 36),
 ('Marielle90', 27),
 ('Hilaire100', 58);

INSERT INTO maitre_de_jeu (pseudo_mj, age)
 VALUES
 ('GiGi', 25),
 ('Amy10', 22),
 ('Marie18', 28),
 ('Hil100', 60);

INSERT INTO organisateur (pseudo_organisateur)
 VALUES
 ('Amima20'),
 ('Amira100'),
 ('Maria180'),
 ('Hihi100');

INSERT INTO personnage (nom, age, niveau, race, classe, pseudo_j)
 VALUES
 ('Elyanna', 200, 200,'elf', 'enchantresse','Rébecca70'),
 ( 'Emir', 18, 200, 'humain','épéiste','Rébecca70'),
 ( 'Elliot', 500, 200, 'démon','épéiste','Rébecca70'),
 ('Blondinet', 200, 50, 'nain', 'enchanteur','Aimée20'),
 ('Erys', 30, 100, 'humain','roi','Aimée20'),
 ( 'Lucifer', 800, 300, 'démon','enchanteur','Aimée20'),
 ('Elodie', 200, 20,'elf', 'enchantresse','Marielle90'),
 ( 'Aymen', 180, 200, 'dragon','combattant','Marielle90'),
 ( 'Amor', 20, 200, 'humain','enchantresse','Marielle90'),
 ('Isabella', 200, 20,'elf','enchantresse','Hilaire100'),
 ( 'Arthur', 18, 200, 'humain','prince','Hilaire100'),
 ( 'Orifice', 500, 200, 'démon', 'forgeron', 'Hilaire100');

INSERT INTO scenario (nom, descrip, niveau, pseudo_mj)
 VALUES
 ('Désert de cadavres','Le jeu se déroulera dans un désert infesté de scorpions mortels', 200,'GiGi'),
 ('Volcan enflammé',' Le jeu se déroulera dans un volcan en éruption', 200,'GiGi'),
 ('Mer enchantée','Le jeu se déroulera dans une mer infestée de sirènes croqueuses d hommes', 200,'Amy10'),
 ('Montagne à dents de scie', 'Le jeu se déroulera dans une montagne infestée d ours mutants', 50,'Amy10'),
 ('Bataille navale', 'Le jeu se déroulera sous l eau',100,'Marie18'),
 ('Bataille dans le ciel', 'Le jeu se déroulera dans le ciel mais attention aux licornes armées',50,'Marie18'),
 ('Sable bouillant', 'Le but est de traverser le désert mais le sable est bouillant', 20, 'Hil100'),
 ('Sauver la princesse', 'Le but est de sauver la princesse Emily mais attention aux ogres', 80,'Hil100');

INSERT INTO creneaux (id_creneau, date_debut,date_fin)
VALUES
(1, '03/12/2022 08:00','03/12/2022 12:00'),
(2, '03/12/2022 14:00','03/12/2022 18:00'),
(3, '04/12/2022 08:00','04/12/2022 12:00'),
(4, '04/12/2022 14:00','04/12/2022 18:00');

INSERT INTO partie (id_scenario,id_creneau)
VALUES
(1,1),
(3,2),
(5,3),
(6,4);

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

INSERT INTO mdp (pseudo,mdp)
VALUES
('Rebecca70', 'bf2974666f328dbf43b4f624c62e0fbfe99ac61b551a437db581b0d57f96ee08'),
('Aimée20', '5d08112296cdfb40ece55f7c492076b79db5fd83f286c9d0ed238a6bd9d0f890'),
('Marielle90', '5cb1db588988ff1217768c74be9a7cf102cb7034d1f37ebd9978ae1d18f62c1a'),
('Hilaire100', 'f7dc98d348d95012795b68b120e39ee078d22cbbfd7b64acd93395a75cae2459'),
('GiGigigi', '3253e1229e98a4db730bf95d81acb3e66a6d6f863265d609a8dcf77cfcdcc953'),
('Amy10', '96836acdccf43d477c11409043664c442e8b8fdf55e94c85efd1febc9bedc426'),
('Marie18', '11485eb472a3f6e8ef10a81b9abb041de33bb2d4c4bfaf66170571cfc39b832a'),
('Hil100', '2ff25d7535f9eee99551026545ac7f810633e14c56b02f8ea3064ee2b9048404'),
('Amima20', 'f56f248221d9a05e8b5bf1bdbd9f2a9b43dbb37ffb5b130a3455e0e629980f84'),
('Amira100', 'ece4fae69e8b664a484893153f40ecfc58bb33695785cb50defe30d91d713702'),
('Maria180', 'ecd61231077f53d46f51ae6826a6c595f0d10591458d3883531c26a4f3c88a53'),
('Hihi100', 'f45ee875ec85143d36410b2bae622e6bbcef9e344e7528d219cb112a0116cc63');