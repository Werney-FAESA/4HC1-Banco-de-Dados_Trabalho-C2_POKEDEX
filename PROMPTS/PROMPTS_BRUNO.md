# Registro de uso de IA - Membro 3 (Bruno Mauro Bayer Laiber)

Este arquivo registra o uso de IA como apoio ao desenvolvimento, conforme o item
(5) das Observações Importantes do edital. Todo o código foi revisado e deve ser
compreendido pelo integrante antes da entrega e da apresentação.

## Registro 1 - CRUD de Evolução, relatórios de evolução e exclusão segura

- **Data:** 27/10/2026
- **Fonte:** Claude (Anthropic) — claude.ai
- **Prompt utilizado:**

  > "https://github.com/Werney-FAESA/4HC1-Banco-de-Dados_Trabalho-C2_POKEDEX.git
  > sou o membro 3 e faça o que deve ser feito do membro 3 e crie um branch e poste nela."
  >
  > (junto do PDF do edital do trabalho C2)

- **O que a IA fez:**
  - Leu o edital, o `TAREFAS.md` e o `TAREFAS_FALTANTES.md` para identificar as
    tarefas do Membro 3.
  - Implementou `src/controller/controller_evolucao.py` (inserir, listar,
    atualizar e excluir), seguindo o mesmo padrão da controladora de Pokémon
    (SQL escrito à mão, sem ORM, valores passados como parâmetros do psycopg2).
  - Criou `src/utils/exclusao_segura.py`, o padrão de exclusão com trava de FK
    (item 6.c.5.i): confirma, verifica dependentes e oferece excluir os
    registros das tabelas filhas numa única transação.
  - Aplicou esse padrão na exclusão de Pokémon.
  - Criou os SQLs `src/sql/relatorio_pokemons_evolucao.sql` e
    `src/sql/relatorio_pokemons_evolucao_ult.sql` (consultas com JOIN).
  - Ajustou o `to_string()` de `src/model/evolucao.py`.
  - Testou tudo num PostgreSQL local com `sql/create_tables.sql` e
    `sql/inserts_iniciais.sql`.

- **O que o grupo fez com a resposta:** revisar cada consulta SQL, rodar o
  sistema no PostgreSQL do grupo (docker compose) e entender os métodos antes de
  apresentar.

### Pontos para entender antes da apresentação

- **Validações na inserção:** os dois Pokémons precisam existir; base e evoluído
  não podem ser o mesmo; o par base → evoluído não pode se repetir; com o modo
  "Nível" o nível é obrigatório (1 a 100).
- **ID da evolução:** é sugerido `MAX(id_evolucao) + 1`, mas o usuário pode
  digitar outro; sempre é verificado se o ID já existe (integridade de entidade).
- **Exclusão segura:** o mapa `DEPENDENCIAS` em `exclusao_segura.py` espelha as
  FKs do `create_tables.sql`. A exclusão em cascata é recursiva e roda dentro de
  uma transação: se algo falhar, é feito `rollback` e nada é apagado.
- **Fluxo contínuo (itens 6.b.5, 6.c.6, 6.d.8):** depois de cada operação a
  controladora pergunta se o usuário deseja continuar na mesma entidade.
