from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_batalha import Controller_Batalha
from controller.controller_evolucao import Controller_Evolucao
from controller.controller_pokemon import Controller_Pokemon
from controller.controller_regiao import Controller_Regiao
from controller.controller_treinador import Controller_Treinador

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_batalha = Controller_Batalha()
ctrl_evolucao = Controller_Evolucao()
ctrl_pokemon = Controller_Pokemon()
ctrl_regiao = Controller_Regiao()
ctrl_treinador = Controller_Treinador()


def reports(opcao_relatorio:int=0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_batalhas()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_pokemons_evolucao_ult()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_pokemons_evolucao()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_pokemons_quant_regiao()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_pokemons_quant_tipo()
    elif opcao_relatorio == 6:
        relatorio.get_relatorio_pokemons()
    elif opcao_relatorio == 7:
        relatorio.get_relatorio_regiao_quant_pokemons()
    elif opcao_relatorio == 8:
        relatorio.get_relatorio_regiao()
    elif opcao_relatorio == 9:
        relatorio.get_relatorio_tabelas_quant()
    elif opcao_relatorio == 10:
        relatorio.get_relatorio_treinadores()


def inserir(opcao_inserir:int=0):
    if opcao_inserir == 1:
        novo_batalha = ctrl_batalha.inserir_batalha()
    elif opcao_inserir == 2:
        novo_evolucao = ctrl_evolucao.inserir_evolucao()
    elif opcao_inserir == 3:
        novo_pokemon = ctrl_pokemon.inserir_pokemon()
    elif opcao_inserir == 4:
        novo_regiao = ctrl_regiao.inserir_regiao()
    elif opcao_inserir == 5:
        novo_treinador = ctrl_treinador.inserir_treinador()



def atualizar(opcao_atualizar:int=0):
    if opcao_atualizar == 1:
        relatorio.get_relatorio_batalhas()
        batalha_atualizado = ctrl_batalha.atualizar_batalha()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_pokemons_evolucao_ult()
        evolucao_atualizado = ctrl_evolucao.atualizar_evolucao()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_pokemons()
        pokemon_atualizado = ctrl_pokemon.atualizar_pokemon()
    elif opcao_atualizar == 4:
        relatorio.get_relatorio_regiao()
        regiao_atualizado = ctrl_regiao.atualizar_regiao()
    elif opcao_atualizar == 5:
        relatorio.get_relatorio_treinadores()
        treinador_atualizado = ctrl_treinador.atualizar_treinador()


def remover(opcao_excluir:int=0):
    if opcao_excluir == 1:
        relatorio.get_relatorio_batalhas()
        ctrl_batalha.excluir_batalha()
    elif opcao_excluir == 2:
        relatorio.get_relatorio_pokemons_evolucao_ult()
        ctrl_evolucao.excluir_evolucao()
    elif opcao_excluir == 3:
        relatorio.get_relatorio_pokemons()
        ctrl_pokemon.excluir_pokemon()
    elif opcao_excluir == 4:
        relatorio.get_relatorio_regiao()
        ctrl_regiao.excluir_regiao()
    elif opcao_excluir == 5:
        relatorio.get_relatorio_treinadores()
        ctrl_treinador.excluir_treinador()


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = input("Escolha uma opção: ")
        config.clear_console(1)

        if opcao == "1": # relatorios
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção: "))
            config.clear_console(1)

            reports(opcao_relatorio)
            config.clear_console(1)

        elif opcao == "2": # inserir registros
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção: "))
            config.clear_console(1)

            inserir(opcao_inserir = opcao_inserir)
            config.clear_console(1)

            print(tela_inicial.get_updated_screen())
            config.clear_console(1)


        elif opcao == "3": # atualizar registros
            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção: "))
            config.clear_console(1)

            atualizar(opcao_atualizar = opcao_atualizar)
            config.clear_console(1)

        elif opcao == "4": # remover registros
            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção: "))
            config.clear_console(1)

            remover(opcao_excluir = opcao_excluir)
            config.clear_console(1)

            print(tela_inicial.get_updated_screen())
            config.clear_console(1)

        elif opcao == "5": # sair
            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("obrigado por utilizar a POKEDEX!")
            exit(0)

        else:
            print("Opção inválida.")
            exit(1)

if __name__ == "__main__":
    run()

























































