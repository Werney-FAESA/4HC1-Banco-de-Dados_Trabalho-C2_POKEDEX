CREATE TABLE tb_regiao (
    id_regiao INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_regiao VARCHAR(50) NOT NULL UNIQUE,
    professor_responsavel VARCHAR(100)
);

INSERT INTO tb_regiao ( nome_regiao, professor_responsavel)
VALUES
    ('Kanto', 'Professor Carvalho'),
    ('Johto', 'Professor Elm'),
    ('Hoenn', 'Professor Birch');