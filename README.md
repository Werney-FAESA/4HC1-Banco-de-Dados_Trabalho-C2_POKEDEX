# 4HC1-Banco-de-Dados_Trabalho-C2_POKEDEX

## Conexao com o PostgreSQL

O projeto usa `psycopg2` diretamente, sem ORM. O banco roda pelo Docker Compose e
fica disponivel em `localhost:5432`.

### Preparar o ambiente

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requeriments.txt
sudo docker compose up -d
sudo docker compose ps
```

O servico `db` deve aparecer como `running` ou `Up`. O comando `sudo` e necessario
neste ambiente para acessar a API do Docker.

### Validar a conexao

Execute uma consulta minima usando a classe da aplicacao:

```bash
python -c "from src.conexion.conexion import PostgresQueries; resultado = PostgresQueries().sqlToDataFrame('SELECT 1 AS conectado'); print(resultado.to_string(index=False))"
```

O resultado esperado e:

```text
 conectado
	 1
```

Para testar uma tabela do banco, execute:

```bash
python -c "from src.conexion.conexion import PostgresQueries; print(PostgresQueries().sqlToDataFrame('SELECT * FROM pokemon LIMIT 5'))"
```

As configuracoes podem ser sobrescritas pelas variaveis `POSTGRES_HOST`,
`POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_USER` e `POSTGRES_PASSWORD`.

### Como usar

Consultas recebem parametros separados do SQL. O `psycopg2` faz o escaping correto;
nao concatene valores diretamente na string da consulta.

```python
from src.conexion.conexion import PostgresQueries

db = PostgresQueries()
try:
	resultado = db.sqlToDataFrame(
		"SELECT * FROM pokemon WHERE nome = %s",
		("Pikachu",),
	)
finally:
	db.close()
```

Para escrever, abra explicitamente uma conexao com permissao de escrita:

```python
db = PostgresQueries(can_write=True)
try:
	db.write(
		"UPDATE pokemon SET altura = %s WHERE id_pokemon = %s",
		(0.4, 25),
	)
finally:
	db.close()
```

Em caso de falha de escrita, a transacao recebe `rollback`. Consultas de leitura
retornam um `DataFrame` vazio quando ocorre um erro de banco, enquanto erros de
integridade e conexao sao relancados para que a camada superior possa trata-los.
