import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime, timedelta
from repository.repositories import (
    SessaoRepository, RegistroPublicoRepository,
    CinemaRepository, FilmeRepository, DiretorRepository
)


class CinemaService:
    def __init__(self):
        self.repo = CinemaRepository()

    def listar(self):
        return self.repo.listar()

    def cadastrar(self, nome, endereco, cidade, estado, capacidade):
        return self.repo.salvar(nome, endereco, cidade, estado, int(capacidade))


class FilmeService:
    def __init__(self):
        self.repo = FilmeRepository()
        self.diretor_repo = DiretorRepository()

    def listar(self):
        return self.repo.listar()

    def cadastrar(self, titulo, duracao_min, genero, sinopse, nome_diretor):
        diretor_id = self.diretor_repo.salvar(nome_diretor)
        return self.repo.salvar(titulo, int(duracao_min), genero, sinopse, diretor_id)


class SessaoService:
    def __init__(self):
        self.repo = SessaoRepository()
        self.filme_repo = FilmeRepository()

    def cadastrar(self, cinema_id, filme_id, data, horario, sala):
        sessoes_existentes = self.repo.buscar_sessoes_por_sala_e_data(sala, data)
        novo_inicio = datetime.strptime(horario, "%H:%M")

        filme = self.filme_repo.buscar_por_id(filme_id)
        if not filme:
            raise ValueError("Filme não encontrado.")

        novo_fim = novo_inicio + timedelta(minutes=filme.duracao_min + 30)

        for s in sessoes_existentes:
            inicio_existente = datetime.strptime(s.horario, "%H:%M")
            filme_s = self.filme_repo.buscar_por_id(s.filme_id)
            fim_existente = inicio_existente + timedelta(minutes=filme_s.duracao_min + 30)

            if not (novo_fim <= inicio_existente or novo_inicio >= fim_existente):
                raise ValueError(f"Conflito de horário na sala '{sala}' com sessão existente às {s.horario}.")

        id = self.repo.salvar(cinema_id, filme_id, data, horario, sala)
        return id

    def listar_por_cinema(self, cinema_id):
        return self.repo.listar_por_cinema(cinema_id)


class RegistroPublicoService:
    def __init__(self):
        self.repo = RegistroPublicoRepository()

    def registrar(self, sessao_id, quantidade):
        from datetime import date
        from database import get_connection

        conn = get_connection()
        row = conn.execute(
            "SELECT c.capacidade FROM sessao s JOIN cinema c ON s.cinema_id = c.id WHERE s.id = ?",
            (sessao_id,)
        ).fetchone()
        conn.close()

        if not row:
            raise ValueError("Sessão não encontrada.")

        capacidade = row[0]
        total_atual = self.repo.total_por_sessao(sessao_id)

        if total_atual + quantidade > capacidade:
            raise ValueError(
                f"Público excede a capacidade do cinema ({capacidade}). "
                f"Já registrado: {total_atual}."
            )

        data_hoje = date.today().isoformat()
        id = self.repo.salvar(sessao_id, data_hoje, quantidade)
        return id

    def total_por_sessao(self, sessao_id):
        return self.repo.total_por_sessao(sessao_id)

    def total_por_cinema(self, cinema_id):
        return self.repo.total_por_cinema(cinema_id)