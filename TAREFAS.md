# 👥 Divisão de Trabalho da Equipe (5 Integrantes) - Projeto Pokédex

> **Disciplina:** Banco de Dados — FAESA | **Professor:** Howard Roatti  
> **Tema:** Pokédex  
 


---

## 📌 Quadro Resumo de Responsabilidades

| Integrante | Papel Principal | Entidades / Módulos em Foco | Entregáveis Específicos |
| :--- | :--- | :--- | :--- |
| **Membro 1** | Arquiteto de BD & Backend | `TB_REGIAO` + Conexão com o BD | Diagrama Relacional, DDLs SQL e `controller_regiao.py` |
| **Membro 2** | Desenvolvedor Backend | `TB_POKEMON` | `controller_pokemon.py` |
| **Membro 3** | Desenvolvedor Backend & Regras | `TB_EVOLUCAO` + Trava de Integridade | `controller_evolucao.py` e lógica de FK na exclusão (item 6.c.5.i) |
| **Membro 4** | Especialista em SQL & Backend | `TB_TREINADOR` + Módulo de Relatórios | `controller_treinador.py`, `relatorios.py` (GROUP BY e JOINs) |
| **Membro 5** | Líder de Integração & QA | Menu Principal + README & Vídeo | `principal.py`, `config.py`, README Linux e Vídeo no YouTube |
| **Membro 6** | Desenvolvedor Backend & Regras | `TB_BATALHA` + Validações Cruzadas | `controller_batalha.py`, `model/batalha.py` e testes de integridade |

---

## 🔍 Detalhamento por Integrante

---

### 👤 Membro 1: BD & Backend (Entidade: Região)
**Foco:** Modelagem do Banco de Dados, scripts SQL fundamentais, conexão e CRUD de Regiões.

#### Tarefas:
1. **Diagrama Relacional**:
   - Criar o modelo no **Mermaid** (ou software equivalente).
   - Especificar tabelas, atributos, tipos, chaves primárias, chaves estrangeiras, obrigatoriedades e cardinalidades.
   - Exportar o diagrama em **PDF**, **PNG** ou **JPEG** para a pasta `diagrama/`.
2. **Scripts SQL DDL (`sql/create_tables.sql` e `sql/drop_tables.sql`)**:
   - Escrever o script SQL com criação de todas as tabelas e constraints.
   - Configurar as `SEQUENCES` caso utilizem Oracle (ou `AUTO_INCREMENT`/`SERIAL` no MySQL/PostgreSQL).
   - Criar script de carga inicial de teste (`sql/inserts_iniciais.sql`).
3. **Módulo de Conexão (`src/connection/conexion.py`)**:
   - Implementar a conexão com o banco de dados sem ORM, com tratamento de erros.
4. **Model e Controller da Região**:
   - Criar `src/model/regiao.py` com atributos, getters, setters e método `to_string()`.
   - Criar `src/controller/controller_regiao.py`:
     - `inserir_regiao()`: valida se já existe, insere e confirma.
     - `atualizar_regiao()`: lista registros, seleciona PK, altera atributos atômicos e exibe o resultado.
     - `excluir_regiao()`: lista registros, verifica se há Pokémons associados (trava de FK) antes de excluir.
     - `verifica_existencia()`: consulta se a região existe no banco.

---

### 👤 Membro 2: Backend (Entidade: Pokémon) & Splash Screen
**Foco:** Entidade central do sistema (Pokémon) e tela de inicialização dinâmica.

#### Tarefas:
1. **Model do Pokémon (`src/model/pokemon.py`)**:
   - Atributos: `id_pokemon`, `nome`, `tipo_primario`, `tipo_secundario`, `nivel_base`, e **objeto associado `regiao: Regiao`** (exigência explícita do edital: conter a instância e não apenas o ID).
   - Getters, setters e método `to_string()`.
2. **Controller do Pokémon (`src/controller/controller_pokemon.py`)**:
   - `inserir_pokemon()`: valida se o ID não existe, lista as regiões existentes para o usuário selecionar uma válida, insere no banco.
   - `atualizar_pokemon()`: lista os Pokémons, escolhe por PK, atualiza dados atômicos e exibe o registro atualizado.
   - `excluir_pokemon()`: lista os Pokémons, verifica se o Pokémon é chave estrangeira em `TB_EVOLUCAO` antes de permitir excluir.
   - `verifica_existencia()`: método de consulta por ID.


---

### 👤 Membro 3: Backend (Entidade: Evolução) & Regras de Exclusão FK
**Foco:** Entidade de relacionamento complexo (Evolução) e conformidade rigorosa com integridade referencial.

#### Tarefas:
1. **Model de Evolução (`src/model/evolucao.py`)**:
   - Atributos: `a definir`.
   - Getters, setters e método `to_string()`.
2. **Controller de Evolução (`src/controller/controller_evolucao.py`)**:
   - `inserir_evolucao()`: permite escolher o Pokémon base e a evolução resultante, checando se ambos existem e validando integridade.
   - `atualizar_evolucao()`: altera os requisitos de evolução (nível, pedra de evolução, etc.).
   - `excluir_evolucao()`: remove o registro com confirmação.
