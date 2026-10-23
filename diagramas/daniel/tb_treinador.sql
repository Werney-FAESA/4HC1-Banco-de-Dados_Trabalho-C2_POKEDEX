CREATE TABLE tb_treinador (
    id_treinador INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER,
    id_regiao INTEGER NOT NULL,
    
    constraint TREINADOR_REGIAO_FK foreign key (id_regiao)
        references tb_regiao (id_regiao)
);

INSERT INTO tb_treinador ( nome, idade, id_regiao)
VALUES
    ('Ash', '10', '1'),
    ('Gary', '10', '2'),
    ('Misty', '12', '3');