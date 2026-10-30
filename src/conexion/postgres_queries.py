###########################################################################
# Adaptado para PostgreSQL a partir do código do Prof. Howard Roatti
#
# Essa classe auxilia na conexão com o Banco de Dados PostgreSQL
###########################################################################
import os
import json
try:
    import psycopg2
except ImportError:
    import psycopg as psycopg2
from pandas import DataFrame

class PostgresQueries:
    _active_port = None

    def __init__(self, can_write: bool = False, database: str = "pokedex"):
        self.can_write = can_write
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = int(os.getenv("POSTGRES_PORT", "5432"))
        self.database = os.getenv("POSTGRES_DB", database)
        self.conn = None
        self.cur = None

        # Procura o arquivo de autenticação tanto relativo ao projeto quanto relativo ao arquivo atual
        base_dir = os.path.dirname(__file__)
        possible_paths = [
            os.path.join(base_dir, "passphrase", "authentication.postgres"),
            "src/conexion/passphrase/authentication.postgres",
            "conexion/passphrase/authentication.postgres",
            os.path.join(base_dir, "passphrase", "authentication.oracle"),
        ]

        auth_path = next((p for p in possible_paths if os.path.exists(p)), None)

        if auth_path:
            with open(auth_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                self.user, self.passwd = [part.strip() for part in content.split(",", 1)]
        else:
            self.user = os.getenv("POSTGRES_USER", "postgres")
            self.passwd = os.getenv("POSTGRES_PASSWORD", "password123")

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
        ports_to_try = (
            [PostgresQueries._active_port]
            if PostgresQueries._active_port is not None
            else [self.port, 5433] if int(self.port) == 5432 else [int(self.port)]
        )
        last_error = None
        for port in ports_to_try:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    port=port,
                    dbname=self.database,
                    user=self.user,
                    password=self.passwd
                )
                self.conn.autocommit = True
                self.cur = self.conn.cursor()
                self.port = port
                PostgresQueries._active_port = port
                return self.cur
            except (psycopg2.OperationalError, UnicodeDecodeError) as e:
                last_error = e

        raise RuntimeError(
            f"Não foi possível conectar ao PostgreSQL em {self.host} (portas tentadas: {ports_to_try}). "
            "Verifique se o container Docker 'pokedex_db' está ativo (`docker compose up -d`)."
        ) from last_error

    def sqlToDataFrame(self, query: str, params=None) -> DataFrame:
        '''
        Esse método irá executar uma query
        Parameters:
        - query: consulta utilizada para recuperação dos dados
        return: um DataFrame da biblioteca Pandas
        '''
        if self.cur is None:
            self.connect()
        self.cur.execute(query, params)
        rows = self.cur.fetchall()
        columns = [col[0].lower() for col in self.cur.description]
        return DataFrame(rows, columns=columns)

    def sqlToMatrix(self, query: str, params=None) -> tuple:
        '''
        Esse método irá executar uma query
        Parameters:
        - query: consulta utilizada para recuperação dos dados
        return: uma matriz (lista de listas), uma lista com os nomes das colunas(atributos) da(s) tabela(s)
        '''
        if self.cur is None:
            self.connect()
        self.cur.execute(query, params)
        rows = self.cur.fetchall()
        matrix = [list(row) for row in rows]
        columns = [col[0].lower() for col in self.cur.description]
        return matrix, columns

    def sqlToJson(self, query: str, params=None):
        '''
        Esse método irá executar uma query
        Parameters:
        - query: consulta utilizada para recuperação dos dados
        return: um objeto json
        '''
        if self.cur is None:
            self.connect()
        self.cur.execute(query, params)
        columns = [col[0].lower() for col in self.cur.description]
        rows = [dict(zip(columns, row)) for row in self.cur.fetchall()]
        return json.dumps(rows, default=str)

    def write(self, query: str, params=None):
        if not self.can_write:
            raise Exception("Can't write using this connection")

        if self.cur is None:
            self.connect()
        self.cur.execute(query, params)
        self.conn.commit()

    def executeDDL(self, query: str, params=None):
        '''
        Esse método irá executar o comando DDL enviado no atributo query
        Parameters:
        - query: consulta utilizada para comandos DDL
        '''
        if self.cur is None:
            self.connect()
        self.cur.execute(query, params)
        self.conn.commit()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

# Alias para facilitar caso algum script tente importar OracleQueries
OracleQueries = PostgresQueries
