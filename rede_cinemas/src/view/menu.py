import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from controller.controllers import (
    CinemaController, FilmeController,
    SessaoController, RegistroPublicoController
)


def menu():
    print("\n========== REDE DE CINEMAS ==========")
    print("1. Cadastrar Cinema")
    print("2. Cadastrar Filme")
    print("3. Cadastrar Sessão")
    print("4. Registrar Público em Sessão")
    print("5. Listar Filmes em Cartaz")
    print("6. Consultar Total de Público por Sessão")
    print("7. Consultar Total de Público por Cinema")
    print("0. Sair")
    print("=====================================")
    return input("Opção: ").strip()


def run():
    cinema_ctrl = CinemaController()
    filme_ctrl = FilmeController()
    sessao_ctrl = SessaoController()
    publico_ctrl = RegistroPublicoController()

    while True:
        opcao = menu()

        if opcao == "1":
            print("\n--- Cadastrar Cinema ---")
            nome = input("Nome: ")
            endereco = input("Endereço: ")
            cidade = input("Cidade: ")
            estado = input("Estado (UF): ")
            capacidade = input("Capacidade: ")
            res = cinema_ctrl.cadastrar(nome, endereco, cidade, estado, capacidade)
            print(f"\n[{'OK' if res['sucesso'] else 'ERRO'}] {res['mensagem']}")

        elif opcao == "2":
            print("\n--- Cadastrar Filme ---")
            titulo = input("Título: ")
            duracao = input("Duração (minutos): ")
            genero = input("Gênero: ")
            sinopse = input("Sinopse: ")
            diretor_id = input("ID do Diretor: ")
            res = filme_ctrl.cadastrar(titulo, duracao, genero, sinopse, diretor_id)
            print(f"\n[{'OK' if res['sucesso'] else 'ERRO'}] {res['mensagem']}")

        elif opcao == "3":
            print("\n--- Cadastrar Sessão ---")
            cinemas = cinema_ctrl.listar()
            if not cinemas:
                print("Nenhum cinema cadastrado.")
                continue
            print("Cinemas disponíveis:")
            for c in cinemas:
                print(f"  [{c.id}] {c.nome} — {c.cidade}/{c.estado}")
            cinema_id = input("ID do Cinema: ")

            filmes = filme_ctrl.listar()
            if not filmes:
                print("Nenhum filme cadastrado.")
                continue
            print("Filmes disponíveis:")
            for f in filmes:
                print(f"  [{f.id}] {f.titulo} ({f.duracao_min} min)")
            filme_id = input("ID do Filme: ")

            data = input("Data (AAAA-MM-DD): ")
            horario = input("Horário (HH:MM): ")
            sala = input("Sala: ")
            res = sessao_ctrl.cadastrar(int(cinema_id), int(filme_id), data, horario, sala)
            print(f"\n[{'OK' if res['sucesso'] else 'ERRO'}] {res['mensagem']}")

        elif opcao == "4":
            print("\n--- Registrar Público ---")
            sessao_id = input("ID da Sessão: ")
            quantidade = input("Quantidade de público: ")
            res = publico_ctrl.registrar(int(sessao_id), int(quantidade))
            print(f"\n[{'OK' if res['sucesso'] else 'ERRO'}] {res['mensagem']}")

        elif opcao == "5":
            print("\n--- Filmes em Cartaz ---")
            cinemas = cinema_ctrl.listar()
            if not cinemas:
                print("Nenhum cinema cadastrado.")
                continue
            for c in cinemas:
                print(f"  [{c.id}] {c.nome}")
            cinema_id = input("ID do Cinema: ")
            sessoes = sessao_ctrl.listar_por_cinema(int(cinema_id))
            if not sessoes:
                print("Nenhuma sessão encontrada.")
            else:
                print(f"\n{'ID':<5} {'Filme':<30} {'Data':<12} {'Horário':<8} {'Sala'}")
                print("-" * 65)
                for s in sessoes:
                    print(f"{s[0]:<5} {s[6]:<30} {s[3]:<12} {s[4]:<8} {s[5]}")

        elif opcao == "6":
            print("\n--- Total de Público por Sessão ---")
            sessao_id = input("ID da Sessão: ")
            res = publico_ctrl.total_por_sessao(int(sessao_id))
            print(f"Total de público: {res['total']}")

        elif opcao == "7":
            print("\n--- Total de Público por Cinema ---")
            cinemas = cinema_ctrl.listar()
            if not cinemas:
                print("Nenhum cinema cadastrado.")
                continue
            for c in cinemas:
                print(f"  [{c.id}] {c.nome}")
            cinema_id = input("ID do Cinema: ")
            res = publico_ctrl.total_por_cinema(int(cinema_id))
            print(f"Total de público: {res['total']}")

        elif opcao == "0":
            print("Saindo... Ate mais!")
            break

        else:
            print("Opção inválida.")