3. **Padrão de Exclusão Segura**:
   - Revisar e padronizar o comportamento de exclusão em todas as controladoras:
     - Quando o usuário tentar deletar uma tupla pai que tem dependentes (ex: Região com Pokémons, ou Pokémon com Evoluções):
       - O sistema deve detectar a restrição e alertar claramente: *"Não é possível excluir o registro pois ele possui registros dependentes em outra tabela."*
       - Opcionalmente oferecer: *"Deseja excluir primeiro os registros dependentes vinculados? (S/N)"*.

---

### 👤 Membro 4: SQL & Backend (Entidade: Treinador & Relatórios)
**Foco:** Entidade Treinador e os Relatórios Avançados com Agrupamento e Junções SQL.

#### Tarefas:
1. **Model e Controller de Treinador (`src/model/treinador.py` e `src/controller/controller_treinador.py`)**:
   - Atributos: `a definir`.
   - CRUD completo (inserir, listar, atualizar e excluir).
2. **Relatórios SQL (`sql/relatorios.sql` e `src/reports/relatorios.py`)**:
   - **Relatório 1 (Sumarização / Agrupamento)**:
     - Consulta SQL utilizando `GROUP BY` e funções agregadas (`COUNT`, `AVG`, `MAX`).
     - *Exemplo:* Quantidade de Pokémons e média de nível agrupados por Região e Tipo.
   - **Relatório 2 (Junção de Tabelas / JOIN)**:
     - Consulta SQL utilizando `INNER JOIN` / `LEFT JOIN` entre 3 ou mais tabelas.
     - *Exemplo:* Relatório de Linhagens Evolutivas: exibe Pokémon inicial, para quem evolui, nível de evolução e a Região nativa.
3. **Formatação dos Relatórios no Console**:
   - Exibir os resultados de forma limpa, alinhada e tabular no terminal.

---

### 👤 Membro 5: Líder de Integração, Interface Principal, README Linux & Vídeo
**Foco:** Orquestração da aplicação, navegação contínua, documentação no GitHub e gravação do vídeo.

#### Tarefas:
1. **Menu Principal e Navegação (`principal.py` e `src/utils/config.py`)**:
   - Implementar o fluxo do menu com as 5 opções obrigatórias:
     1. Relatórios
     2. Inserir Registros
     3. Remover Registros
     4. Atualizar Registros
     5. Sair
   - Submenus de seleção de entidade para Inserção, Atualização e Remoção.
   - Implementar a navegação em loop: sempre perguntar se deseja realizar outra operação e retornar ao menu correto sem fechar o programa inesperadamente.
   - Limpeza de tela multiplataforma (`clear` no Linux, `cls` no Windows).
2. **Documentação Linux no `README.md`**:
   - Explicar passo a passo como clonar, instalar dependências no Linux (`apt`, `python3-pip`, `venv`).
   - Como configurar as credenciais do banco e executar os scripts DDL.
   - Como rodar o sistema (`python3 principal.py`).
3. **Vídeo Demonstrativo no YouTube**:
   - Gravar a tela executando o sistema do início ao fim:
     - Splash Screen inicial com nomes e contagens.
     - Navegação em todos os menus.
     - Inserção com sucesso.
     - Atualização com exibição do antes/depois.
     - Exclusão com demonstração da trava de chave estrangeira (FK).
     - Execução e visualização dos dois Relatórios (Agrupamento e Junção).
   - Subir no YouTube (Não Listado ou Público) e inserir o link no `README.md`.
4. **Entrega no AVA**:
   - Gerar o arquivo `.txt` com o link do repositório no GitHub para postagem no AVA.

---

### 👤 Membro 6: Desenvolvedor Backend (Entidade: Batalha) & Validações Cruzadas
**Foco:** Entidade de histórico de combate (`TB_BATALHA`), integridade de múltiplas chaves estrangeiras e testes de fluxo.

#### Tarefas:
1. **Model de Batalha (`src/model/batalha.py`)**:
   - Atributos: `a definir`.
   -- CRUD completo (inserir, listar, atualizar e excluir).
2. **Controller de Batalha (`src/controller/controller_batalha.py`)**:
   - `inserir_batalha()`: lista os treinadores cadastrados, valida se o desafiante e o desafiado são distintos (`treinador_1 != treinador_2`), define vencedor e grava com transação no banco.
   - `atualizar_batalha()`: permite ajustar local, data ou vencedor caso haja empate/revisão.
   - `excluir_batalha()`: remove o registro com confirmação do usuário.
   - `verifica_existencia()`: checagem de existência por ID.
3. **Validação de Integridade Referencial Mútua**:
   - Garantir que a tabela `TB_TREINADOR` não possa ser excluída sem aviso caso o treinador participe de uma batalha (trava de FK complementar ao trabalho do Membro 3).


---





