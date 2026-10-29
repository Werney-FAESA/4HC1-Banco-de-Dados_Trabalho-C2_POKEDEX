from conexion.postgres_queries import PostgresQueries

class Relatorio:
    def __init__(self):

        # carrega a query do relatório de batalhas a partir do arquivo SQL
        with open("src/sql/relatorio_batalhas.sql") as f:
            self.query_relatorio_batalhas = f.read()

        with open("src/sql/relatorio_batalhas_vitorias.sql") as f:
            self.query_relatorio_batalhas_vitorias = f.read()

        with open("src/sql/relatorio_pokemons_evolucao_ult.sql") as f:
            self.query_relatorio_pokemons_evolucao_ult = f.read()


        with open("src/sql/relatorio_pokemons_evolucao.sql") as f:
            self.query_relatorio_pokemons_evolucao = f.read()


        with open("src/sql/relatorio_pokemons_quant_regiao.sql") as f:
            self.query_relatorio_pokemons_quant_regiao = f.read()   


        with open("src/sql/relatorio_pokemons_quant_tipo.sql") as f:
            self.query_relatorio_pokemons_quant_tipo = f.read()


        with open("src/sql/relatorio_pokemons.sql") as f:
            self.query_relatorio_pokemons = f.read()



        with open("src/sql/relatorio_regiao_quant_pokemons.sql") as f:
            self.query_relatorio_regiao_quant_pokemonms = f.read()


        with open("src/sql/relatorio_regiao.sql") as f:
            self.query_relatorio_regiao = f.read()

        with open("src/sql/relatorio_tabelas_quant.sql") as f:
            self.query_relatorio_tabelas_quant = f.read()



        with open("src/sql/relatorio_treinadores.sql") as f: 
            self.query_relatorio_treinadores = f.read()

        with open("src/sql/relatorio_treinadores_por_regiao.sql") as f:
            self.query_relatorio_treinadores_por_regiao = f.read()


    def get_relatorio_batalhas(self):
        postgres = PostgresQueries()
        postgres.connect()
        print(postgres.sqlToDataFrame(self.query_relatorio_batalhas))
        input("Pressione Enter para sair do relatório de batalhas...")

    def get_relatorio_batalhas_vitorias(self):
        postgres = PostgresQueries()
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
