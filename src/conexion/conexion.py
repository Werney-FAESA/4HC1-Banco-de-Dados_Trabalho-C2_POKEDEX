import psycopg2
from psycopg2 import OperationalError, DatabaseError, IntegrityError
import pandas as pd
import os


class PostgresQueries:
    def __init__(self, can_write: bool = False):
        self.can_write = can_write
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = os.getenv("POSTGRES_PORT", "5432")
        self.database = os.getenv("POSTGRES_DB", "pokedex")
        self.user = os.getenv("POSTGRES_USER", "postgres")
        self.password = os.getenv("POSTGRES_PASSWORD", "password123")
        self.conn = None
        self.cur = None

    def connect(self):
        """Estabelece a conexão com o PostgreSQL com tratamento de erros."""
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cur = self.conn.cursor()
            return self.cur
        except OperationalError as e:
            print(f"\n[ERRO DE CONEXÃO] Falha ao conectar ao container PostgreSQL ({self.host}:{self.port}).")
            print(f"Certifique-se de que o container está ativo (`docker compose up -d`). Detalhes: {e}")
            raise
        except Exception as e:
            print(f"\n[ERRO INESPERADO] Falha ao abrir conexão: {e}")
            raise

    def sqlToDataFrame(self, query: str, params=None) -> pd.DataFrame:
        """Executa comandos SELECT e retorna um DataFrame do Pandas."""
        try:
            self.connect()
            self.cur.execute(query, params)
            rows = self.cur.fetchall()
            columns = [desc[0].lower() for desc in self.cur.description]
            return pd.DataFrame(rows, columns=columns)
        except DatabaseError as e:
            print(f"\n[ERRO DE CONSULTA SQL] Falha ao executar SELECT: {e}")
            return pd.DataFrame()
        finally:
            self.close()

    def write(self, query: str, params=None):
        """Executa comandos INSERT, UPDATE e DELETE sem ORM com tratamento de transação."""
        if not self.can_write:
            raise PermissionError("[PERMISSÃO] Esta instância de conexão foi aberta apenas para leitura.")
        
        try:
            self.connect()
            self.cur.execute(query, params)
            self.conn.commit()
        except IntegrityError as e:
            if self.conn:
                self.conn.rollback()
            print(f"\n[ERRO DE INTEGRIDADE] Falha nas restrições de chave/tabela: {e}")
            raise
        except DatabaseError as e:
            if self.conn:
                self.conn.rollback()
            print(f"\n[ERRO DE ESCRITA] Operação revertida (Rollback): {e}")
            raise
        finally:
            self.close()

    def executeDDL(self, query: str):
        """Executa comandos DDL (CREATE, DROP, ALTER)."""
        try:
            self.connect()
            self.cur.execute(query)
            self.conn.commit()
        except DatabaseError as e:
            if self.conn:
                self.conn.rollback()
            print(f"\n[ERRO DDL] Falha ao executar alteração estrutural: {e}")
            raise
        finally:
            self.close()

    def close(self):
        """Encerra com segurança o cursor e a conexão."""
        try:
            if self.cur and not self.cur.closed:
                self.cur.close()
            if self.conn and not self.conn.closed:
                self.conn.close()
        except Exception as e:
            print(f"[AVISO] Erro ao fechar conexão: {e}")
        finally:
            self.cur = None
            self.conn = None