# 4HC1-Banco-de-Dados_Trabalho-C2_POKEDEX

Sistema de gerenciamento de Pokédex via terminal (CLI) integrado ao banco de dados **PostgreSQL** via Docker, utilizando `psycopg2` e `pandas` (sem ORM).

---

## 🎥 Vídeo de Demonstração (YouTube)

- **Link do vídeo:** *([(https://youtu.be/7AE_30qgB7E)](https://youtu.be/7AE_30qgB7E))*

---

## 🚀 Passo a Passo para Executar o Projeto

### 1. Preparar o Ambiente e Instalar Dependências

**No Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

**No Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

---

### 2. Iniciar o Banco de Dados (PostgreSQL via Docker)

Suba o container do PostgreSQL em segundo plano:

```bash
sudo docker compose up -d
sudo docker compose ps
```
*(No Windows com Docker Desktop, não é necessário usar `sudo`: `docker compose up -d`)*

O serviço `db` (`pokedex_db`) será iniciado na porta `5432` e executará automaticamente os scripts de criação de tabelas (`sql/create_tables.sql`) e carga inicial de dados (`sql/inserts_iniciais.sql`).

---

### 3. Executar a Aplicação no Terminal

A partir da raiz do projeto, execute:

**No Linux / macOS:**
```bash
python3 src/principal.py
```

**No Windows:**
```powershell
python src/principal.py
```

---

## 🔍 Validação Rápida da Conexão (Opcional)

Para testar uma consulta diretamente no banco `pokedex`:

```bash
python3 -c "from src.conexion.conexion import PostgresQueries; print(PostgresQueries().sqlToDataFrame('SELECT * FROM tb_pokemon LIMIT 5').to_string(index=False))"
```

As configurações padrão (`localhost:5432`, banco `pokedex`, usuário `postgres`, senha `password123`) também podem ser sobrescritas pelas variáveis de ambiente `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_USER` e `POSTGRES_PASSWORD`.

---

## 🛠️ Exemplos de Uso da Camada de Conexão

Consultas recebem parâmetros separados do SQL (`%s`), garantindo segurança contra SQL Injection:

```python
from src.conexion.conexion import PostgresQueries

db = PostgresQueries()
try:
    resultado = db.sqlToDataFrame(
        "SELECT * FROM tb_pokemon WHERE nome_pokemon = %s",
        ("Pikachu",),
    )
finally:
    db.close()
```

Para operações de escrita (`INSERT`, `UPDATE`, `DELETE`), habilite `can_write=True`:

```python
db = PostgresQueries(can_write=True)
try:
    db.write(
        "UPDATE tb_pokemon SET nivel_base = %s WHERE id_pokemon = %s",
        (15, 25),
    )
finally:
    db.close()
```

---

### Encerrar o Banco de Dados

Quando terminar de utilizar a aplicação:

```bash
docker compose down
```
