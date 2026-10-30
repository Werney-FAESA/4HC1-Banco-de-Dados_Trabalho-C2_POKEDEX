try:
    import psycopg2
    from psycopg2 import OperationalError, DatabaseError, IntegrityError
except ImportError:
    import psycopg as psycopg2
    from psycopg import OperationalError, DatabaseError, IntegrityError
import pandas as pd
import os


class PostgresQueries:
    _active_port = None

    def __init__(self, can_write: bool = False, database: str = "pokedex"):
        self.can_write = can_write
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = os.getenv("POSTGRES_PORT", "5432")
        self.database = os.getenv("POSTGRES_DB", database)

        base_dir = os.path.dirname(__file__)
        auth_path = os.path.join(base_dir, "passphrase", "authentication.postgres")
        if os.path.exists(auth_path):
            with open(auth_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                user_file, pass_file = [part.strip() for part in content.split(",", 1)]
        else:
            user_file, pass_file = "postgres", "password123"

        self.user = os.getenv("POSTGRES_USER", user_file)
        self.password = os.getenv("POSTGRES_PASSWORD", pass_file)
        self.conn = None
        self.cur = None

    def connect(self):
        """Estabelece a conexão com o PostgreSQL com tratamento de erros e fallback de porta."""
        ports_to_try = (
            [PostgresQueries._active_port]
            if PostgresQueries._active_port is not None
            else [int(self.port), 5433] if int(self.port) == 5432 else [int(self.port)]
        )
        last_error = None
        for port in ports_to_try:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    port=port,
                    dbname=self.database,
                    user=self.user,
                    password=self.password
                )
                self.cur = self.conn.cursor()
                self.port = port
                PostgresQueries._active_port = port
                return self.cur
            except (OperationalError, UnicodeDecodeError) as e:
                last_error = e
            except Exception as e:
                print(f"\n[ERRO INESPERADO] Falha ao abrir conexão: {e}")
                raise

        print(f"\n[ERRO DE CONEXÃO] Falha ao conectar ao container PostgreSQL ({self.host}, portas {ports_to_try}).")
        print("Certifique-se de que o container está ativo (`docker compose up -d`).")
        if last_error:
            raise last_error

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
