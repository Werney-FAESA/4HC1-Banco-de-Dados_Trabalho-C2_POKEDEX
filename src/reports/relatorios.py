import os
from conexion.postgres_queries import PostgresQueries

class Relatorio:
    def __init__(self):
        base_sql_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sql")

        def _read_sql(filename: str) -> str:
            path = f"src/sql/{filename}"
            if not os.path.exists(path):
                path = f"sql/{filename}"
            if not os.path.exists(path):
                path = os.path.join(base_sql_dir, filename)
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        # carrega a query do relatório de batalhas a partir do arquivo SQL
        self.query_relatorio_batalhas = _read_sql("relatorio_batalhas.sql")
        self.query_relatorio_batalhas_vitorias = _read_sql("relatorio_batalhas_vitorias.sql")
        self.query_relatorio_pokemons_evolucao_ult = _read_sql("relatorio_pokemons_evolucao_ult.sql")
        self.query_relatorio_pokemons_evolucao = _read_sql("relatorio_pokemons_evolucao.sql")
        self.query_relatorio_pokemons_quant_regiao = _read_sql("relatorio_pokemons_quant_regiao.sql")
        self.query_relatorio_pokemons_quant_tipo = _read_sql("relatorio_pokemons_quant_tipo.sql")
        self.query_relatorio_pokemons = _read_sql("relatorio_pokemons.sql")
        self.query_relatorio_regiao_quant_pokemonms = _read_sql("relatorio_regiao_quant_pokemons.sql")
        self.query_relatorio_regiao = _read_sql("relatorio_regiao.sql")
        self.query_relatorio_tabelas_quant = _read_sql("relatorio_tabelas_quant.sql")
        self.query_relatorio_treinadores = _read_sql("relatorio_treinadores.sql")
        self.query_relatorio_treinadores_por_regiao = _read_sql("relatorio_treinadores_por_regiao.sql")


    def get_relatorio_batalhas(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_batalhas))
        input("Pressione Enter para sair do relatório de batalhas...")

    def get_relatorio_batalhas_vitorias(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_batalhas_vitorias))
        input("Pressione Enter para sair do relatório de vitórias por treinador...")

    def get_relatorio_pokemons_evolucao_ult(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_pokemons_evolucao_ult))
        input("Pressione Enter para sair do relatório de pokémons a ultima evolução.")


    def get_relatorio_pokemons_evolucao(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_pokemons_evolucao))
        input("Pressione Enter para sair do relatório de pokémons e suas evoluções...")


    def get_relatorio_pokemons_quant_regiao(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_pokemons_quant_regiao))
        input("Pressione Enter para sair do relatório de quantidade de pokémons por região...")


    def get_relatorio_pokemons_quant_tipo(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_pokemons_quant_tipo))
        input("Pressione Enter para sair do relatório de quantidade de pokémons por tipo...")


    def get_relatorio_pokemons(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_pokemons))
        input("Pressione Enter para sair do relatório de pokémons...")


    def get_relatorio_regiao_quant_pokemons(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_regiao_quant_pokemonms))
        input("Pressione Enter para sair do relatório de quantidade de pokémons por região...")


    def get_relatorio_regiao(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_regiao))
        input("Pressione Enter para sair do relatório de regiões...")


    def get_relatorio_tabelas_quant(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_tabelas_quant))
        input("Pressione Enter para sair do relatório de quantidade de registros por tabela...")


    def get_relatorio_treinadores(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_treinadores))
        input("Pressione Enter para sair do relatório de treinadores...")

    def get_relatorio_treinadores_por_regiao(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_treinadores_por_regiao))
        input("Pressione Enter para sair do relatório de treinadores por região...")
