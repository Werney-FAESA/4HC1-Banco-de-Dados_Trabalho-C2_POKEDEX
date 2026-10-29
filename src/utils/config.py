MENU_PRINCIPAL = """Menu Principal:
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Menu Relatórios
1 - Relatorio de Batalhas
2 - Relatorio de Pokémons - ultima evolução
3 - Relatorio de pokémons - todas evoluçoes 
4 - Relatorio de pokemons - quantidade por região
5 - Relatorio de pokemons - quantidade por tipo
6 - Relatorio de pokemons
7 - Relatorio de regiões - quantidade de pokémons por região
8 - Relatorio de regiões
9 - Relatorio de tabelas - quantidade de registros por tabela
10 - Relatorio de treinadores
11 - Relatorio de treinadores por região (quantidade, idade média e maior idade)
0 - Voltar ao menu principal
"""

MENU_ENTIDADES = """Entidades
1 - Batalhas
2 - Evoluções
3 - Pokémons
4 - Regiões
5 - Treinadores.
"""

QUERY_COUNT = 'select count(1) as total from {tabela}'

def clear_console(wait_time: int = 3):
    import os
    from time import sleep

    sleep(wait_time)
    os.system('clear')