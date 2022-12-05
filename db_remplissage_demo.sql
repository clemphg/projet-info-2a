
INSERT INTO creneaux (id_creneau, date_debut,date_fin)
VALUES
(1, '10/12/2022 08:00','10/12/2022 12:00'),
(2, '10/12/2022 14:00','10/12/2022 18:00'),
(3, '11/12/2022 08:00','11/12/2022 12:00'),
(4, '11/12/2022 14:00','11/12/2022 18:00');


INSERT INTO joueur (pseudo_j, age)
 VALUES
 ('Ilona0706', 21),
 ('Aurore', 58);

INSERT INTO maitre_de_jeu (pseudo_mj, age)
 VALUES
 ('Baptiste', 21);

INSERT INTO organisateur (pseudo_organisateur)
 VALUES
 ('Clementine');

INSERT INTO personnage (nom, age, niveau, race, classe, pseudo_j)
 VALUES
 ('Elyanna', 150, 200,'Elf', 'Wizard','Aurore');

INSERT INTO scenario (nom, descrip, niveau, pseudo_mj)
 VALUES
 ('Désert de cadavres','Le jeu se déroulera dans un désert infesté de scorpions mortels', 150,'Baptiste'),
 ('Volcan enflammé',' Le jeu se déroulera dans un volcan en éruption', 200,'Baptiste');

INSERT INTO mdp (pseudo,mdp)
VALUES
('Ilona0706', 'c0c87baf8949d61e4d71894a8cb4901936f9e8d98a534db72d5e0d6695852c1a'),
('Baptiste', 'a1af2782a5dcda0ef0b93500e19de715e34a5ffabeec33ee57ccd300d2fea418'),
('Aurore', '8c100733d30e43ede3a98eb14fede2cb9b73c9e032804a059e7806bbb5c8a3fc'),
('Clementine', '5ec864311cd89aa4ff2d3f6a3f44e4d347da9c6d8c154edb6e73d6c9d750e5a8');

INSERT INTO journal (pseudo,date,msg)
VALUES
('Ilona0706', '06/12/2022 08:00', 'Inscription sur la plateforme.'),
('Baptiste', '06/12/2022 09:00', 'Inscription sur la plateforme.'),
('Baptiste', '06/12/2022 09:07', 'Création du scénario 1 (Désert de cadavres, niveau minimum : 150).'),
('Baptiste', '06/12/2022 09:10', 'Création du scénario 2 (Volcan enflammé, niveau minimum : 200).'),
('Aurore', '06/12/2022 08:00', 'Inscription sur la plateforme.'),
('Aurore', '06/12/2022 08:05', 'Création du personnage 1 (Alyanna, 150 ans, niveau 200, Elf, Wizard).'),
('Clementine', '06/12/2022 08:00', 'Inscription sur la plateforme.');