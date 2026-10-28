CREATE TABLE TB_REGIAO (
    id_regiao INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_regiao VARCHAR(50) NOT NULL UNIQUE,
    professor_responsavel VARCHAR(100)
);

CREATE TABLE TB_TREINADOR (
    id_treinador INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER,
    id_regiao INTEGER NOT NULL,
    
    constraint TREINADOR_REGIAO_FK foreign key (id_regiao)
        references tb_regiao (id_regiao)
);

create table TB_POKEMON (
	id_pokemon INTEGER not null,
	nome_pokemon varchar(50) not null,
	tipo_primario varchar(50) not null,
	tipo_secundario varchar(50),
	nivel_base INTEGER,
	id_regiao INTEGER not null,
	
	constraint POKEMON_PK primary key (id_pokemon),
	
	constraint POKEMON_REGIAO_FK
		foreign key (id_regiao)
		references TB_REGIAO (id_regiao)
);

create table TB_EVOLUCAO (
	id_evolucao int not null,
	id_pokemon_base int not null,
	id_pokemon_evoluido int not null,
	nivel_evolucao int,
	modo_evolucao varchar(50) not null,
	
	constraint EVOLUCAO_PK primary key (id_evolucao),
	constraint POKEMON_BASE_FK foreign key (id_pokemon_base) references TB_POKEMON (id_pokemon),
	constraint POKEMON_EVOLUIDO_FK foreign key (id_pokemon_evoluido) references TB_POKEMON (id_pokemon)
	
);create table TB_BATALHA (
	id_batalha int not null,
	id_treinador_1 int not null,
	id_treinador_2 int not null,
	data_batalha date not null,
	id_vencedor int not null,
	local_batalha varchar(50) not null,
	
	constraint BATALHA_PK primary key (id_batalha),
	constraint TREINADOR_1_FK foreign key (id_treinador_1) references TB_TREINADOR (id_treinador),
	constraint TREINADOR_2_FK foreign key (id_treinador_2) references TB_TREINADOR (id_treinador),
	constraint VENCEDOR_FK foreign key (id_vencedor) references TB_TREINADOR (id_treinador)
);

commit;