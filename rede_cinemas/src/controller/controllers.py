import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from service.services import SessaoService, RegistroPublicoService, CinemaService, FilmeService


class CinemaController:
    def __init__(self):
        self.service = CinemaService()

    def listar(self):
        return self.service.listar()

    def cadastrar(self, nome, endereco, cidade, estado, capacidade):
        try:
            id = self.service.cadastrar(nome, endereco, cidade, estado, capacidade)
            return {"sucesso": True, "mensagem": f"Cinema cadastrado com sucesso! ID: {id}"}
        except Exception as e:
            return {"sucesso": False, "mensagem": str(e)}


class FilmeController:
    def __init__(self):
        self.service = FilmeService()

    def listar(self):
        return self.service.listar()

    def cadastrar(self, titulo, duracao_min, genero, sinopse, diretor_id):
        try:
            id = self.service.cadastrar(titulo, duracao_min, genero, sinopse, diretor_id)
            return {"sucesso": True, "mensagem": f"Filme cadastrado com sucesso! ID: {id}"}
        except Exception as e:
            return {"sucesso": False, "mensagem": str(e)}


class SessaoController:
    def __init__(self):
        self.service = SessaoService()

    def cadastrar(self, cinema_id, filme_id, data, horario, sala):
        try:
            id = self.service.cadastrar(cinema_id, filme_id, data, horario, sala)
            return {"sucesso": True, "mensagem": f"Sessão cadastrada com sucesso! ID: {id}"}
        except ValueError as e:
            return {"sucesso": False, "mensagem": str(e)}

    def listar_por_cinema(self, cinema_id):
        return self.service.listar_por_cinema(cinema_id)


class RegistroPublicoController:
    def __init__(self):
        self.service = RegistroPublicoService()

    def registrar(self, sessao_id, quantidade):
        try:
            id = self.service.registrar(sessao_id, quantidade)
            return {"sucesso": True, "mensagem": f"Público registrado com sucesso! ID: {id}"}
        except ValueError as e:
            return {"sucesso": False, "mensagem": str(e)}

    def total_por_sessao(self, sessao_id):
        total = self.service.total_por_sessao(sessao_id)
        return {"total": total}

    def total_por_cinema(self, cinema_id):
        total = self.service.total_por_cinema(cinema_id)
        return {"total": total}