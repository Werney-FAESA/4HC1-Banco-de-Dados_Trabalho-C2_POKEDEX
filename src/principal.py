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


def reports(opcao_relatorio: int = 0):
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
    elif opcao_relatorio == 11:
        relatorio.get_relatorio_treinadores_por_regiao()
    elif opcao_relatorio == 12:
        relatorio.get_relatorio_batalhas_vitorias()


def inserir(opcao_inserir: int = 0):
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


def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        batalha_atualizado = ctrl_batalha.atualizar_batalha()
    elif opcao_atualizar == 2:
        evolucao_atualizado = ctrl_evolucao.atualizar_evolucao()
    elif opcao_atualizar == 3:
        pokemon_atualizado = ctrl_pokemon.atualizar_pokemon()
    elif opcao_atualizar == 4:
        regiao_atualizado = ctrl_regiao.atualizar_regiao()
    elif opcao_atualizar == 5:
        treinador_atualizado = ctrl_treinador.atualizar_treinador()


def remover(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        ctrl_batalha.excluir_batalha()
    elif opcao_excluir == 2:
        ctrl_evolucao.excluir_evolucao()
    elif opcao_excluir == 3:
        ctrl_pokemon.excluir_pokemon()
    elif opcao_excluir == 4:
        ctrl_regiao.excluir_regiao()
    elif opcao_excluir == 5:
        ctrl_treinador.excluir_treinador()


def _continuar(acao: str) -> bool:
    resposta = input(f"\nDeseja {acao} mais algum registro? (S/N): ").strip().upper()
    return resposta in {"S", "SIM"}


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = input("Escolha uma opção: ").strip()
        config.clear_console(1)

        if opcao == "1":  # relatorios
            print(config.MENU_RELATORIOS)
            try:
                opcao_relatorio = int(input("Escolha uma opção: ").strip())
            except ValueError:
                print("Opção inválida.")
                config.clear_console(1)
                continue
            config.clear_console(1)

            reports(opcao_relatorio)
            config.clear_console(1)

        elif opcao == "2":  # inserir registros
            while True:
                print(config.MENU_ENTIDADES)
                try:
                    opcao_inserir = int(input("Escolha uma opção: ").strip())
                except ValueError:
                    print("Opção inválida.")
                    config.clear_console(1)
                    break
                config.clear_console(1)

                inserir(opcao_inserir=opcao_inserir)
                config.clear_console(1)

                if opcao_inserir == 2 or not _continuar("inserir"):
                    break

            print(tela_inicial.get_updated_screen())
            config.clear_console(1)

        elif opcao == "3":  # atualizar registros
            while True:
                print(config.MENU_ENTIDADES)
                try:
                    opcao_atualizar = int(input("Escolha uma opção: ").strip())
                except ValueError:
                    print("Opção inválida.")
                    config.clear_console(1)
                    break
                config.clear_console(1)

                atualizar(opcao_atualizar=opcao_atualizar)
                config.clear_console(1)

                if opcao_atualizar == 2 or not _continuar("atualizar"):
                    break

            print(tela_inicial.get_updated_screen())
            config.clear_console(1)

        elif opcao == "4":  # remover registros
            while True:
                print(config.MENU_ENTIDADES)
                try:
                    opcao_excluir = int(input("Escolha uma opção: ").strip())
                except ValueError:
                    print("Opção inválida.")
                    config.clear_console(1)
                    break
                config.clear_console(1)

                remover(opcao_excluir=opcao_excluir)
                config.clear_console(1)

                if opcao_excluir == 2 or not _continuar("excluir"):
                    break

            print(tela_inicial.get_updated_screen())
            config.clear_console(1)

        elif opcao == "5":  # sair
            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("obrigado por utilizar a POKEDEX!")
            exit(0)

        else:
            print("Opção inválida.")
            config.clear_console(1)


if __name__ == "__main__":
    run()
