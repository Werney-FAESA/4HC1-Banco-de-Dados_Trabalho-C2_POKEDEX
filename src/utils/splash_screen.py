from conexion.postgres_queries import PostgresQueries
from utils import config


class SplashScreen:

    def __init__(self):
        # consultas de contagem de registros - inicio
        self.qry_total_batalhas = config.QUERY_COUNT.format(tabela='TB_BATALHA')
        self.qry_total_evolucao = config.QUERY_COUNT.format(tabela='TB_EVOLUCAO')
        self.qry_total_pokemons = config.QUERY_COUNT.format(tabela='TB_POKEMON')
        self.qry_total_regioes = config.QUERY_COUNT.format(tabela='TB_REGIAO')
        self.qry_total_treinadores = config.QUERY_COUNT.format(tabela='TB_TREINADOR')
        # consultas de contagem de registros - fim


        #nomes dos criadores
        self.created_by0 = "Bruno Mauro Bayer Laiber"
        self.created_by1 = "Daniel Lima Del'Antonio"
        self.created_by2 = "Gabriel Antônio Galdino dos Santos"
        self.created_by3 = "Issacar Mattos Gutler"
        self.created_by4 = "Kaike Vaccari do Nascimento"
        self.created_by5 = "Werney Ferreira Rocha"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2026/2"

    def get_total_batalhas(self):
        postgres = PostgresQueries()
        postgres.connect()
        return postgres.sqlToDataFrame(self.qry_total_batalhas)["total"].values[0]

    def get_total_evolucao(self):
        postgres = PostgresQueries()
        postgres.connect()
        return postgres.sqlToDataFrame(self.qry_total_evolucao)["total"].values[0]

    def get_total_pokemons(self):
        postgres = PostgresQueries()
        postgres.connect()
        return postgres.sqlToDataFrame(self.qry_total_pokemons)["total"].values[0]

    def get_total_regioes(self):
        postgres = PostgresQueries()
        postgres.connect()
        return postgres.sqlToDataFrame(self.qry_total_regioes)["total"].values[0]

    def get_total_treinadores(self):
        postgres = PostgresQueries()
        postgres.connect()
        return postgres.sqlToDataFrame(self.qry_total_treinadores)["total"].values[0]


    def get_updated_screen(self):
        return f"""
        ################################################################################
        #                            POKEDEX
        #
        # TOTAL DE REGISTROS:
        #     1 - BATALHAS:                 {str(self.get_total_batalhas()).rjust(5)}
        #     2 - EVOLUÇÃO:                 {str(self.get_total_evolucao()).rjust(5)}
        #     3 - POKEMONS:                 {str(self.get_total_pokemons()).rjust(5)}
        #     4 - REGIÕES:                  {str(self.get_total_regioes()).rjust(5)}
        #     5 - TREINADORES:              {str(self.get_total_treinadores()).rjust(5)}
        #
        # CRIADO POR: {self.created_by0}
        #             {self.created_by1}
        #             {self.created_by2}
        #             {self.created_by3}
        #             {self.created_by4}
        #             {self.created_by5}
        #
        # PROFESSOR: {self.professor}
        #
        # DISCIPLINA: {self.disciplina}
        #             {self.semestre}
        ################################################################################
        """











