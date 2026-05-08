class Cinema:
    def __init__(self, id, nome, endereco, cidade, estado, capacidade):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.capacidade = capacidade

    def __repr__(self):
        return f"Cinema(id={self.id}, nome='{self.nome}', cidade='{self.cidade}')"


class Filme:
    def __init__(self, id, titulo, duracao_min, genero, sinopse, diretor_id):
        self.id = id
        self.titulo = titulo
        self.duracao_min = duracao_min
        self.genero = genero
        self.sinopse = sinopse
        self.diretor_id = diretor_id

    def __repr__(self):
        return f"Filme(id={self.id}, titulo='{self.titulo}')"


class Sessao:
    def __init__(self, id, cinema_id, filme_id, data, horario, sala):
        self.id = id
        self.cinema_id = cinema_id
        self.filme_id = filme_id
        self.data = data
        self.horario = horario
        self.sala = sala

    def __repr__(self):
        return f"Sessao(id={self.id}, data='{self.data}', horario='{self.horario}')"


class RegistroPublico:
    def __init__(self, id, sessao_id, data_registro, quantidade):
        self.id = id
        self.sessao_id = sessao_id
        self.data_registro = data_registro
        self.quantidade = quantidade

    def __repr__(self):
        return f"RegistroPublico(sessao_id={self.sessao_id}, quantidade={self.quantidade})"