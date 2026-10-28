# Tarefas Faltantes 



## Membro 1: (Entidade: `TB_REGIAO`)

### Tarefas Faltantes
- [x] **Criar `src/model/regiao.py`**:
  - Implementar classe `Regiao` com construtor `__init__`, atributos (`id_regiao`, `nome_regiao`, `professor_responsavel`), getters, setters e método `to_string()`.
- [x] **Implementar `src/controller/controller_regiao.py`**:
  - Preencher o arquivo (atualmente com 0 bytes) com as funções de CRUD e checagens.
- [x] **Implementar `src/sql`**:
  - arquivos de relatorios (pode usar o arquivo reports/relatorios.py como referencia)





## Membro 2: (Entidade: `TB_POKEMON`)

### Tarefas Faltantes
- [ ] **Implementar `src/controller/controller_pokemon.py`**:
  - inserção, listagem, atualização e exclusão com todas as validações necessarias.
- [ ] **Implementar `src/sql`**:
  - arquivos de relatorios (pode usar o arquivo reports/relatorios.py como referencia)

## Membro 3: (Entidade: `TB_EVOLUCAO`)

### Tarefas Faltantes
- [x] **Implementar `src/controller/controller_evolucao.py`**:
  - inserção, listagem, atualização e exclusão com todas as validações necessarias.
- [x] **Implementar `src/sql`**:
  - arquivos de relatorios (pode usar o arquivo reports/relatorios.py como referencia)
  - `relatorio_pokemons_evolucao.sql` e `relatorio_pokemons_evolucao_ult.sql`
- [x] **Padrão de exclusão segura (`src/utils/exclusao_segura.py`)**:
  - Trava de FK com opção de excluir os dependentes (item 6.c.5.i). Aplicado em Pokémon; Região, Treinador e Batalha devem usar `excluir_registro_seguro()`.



## Membro 4: (Entidade: `TB_TREINADOR` & Relatórios)

### Tarefas Faltantes
- [ ] **Implementar `src/controller/controller_treinador.py`**:
  - inserção, listagem, atualização e exclusão com todas as validações necessarias.
- [ ] **Implementar `src/sql`**:
  - arquivos de relatorios (pode usar o arquivo reports/relatorios.py como referencia)



## Membro 5:  (Integração, README & Vídeo)

### Tarefas Faltantes
- [ ] **Ajustar `src/utils/splash_screen.py`**:
  - Adicionar o nome do 6º integrante na lista de criadores da Splash Screen.
- [ ] **Complementar o `README.md`**:
  - Adicionar a instrução clara de execução no ambiente Linux:
    ```bash
    python3 src/principal.py
    ```
- [ ] **Gravar o Vídeo Demonstrativo no YouTube **:
  - Demonstrar no terminal Linux o funcionamento de todas as opções de menu (Inserir, Atualizar, Excluir com teste de trava de FK e Relatórios).
  - Subir no YouTube (Não Listado/Público) e colar o link no `README.md`.
- [ ] **Gerar arquivo `.txt` para postagem no AVA**:
  - Documento de texto contendo o link do repositório no GitHub.

---

## Membro 6: (Entidade: `TB_BATALHA`)

### Tarefas Faltantes
- [ ] **Criar e Implementar `src/controller/controller_batalha.py`**:
  - inserção, listagem, atualização e exclusão com todas as validações necessarias.
- [ ] **Implementar `src/sql`**:
  - arquivos de relatorios (pode usar o arquivo reports/relatorios.py como referencia)

