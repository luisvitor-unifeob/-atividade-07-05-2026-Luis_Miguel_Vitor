import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database import get_connection
from model.models import Cinema, Filme, Sessao, RegistroPublico


class CinemaRepository:
    def listar(self):
        conn = get_connection()
        rows = conn.execute("SELECT * FROM cinema").fetchall()
        conn.close()
        return [Cinema(*row) for row in rows]

    def buscar_por_id(self, id):
        conn = get_connection()
        row = conn.execute("SELECT * FROM cinema WHERE id = ?", (id,)).fetchone()
        conn.close()
        return Cinema(*row) if row else None

    def salvar(self, nome, endereco, cidade, estado, capacidade):
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO cinema (nome, endereco, cidade, estado, capacidade) VALUES (?,?,?,?,?)",
            (nome, endereco, cidade, estado, capacidade)
        )
        conn.commit()
        id = cur.lastrowid
        conn.close()
        return id


class DiretorRepository:
    def salvar(self, nome):
        conn = get_connection()
        cur = conn.execute("INSERT INTO diretor (nome) VALUES (?)", (nome,))
        conn.commit()
        id = cur.lastrowid
        conn.close()
        return id


class FilmeRepository:
    def listar(self):
        conn = get_connection()
        rows = conn.execute("SELECT * FROM filme").fetchall()
        conn.close()
        return [Filme(*row) for row in rows]

    def buscar_por_id(self, id):
        conn = get_connection()
        row = conn.execute("SELECT * FROM filme WHERE id = ?", (id,)).fetchone()
        conn.close()
        return Filme(*row) if row else None

    def salvar(self, titulo, duracao_min, genero, sinopse, diretor_id):
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO filme (titulo, duracao_min, genero, sinopse, diretor_id) VALUES (?,?,?,?,?)",
            (titulo, duracao_min, genero, sinopse, diretor_id)
        )
        conn.commit()
        id = cur.lastrowid
        conn.close()
        return id


class SessaoRepository:
    def buscar_sessoes_por_sala_e_data(self, sala, data):
        conn = get_connection()
        rows = conn.execute(
            "SELECT * FROM sessao WHERE sala = ? AND data = ?", (sala, data)
        ).fetchall()
        conn.close()
        return [Sessao(*row) for row in rows]

    def salvar(self, cinema_id, filme_id, data, horario, sala):
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO sessao (cinema_id, filme_id, data, horario, sala) VALUES (?,?,?,?,?)",
            (cinema_id, filme_id, data, horario, sala)
        )
        conn.commit()
        id = cur.lastrowid
        conn.close()
        return id

    def listar_por_cinema(self, cinema_id):
        conn = get_connection()
        rows = conn.execute(
            """SELECT s.*, f.titulo FROM sessao s
               JOIN filme f ON s.filme_id = f.id
               WHERE s.cinema_id = ?""", (cinema_id,)
        ).fetchall()
        conn.close()
        return rows


class RegistroPublicoRepository:
    def salvar(self, sessao_id, data_registro, quantidade):
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO registro_publico (sessao_id, data_registro, quantidade) VALUES (?,?,?)",
            (sessao_id, data_registro, quantidade)
        )
        conn.commit()
        id = cur.lastrowid
        conn.close()
        return id

    def total_por_sessao(self, sessao_id):
        conn = get_connection()
        row = conn.execute(
            "SELECT SUM(quantidade) FROM registro_publico WHERE sessao_id = ?", (sessao_id,)
        ).fetchone()
        conn.close()
        return row[0] or 0

    def total_por_cinema(self, cinema_id):
        conn = get_connection()
        row = conn.execute(
            """SELECT SUM(rp.quantidade) FROM registro_publico rp
               JOIN sessao s ON rp.sessao_id = s.id
               WHERE s.cinema_id = ?""", (cinema_id,)
        ).fetchone()
        conn.close()
        return row[0] or 0