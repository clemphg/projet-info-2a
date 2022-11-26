
INSERT INTO joueur (pseudo_j, age)
 VALUES
 ('Rebecca70', 24),
 ('Aimee20', 36),
 ('Marielle90', 27),
 ('Hilaire100', 58);

INSERT INTO maitre_de_jeu (pseudo_mj, age)
 VALUES
 ('GiGigigi', 25),
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
 ('Elyanna', 200, 200,'Elf', 'Wizard','Rebecca70'),
 ( 'Emir', 18, 200, 'Human','Rogue','Rebecca70'),
 ( 'Elliot', 500, 200, 'Tiefling','Bard','Rebecca70'),
 ('Blondinet', 200, 50, 'Dwarf', 'Fighter','Aimee20'),
 ('Erys', 30, 100, 'Human','Paladin','Aimee20'),
 ( 'Lucifer', 800, 300, 'Tiefling','Barbarian','Aimee20'),
 ('Elodie', 200, 20,'Half-Elf', 'Paladin','Marielle90'),
 ( 'Aymen', 180, 200, 'Dragonborn','Fighter','Marielle90'),
 ( 'Amor', 20, 200, 'Human','Rogue','Marielle90'),
 ('Isabella', 200, 20,'Elf','Sorcerer','Hilaire100'),
 ( 'Arthur', 18, 200, 'Human','Druid','Hilaire100'),
 ( 'Orfevre', 500, 200, 'Tiefling', 'Monk', 'Hilaire100');

INSERT INTO scenario (nom, descrip, niveau, pseudo_mj)
 VALUES
 ('Désert de cadavres','Le jeu se déroulera dans un désert infesté de scorpions mortels', 200,'GiGigigi'),
 ('Volcan enflammé',' Le jeu se déroulera dans un volcan en éruption', 200,'GiGigigi'),
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
('Aimee20', '15067c616e3f58863396a2acdc81c2f0cc224bd49d7be3b2059d2afdc551c9a0'),
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

INSERT INTO journal (pseudo,date,msg)
VALUES
('Rebecca70', '21/11/2022 08:00', 'Inscription sur la plateforme.'),
('Rebecca70', '21/11/2022 08:30', 'Création du personnage 1 (Elyanna, 200 ans, niveau 200, Elf, Wizard).'),
('Rebecca70', '21/11/2022 08:35', 'Création du personnage 2 (Emir, 18 ans, niveau 200, Human, Rogue).'),
('Rebecca70', '21/11/2022 09:00', 'Création du personnage 3 (Elliot, 500 ans, niveau 200, Tiefling, Bard).'),
('Rebecca70', '21/11/2022 09:05', 'Inscription à la partie 4 avec le personnage 1.'),
('Rebecca70', '21/11/2022 09:07', 'Inscription à la partie 2 avec le personnage 3.'),
('Rebecca70', '21/11/2022 09:10', 'Inscription à la partie 3 avec le personnage 2.'),
('Aimee20', '22/11/2022 08:00', 'Inscription sur la plateforme.'),
('Marielle90', '23/11/2022 08:00', 'Inscription sur la plateforme.'),
('Hilaire100', '24/11/2022 08:00', 'Inscription sur la plateforme.');