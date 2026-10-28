INSERT INTO tb_regiao ( nome_regiao, professor_responsavel)
VALUES
    ('Kanto', 'Professor Carvalho'),
    ('Johto', 'Professor Elm'),
    ('Hoenn', 'Professor Birch');

INSERT INTO tb_treinador ( nome, idade, id_regiao)
VALUES
    ('Ash', '10', '1'),
    ('Gary', '10', '2'),
    ('Brock', '15', '1'),
    ('Misty', '12', '3'),
    ('Lance', '25', '1'),
    ('Ethan', '11', '2'),
    ('Claire', '19', '2'),
    ('Silver', '11', '2'),
    ('Whitney', '16', '2'),
    ('Falkner', '17', '2'),
    ('Steven Stone', '25', '3'),
    ('May', '10', '3'),
    ('Brendan', '12', '3'),
    ('Wally', '10', '3'),
    ('Wallace', '24', '3');


-- Kanto (id_regiao = 1)
INSERT INTO tb_pokemon VALUES (1, 'Bulbasaur', 'Grass', 'Poison', 1, 1);
INSERT INTO tb_pokemon VALUES (2, 'Ivysaur', 'Grass', 'Poison', 16, 1);
INSERT INTO tb_pokemon VALUES (3, 'Venusaur', 'Grass', 'Poison', 32, 1);
INSERT INTO tb_pokemon VALUES (4, 'Charmander', 'Fire', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (5, 'Charmeleon', 'Fire', NULL, 16, 1);
INSERT INTO tb_pokemon VALUES (6, 'Charizard', 'Fire', 'Flying', 36, 1);
INSERT INTO tb_pokemon VALUES (7, 'Squirtle', 'Water', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (8, 'Wartortle', 'Water', NULL, 16, 1);
INSERT INTO tb_pokemon VALUES (9, 'Blastoise', 'Water', NULL, 36, 1);
INSERT INTO tb_pokemon VALUES (10, 'Caterpie', 'Bug', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (11, 'Metapod', 'Bug', NULL, 7, 1);
INSERT INTO tb_pokemon VALUES (12, 'Butterfree', 'Bug', 'Flying', 10, 1);
INSERT INTO tb_pokemon VALUES (13, 'Weedle', 'Bug', 'Poison', 1, 1);
INSERT INTO tb_pokemon VALUES (14, 'Kakuna', 'Bug', 'Poison', 7, 1);
INSERT INTO tb_pokemon VALUES (15, 'Beedrill', 'Bug', 'Poison', 10, 1);
INSERT INTO tb_pokemon VALUES (16, 'Pidgey', 'Normal', 'Flying', 1, 1);
INSERT INTO tb_pokemon VALUES (17, 'Pidgeotto', 'Normal', 'Flying', 18, 1);
INSERT INTO tb_pokemon VALUES (18, 'Pidgeot', 'Normal', 'Flying', 36, 1);
INSERT INTO tb_pokemon VALUES (19, 'Rattata', 'Normal', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (20, 'Raticate', 'Normal', NULL, 20, 1);
INSERT INTO tb_pokemon VALUES (25, 'Pikachu', 'Electric', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (26, 'Raichu', 'Electric', NULL, NULL, 1);
INSERT INTO tb_pokemon VALUES (35, 'Clefairy', 'Fairy', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (36, 'Clefable', 'Fairy', NULL, NULL, 1);
INSERT INTO tb_pokemon VALUES (39, 'Jigglypuff', 'Normal', 'Fairy', 1, 1);
INSERT INTO tb_pokemon VALUES (40, 'Wigglytuff', 'Normal', 'Fairy', NULL, 1);
INSERT INTO tb_pokemon VALUES (41, 'Zubat', 'Poison', 'Flying', 1, 1);
INSERT INTO tb_pokemon VALUES (42, 'Golbat', 'Poison', 'Flying', 22, 1);
INSERT INTO tb_pokemon VALUES (43, 'Oddish', 'Grass', 'Poison', 1, 1);
INSERT INTO tb_pokemon VALUES (44, 'Gloom', 'Grass', 'Poison', 21, 1);
INSERT INTO tb_pokemon VALUES (45, 'Vileplume', 'Grass', 'Poison', NULL, 1);
INSERT INTO tb_pokemon VALUES (52, 'Meowth', 'Normal', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (53, 'Persian', 'Normal', NULL, 28, 1);
INSERT INTO tb_pokemon VALUES (54, 'Psyduck', 'Water', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (55, 'Golduck', 'Water', NULL, 33, 1);
INSERT INTO tb_pokemon VALUES (58, 'Growlithe', 'Fire', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (59, 'Arcanine', 'Fire', NULL, NULL, 1);
INSERT INTO tb_pokemon VALUES (60, 'Poliwag', 'Water', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (61, 'Poliwhirl', 'Water', NULL, 25, 1);
INSERT INTO tb_pokemon VALUES (62, 'Poliwrath', 'Water', 'Fighting', NULL, 1);
INSERT INTO tb_pokemon VALUES (63, 'Abra', 'Psychic', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (64, 'Kadabra', 'Psychic', NULL, 16, 1);
INSERT INTO tb_pokemon VALUES (65, 'Alakazam', 'Psychic', NULL, NULL, 1);
INSERT INTO tb_pokemon VALUES (66, 'Machop', 'Fighting', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (67, 'Machoke', 'Fighting', NULL, 28, 1);
INSERT INTO tb_pokemon VALUES (68, 'Machamp', 'Fighting', NULL, NULL, 1);
INSERT INTO tb_pokemon VALUES (74, 'Geodude', 'Rock', 'Ground', 1, 1);
INSERT INTO tb_pokemon VALUES (75, 'Graveler', 'Rock', 'Ground', 25, 1);
INSERT INTO tb_pokemon VALUES (76, 'Golem', 'Rock', 'Ground', NULL, 1);
INSERT INTO tb_pokemon VALUES (92, 'Gastly', 'Ghost', 'Poison', 1, 1);
INSERT INTO tb_pokemon VALUES (93, 'Haunter', 'Ghost', 'Poison', 25, 1);
INSERT INTO tb_pokemon VALUES (94, 'Gengar', 'Ghost', 'Poison', NULL, 1);
INSERT INTO tb_pokemon VALUES (95, 'Onix', 'Rock', 'Ground', 1, 1);
INSERT INTO tb_pokemon VALUES (129, 'Magikarp', 'Water', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (130, 'Gyarados', 'Water', 'Flying', 20, 1);
INSERT INTO tb_pokemon VALUES (131, 'Lapras', 'Water', 'Ice', 1, 1);
INSERT INTO tb_pokemon VALUES (132, 'Ditto', 'Normal', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (133, 'Eevee', 'Normal', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (134, 'Vaporeon', 'Water', NULL, NULL, 1);
INSERT INTO tb_pokemon VALUES (135, 'Jolteon', 'Electric', NULL, NULL, 1);
INSERT INTO tb_pokemon VALUES (136, 'Flareon', 'Fire', NULL, NULL, 1);
INSERT INTO tb_pokemon VALUES (143, 'Snorlax', 'Normal', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (144, 'Articuno', 'Ice', 'Flying', 50, 1);
INSERT INTO tb_pokemon VALUES (145, 'Zapdos', 'Electric', 'Flying', 50, 1);
INSERT INTO tb_pokemon VALUES (146, 'Moltres', 'Fire', 'Flying', 50, 1);
INSERT INTO tb_pokemon VALUES (147, 'Dratini', 'Dragon', NULL, 1, 1);
INSERT INTO tb_pokemon VALUES (148, 'Dragonair', 'Dragon', NULL, 30, 1);
INSERT INTO tb_pokemon VALUES (149, 'Dragonite', 'Dragon', 'Flying', 55, 1);
INSERT INTO tb_pokemon VALUES (150, 'Mewtwo', 'Psychic', NULL, 70, 1);
INSERT INTO tb_pokemon VALUES (151, 'Mew', 'Psychic', NULL, 1, 1);

-- Johto (id_regiao = 2)
INSERT INTO tb_pokemon VALUES (152, 'Chikorita', 'Grass', NULL, 1, 2);
INSERT INTO tb_pokemon VALUES (153, 'Bayleef', 'Grass', NULL, 16, 2);
INSERT INTO tb_pokemon VALUES (154, 'Meganium', 'Grass', NULL, 32, 2);
INSERT INTO tb_pokemon VALUES (155, 'Cyndaquil', 'Fire', NULL, 1, 2);
INSERT INTO tb_pokemon VALUES (156, 'Quilava', 'Fire', NULL, 14, 2);
INSERT INTO tb_pokemon VALUES (157, 'Typhlosion', 'Fire', NULL, 36, 2);
INSERT INTO tb_pokemon VALUES (158, 'Totodile', 'Water', NULL, 1, 2);
INSERT INTO tb_pokemon VALUES (159, 'Croconaw', 'Water', NULL, 18, 2);
INSERT INTO tb_pokemon VALUES (160, 'Feraligatr', 'Water', NULL, 30, 2);
INSERT INTO tb_pokemon VALUES (172, 'Pichu', 'Electric', NULL, 1, 2);
INSERT INTO tb_pokemon VALUES (175, 'Togepi', 'Fairy', NULL, 1, 2);
INSERT INTO tb_pokemon VALUES (176, 'Togetic', 'Fairy', 'Flying', NULL, 2);
INSERT INTO tb_pokemon VALUES (179, 'Mareep', 'Electric', NULL, 1, 2);
INSERT INTO tb_pokemon VALUES (180, 'Flaaffy', 'Electric', NULL, 15, 2);
INSERT INTO tb_pokemon VALUES (181, 'Ampharos', 'Electric', NULL, 30, 2);
INSERT INTO tb_pokemon VALUES (196, 'Espeon', 'Psychic', NULL, NULL, 2);
INSERT INTO tb_pokemon VALUES (197, 'Umbreon', 'Dark', NULL, NULL, 2);
INSERT INTO tb_pokemon VALUES (212, 'Scizor', 'Bug', 'Steel', NULL, 2);
INSERT INTO tb_pokemon VALUES (246, 'Larvitar', 'Rock', 'Ground', 1, 2);
INSERT INTO tb_pokemon VALUES (247, 'Pupitar', 'Rock', 'Ground', 30, 2);
INSERT INTO tb_pokemon VALUES (248, 'Tyranitar', 'Rock', 'Dark', 55, 2);
INSERT INTO tb_pokemon VALUES (249, 'Lugia', 'Psychic', 'Flying', 70, 2);
INSERT INTO tb_pokemon VALUES (250, 'Ho-Oh', 'Fire', 'Flying', 70, 2);

-- Hoenn (id_regiao = 3)
INSERT INTO tb_pokemon VALUES (252, 'Treecko', 'Grass', NULL, 1, 3);
INSERT INTO tb_pokemon VALUES (253, 'Grovyle', 'Grass', NULL, 16, 3);
INSERT INTO tb_pokemon VALUES (254, 'Sceptile', 'Grass', NULL, 36, 3);
INSERT INTO tb_pokemon VALUES (255, 'Torchic', 'Fire', NULL, 1, 3);
INSERT INTO tb_pokemon VALUES (256, 'Combusken', 'Fire', 'Fighting', 16, 3);
INSERT INTO tb_pokemon VALUES (257, 'Blaziken', 'Fire', 'Fighting', 36, 3);
INSERT INTO tb_pokemon VALUES (258, 'Mudkip', 'Water', NULL, 1, 3);


-- Linha Bulbasaur -> Ivysaur -> Venusaur
INSERT INTO tb_evolucao VALUES (1, 1, 2, 16, 'Nível');
INSERT INTO tb_evolucao VALUES (2, 2, 3, 32, 'Nível');

-- Linha Charmander -> Charmeleon -> Charizard
INSERT INTO tb_evolucao VALUES (3, 4, 5, 16, 'Nível');
INSERT INTO tb_evolucao VALUES (4, 5, 6, 36, 'Nível');

-- Linha Squirtle -> Wartortle -> Blastoise
INSERT INTO tb_evolucao VALUES (5, 7, 8, 16, 'Nível');
INSERT INTO tb_evolucao VALUES (6, 8, 9, 36, 'Nível');

-- Linha Caterpie -> Metapod -> Butterfree
INSERT INTO tb_evolucao VALUES (7, 10, 11, 7, 'Nível');
INSERT INTO tb_evolucao VALUES (8, 11, 12, 10, 'Nível');

-- Linha Weedle -> Kakuna -> Beedrill
INSERT INTO tb_evolucao VALUES (9, 13, 14, 7, 'Nível');
INSERT INTO tb_evolucao VALUES (10, 14, 15, 10, 'Nível');

-- Linha Pidgey -> Pidgeotto -> Pidgeot
INSERT INTO tb_evolucao VALUES (11, 16, 17, 18, 'Nível');
INSERT INTO tb_evolucao VALUES (12, 17, 18, 36, 'Nível');

-- Linha Rattata -> Raticate
INSERT INTO tb_evolucao VALUES (13, 19, 20, 20, 'Nível');

-- Linha Pichu -> Pikachu -> Raichu
INSERT INTO tb_evolucao VALUES (14, 172, 25, NULL, 'Amizade');
INSERT INTO tb_evolucao VALUES (15, 25, 26, NULL, 'Pedra do Trovão');

-- Linha Clefairy -> Clefable
INSERT INTO tb_evolucao VALUES (16, 35, 36, NULL, 'Pedra da Lua');

-- Linha Jigglypuff -> Wigglytuff
INSERT INTO tb_evolucao VALUES (17, 39, 40, NULL, 'Pedra da Lua');

-- Linha Zubat -> Golbat
INSERT INTO tb_evolucao VALUES (18, 41, 42, 22, 'Nível');

-- Linha Oddish -> Gloom -> Vileplume
INSERT INTO tb_evolucao VALUES (19, 43, 44, 21, 'Nível');
INSERT INTO tb_evolucao VALUES (20, 44, 45, NULL, 'Pedra da Folha');

-- Linha Meowth -> Persian
INSERT INTO tb_evolucao VALUES (21, 52, 53, 28, 'Nível');

-- Linha Psyduck -> Golduck
INSERT INTO tb_evolucao VALUES (22, 54, 55, 33, 'Nível');

-- Linha Growlithe -> Arcanine
INSERT INTO tb_evolucao VALUES (23, 58, 59, NULL, 'Pedra do Fogo');

-- Linha Poliwag -> Poliwhirl -> Poliwrath
INSERT INTO tb_evolucao VALUES (24, 60, 61, 25, 'Nível');
INSERT INTO tb_evolucao VALUES (25, 61, 62, NULL, 'Pedra da Água');

-- Linha Abra -> Kadabra -> Alakazam
INSERT INTO tb_evolucao VALUES (26, 63, 64, 16, 'Nível');
INSERT INTO tb_evolucao VALUES (27, 64, 65, NULL, 'Troca');

-- Linha Machop -> Machoke -> Machamp
INSERT INTO tb_evolucao VALUES (28, 66, 67, 28, 'Nível');
INSERT INTO tb_evolucao VALUES (29, 67, 68, NULL, 'Troca');

-- Linha Geodude -> Graveler -> Golem
INSERT INTO tb_evolucao VALUES (30, 74, 75, 25, 'Nível');
INSERT INTO tb_evolucao VALUES (31, 75, 76, NULL, 'Troca');

-- Linha Gastly -> Haunter -> Gengar
INSERT INTO tb_evolucao VALUES (32, 92, 93, 25, 'Nível');
INSERT INTO tb_evolucao VALUES (33, 93, 94, NULL, 'Troca');

-- Linha Magikarp -> Gyarados
INSERT INTO tb_evolucao VALUES (34, 129, 130, 20, 'Nível');

-- Linha Eevee -> Vaporeon / Jolteon / Flareon / Espeon / Umbreon
INSERT INTO tb_evolucao VALUES (35, 133, 134, NULL, 'Pedra da Água');
INSERT INTO tb_evolucao VALUES (36, 133, 135, NULL, 'Pedra do Trovão');
INSERT INTO tb_evolucao VALUES (37, 133, 136, NULL, 'Pedra do Fogo');
INSERT INTO tb_evolucao VALUES (38, 133, 196, NULL, 'Amizade (Dia)');
INSERT INTO tb_evolucao VALUES (39, 133, 197, NULL, 'Amizade (Noite)');

-- Linha Dratini -> Dragonair -> Dragonite
INSERT INTO tb_evolucao VALUES (40, 147, 148, 30, 'Nível');
INSERT INTO tb_evolucao VALUES (41, 148, 149, 55, 'Nível');

-- Linha Chikorita -> Bayleef -> Meganium
INSERT INTO tb_evolucao VALUES (42, 152, 153, 16, 'Nível');
INSERT INTO tb_evolucao VALUES (43, 153, 154, 32, 'Nível');

-- Linha Cyndaquil -> Quilava -> Typhlosion
INSERT INTO tb_evolucao VALUES (44, 155, 156, 14, 'Nível');
INSERT INTO tb_evolucao VALUES (45, 156, 157, 36, 'Nível');

-- Linha Totodile -> Croconaw -> Feraligatr
INSERT INTO tb_evolucao VALUES (46, 158, 159, 18, 'Nível');
INSERT INTO tb_evolucao VALUES (47, 159, 160, 30, 'Nível');

-- Linha Togepi -> Togetic
INSERT INTO tb_evolucao VALUES (48, 175, 176, NULL, 'Amizade');

-- Linha Mareep -> Flaaffy -> Ampharos
INSERT INTO tb_evolucao VALUES (49, 179, 180, 15, 'Nível');
INSERT INTO tb_evolucao VALUES (50, 180, 181, 30, 'Nível');

-- Linha Larvitar -> Pupitar -> Tyranitar
INSERT INTO tb_evolucao VALUES (51, 246, 247, 30, 'Nível');
INSERT INTO tb_evolucao VALUES (52, 247, 248, 55, 'Nível');

-- Linha Treecko -> Grovyle -> Sceptile
INSERT INTO tb_evolucao VALUES (53, 252, 253, 16, 'Nível');
INSERT INTO tb_evolucao VALUES (54, 253, 254, 36, 'Nível');

-- Linha Torchic -> Combusken -> Blaziken
INSERT INTO tb_evolucao VALUES (55, 255, 256, 16, 'Nível');
INSERT INTO tb_evolucao VALUES (56, 256, 257, 36, 'Nível');


INSERT INTO tb_batalha VALUES (1, 1, 2, DATE '2024-01-15', 1, 'Cerulean Gym');
INSERT INTO tb_batalha VALUES (2, 1, 3, DATE '2024-01-20', 1, 'Pewter Gym');
INSERT INTO tb_batalha VALUES (3, 1, 4, DATE '2024-01-28', 4, 'Cerulean Gym');
INSERT INTO tb_batalha VALUES (4, 2, 5, DATE '2024-02-05', 5, 'Indigo Plateau');
INSERT INTO tb_batalha VALUES (5, 6, 8, DATE '2024-02-12', 6, 'Cherrygrove City');
INSERT INTO tb_batalha VALUES (6, 6, 10, DATE '2024-02-18', 6, 'Violet Gym');
INSERT INTO tb_batalha VALUES (7, 6, 9, DATE '2024-02-25', 9, 'Goldenrod Gym');
INSERT INTO tb_batalha VALUES (8, 8, 7, DATE '2024-03-02', 7, 'Blackthorn Gym');
INSERT INTO tb_batalha VALUES (9, 5, 7, DATE '2024-03-10', 5, 'Dragon''s Den');
INSERT INTO tb_batalha VALUES (10, 12, 13, DATE '2024-03-15', 13, 'Route 103');
INSERT INTO tb_batalha VALUES (11, 13, 14, DATE '2024-03-22', 13, 'Mauville Gym');
INSERT INTO tb_batalha VALUES (12, 11, 15, DATE '2024-04-01', 11, 'Ever Grande City');
INSERT INTO tb_batalha VALUES (13, 12, 15, DATE '2024-04-08', 15, 'Sootopolis Gym');
INSERT INTO tb_batalha VALUES (14, 1, 6, DATE '2024-04-19', 6, 'Mt. Silver');
INSERT INTO tb_batalha VALUES (15, 3, 4, DATE '2024-04-25', 4, 'Vermilion City');
INSERT INTO tb_batalha VALUES (16, 2, 8, DATE '2024-05-03', 2, 'Viridian Gym');
INSERT INTO tb_batalha VALUES (17, 9, 10, DATE '2024-05-11', 10, 'National Park');
INSERT INTO tb_batalha VALUES (18, 11, 13, DATE '2024-05-18', 11, 'Meteor Falls');
INSERT INTO tb_batalha VALUES (19, 14, 12, DATE '2024-05-24', 14, 'Victory Road');
INSERT INTO tb_batalha VALUES (20, 5, 11, DATE '2024-06-01', 11, 'Pokemon World Tournament');

commit;