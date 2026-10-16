# 🚀 Passo 1: Definição de Tabelas e Diagramas (Guia Rápido por Membro)

> **Objetivo:** Definir as tabelas da Pokédex, criar os diagramas em formato Mermaid (`.mmd`) e imagens, e gerar os trechos SQL individuais.  
> **Padrão de Branch no Git:** `primeiro-passo-tabelas-e-diagrama-membro-X`  
> **Local dos Entregáveis:** Criar uma pasta com o seu nome dentro de `diagramas/` (ex: `diagramas/nome_do_membro/`).

---

## 📌 Regras Gerais para Todos os Membros

1. Criar e entrar na sua branch individual:
   ```bash
   git checkout -b primeiro-passo-tabelas-e-diagrama-membro-X
   ```
2. Criar a pasta com seu nome dentro de `diagramas/`:
   ```bash
   mkdir diagramas/seu_nome
   ```
3. Salvar seus entregáveis dentro dessa pasta:
   * Diagrama da sua parte em arquivo **`.mmd`** (código Mermaid).
   * Imagem exportada do diagrama (**`.png`** ou **`.pdf`**).
   * Arquivo **`.sql`** com o comando `CREATE TABLE` da sua tabela e exemplos de `INSERT`.
4. Fazer commit e push para o repositório:
   ```bash
   git add .
   git commit -m "feat(etapa-1): definicao da tabela e diagrama - membro X"
   git push origin primeiro-passo-tabelas-e-diagrama-membro-X
   ```

---

## 👤 Membro 1 — Tabelas `TB_REGIAO` e `TB_LOCALIZACAO`

* **Tabela:** `TB_REGIAO`
* **Colunas a especificar:** `ID_REGIAO` (PK),...outros que achar necessario.
* **Tabela:** `TB_LOCALIZACAO`
* **Colunas a especificar:** `ID_LOCALIZACAO` (PK), `ID_REGIAO` (FK para `TB_REGIAO`), `NOME_LOCALIZACAO` e outros atributos que achar necessario.
* Cada localização deve pertencer a uma região, e um Pokémon deverá ser vinculado a uma localização, não diretamente a uma região.
* **Entregáveis na pasta `diagramas/membro_1/` (ou com seu nome):**
  1. `diagrama_regiao_localizacao.mmd` (código Mermaid dos modelos de região e localização, incluindo o relacionamento entre eles).
  2. `diagrama_regiao_localizacao.png` (ou `.pdf`).
  3. `tb_regiao.sql` (comando de criação e 3 inserts de exemplo: Kanto, Johto, Hoenn).
  4. `tb_localizacao.sql` (comando de criação com a FK para `TB_REGIAO` e inserts de locais de exemplo).
  5. Suporte ao diagrama relacional global no SQL Power Architect.
* **Branch Git:** `primeiro-passo-tabelas-e-diagrama-membro-1`

---

## 👤 Membro 2 — Tabela `TB_POKEMON` e Diagrama

* **Tabela:** `TB_POKEMON`
* **Colunas a especificar:** `ID_POKEMON` (PK), `ID_LOCALIZACAO` (FK para `TB_LOCALIZACAO`) ... outros que achar necessario.
* **Entregáveis na pasta `diagramas/membro_2/` (ou com seu nome):**
  1. `diagrama_pokemon.mmd` (código Mermaid mostrando `TB_POKEMON` e a FK para `TB_LOCALIZACAO`).
  2. `diagrama_pokemon.png` (ou `.pdf`).
  3. `tb_pokemon.sql` (comando de criação com a constraint(restrições) FK e 6 inserts de Pokémons clássicos).
* **Branch Git:** `primeiro-passo-tabelas-e-diagrama-membro-2`

---

## 👤 Membro 3 — Tabela `TB_EVOLUCAO` e Diagrama

* **Tabela:** `TB_EVOLUCAO`
* **Colunas a especificar:** `ID_EVOLUCAO` (PK), `ID_POKEMON_ORIGEM` (FK -> `TB_POKEMON`), `ID_POKEMON_DESTINO` (FK -> `TB_POKEMON`), `NIVEL_NECESSARIO` (NULL), `METODO_EVOLUCAO` (NOT NULL).
* **Entregáveis na pasta `diagramas/membro_3/` (ou com seu nome):**
  1. `diagrama_evolucao.mmd` (código Mermaid mostrando as duas conexões com `TB_POKEMON`).
  2. `diagrama_evolucao.png` (ou `.pdf`).
  3. `tb_evolucao.sql` (comando de criação com as duas FKs e 3 regras de evolução de teste).
  4. Pequena anotação em texto com a regra de proteção: não permitir deletar Pokémon que esteja nesta tabela.
* **Branch Git:** `primeiro-passo-tabelas-e-diagrama-membro-3`

---

## 👤 Membro 4 — Tabela `TB_TREINADOR` e Dados Iniciais

* **Tabela:** `TB_TREINADOR`
* **Colunas a especificar:** `ID_TREINADOR` (PK), ... e outros que achar necessario.
* **Entregáveis na pasta `diagramas/membro_4/` (ou com seu nome):**
  1. `diagrama_treinador.mmd` (código Mermaid da entidade treinador).
  2. `diagrama_treinador.png` (ou `.pdf`).
  3. `tb_treinador.sql` (comando de criação e 3 inserts: Ash, Gary, Misty).
  4. `inserts_completos.sql` (compilado preliminar com dados de teste para todas as tabelas).
* **Branch Git:** `primeiro-passo-tabelas-e-diagrama-membro-4`

---

## 👤 Membro 5 — Padronização, Script Unificado e Diagrama Geral

* **Papel:** Líder de Integração do Banco e Repositório.
* **Entregáveis na pasta `diagramas/membro_5/` (ou com seu nome):**
  1. `padroes_banco.md` (regras aprovadas: nomes das colunas, tipos e SGBD escolhido).
  2. `diagrama_geral_completo.mmd` (Mermaid com todas as tabelas definidas e seus relacionamentos).
  3. `diagrama_geral_completo.png` (ou `.pdf`).
  4. Revisão e montagem dos scripts finais unificados: `sql/create_tables.sql` e `sql/drop_tables.sql`.
* **Branch Git:** `primeiro-passo-tabelas-e-diagrama-membro-5`

---

## 👤 Membro 6 — Tabela `TB_BATALHA` e Diagrama

* **Tabela:** `TB_BATALHA`
* **Colunas a especificar:** `ID_BATALHA`, `ID_TREINADOR_1` ... outros que achar necessário.
* **Entregáveis na pasta `diagramas/membro_6/` (ou com seu nome):**
  1. `diagrama_batalha.mmd` (código Mermaid mostrando `TB_BATALHA` e as conexões FK com `TB_TREINADOR`).
  2. `diagrama_batalha.png` (ou `.pdf`).
  3. `tb_batalha.sql` (comando `CREATE TABLE` com constraints de PK e FKs, e 3 inserts de batalhas de teste).
  4. Mapeamento(anotação em texto) de regra de exclusão: trava para impedir exclusão de Treinador que tenha histórico em `TB_BATALHA`.
* **Branch Git:** `primeiro-passo-tabelas-e-diagrama-membro-6`