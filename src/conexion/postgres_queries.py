###########################################################################
# Adaptado para PostgreSQL a partir do código do Prof. Howard Roatti
#
# Essa classe auxilia na conexão com o Banco de Dados PostgreSQL
###########################################################################
import os
import json
import psycopg as psycopg2
from pandas import DataFrame

class PostgresQueries:

    def __init__(self, can_write: bool = False, database: str = "db_faesa"):
        self.can_write = can_write
        self.host = "localhost"
        self.port = 5432
        self.database = database
        self.conn = None
        self.cur = None

        # Procura o arquivo de autenticação tanto relativo ao projeto quanto relativo ao arquivo atual
        auth_path = "conexion/passphrase/authentication.postgres"
        if not os.path.exists(auth_path):
            base_dir = os.path.dirname(__file__)
            auth_path = os.path.join(base_dir, "passphrase", "authentication.postgres")
            if not os.path.exists(auth_path):
                # Fallback caso ainda esteja usando o arquivo do oracle
                auth_path = os.path.join(base_dir, "passphrase", "authentication.oracle")

        with open(auth_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            self.user, self.passwd = content.split(",")

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass

    def connect(self):
        '''
        Esse método realiza a conexão com o banco de dados PostgreSQL
        return: um cursor que permite utilizar as funções da biblioteca psycopg2
        '''
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.database,
            user=self.user,
            password=self.passwd
        )
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        return self.cur

    def sqlToDataFrame(self, query: str) -> DataFrame:
        '''
        Esse método irá executar uma query
        Parameters:
        - query: consulta utilizada para recuperação dos dados
        return: um DataFrame da biblioteca Pandas
        '''
        self.cur.execute(query)
        rows = self.cur.fetchall()
        columns = [col[0].lower() for col in self.cur.description]
        return DataFrame(rows, columns=columns)

    def sqlToMatrix(self, query: str) -> tuple:
        '''
        Esse método irá executar uma query
        Parameters:
        - query: consulta utilizada para recuperação dos dados
        return: uma matriz (lista de listas), uma lista com os nomes das colunas(atributos) da(s) tabela(s)
        '''
        self.cur.execute(query)
        rows = self.cur.fetchall()
        matrix = [list(row) for row in rows]
        columns = [col[0].lower() for col in self.cur.description]
        return matrix, columns

    def sqlToJson(self, query: str):
        '''
        Esse método irá executar uma query
        Parameters:
        - query: consulta utilizada para recuperação dos dados
        return: um objeto json
        '''
        self.cur.execute(query)
        columns = [col[0].lower() for col in self.cur.description]
        rows = [dict(zip(columns, row)) for row in self.cur.fetchall()]
        return json.dumps(rows, default=str)

    def write(self, query: str):
        if not self.can_write:
            raise Exception("Can't write using this connection")

        self.cur.execute(query)
        self.conn.commit()

    def executeDDL(self, query: str):
        '''
        Esse método irá executar o comando DDL enviado no atributo query
        Parameters:
        - query: consulta utilizada para comandos DDL
        '''
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

# Alias para facilitar caso algum script tente importar OracleQueries
OracleQueries = PostgresQueries