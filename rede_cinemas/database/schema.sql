CREATE TABLE IF NOT EXISTS diretor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ator (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS filme (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    duracao_min INTEGER NOT NULL,
    genero TEXT NOT NULL,
    sinopse TEXT,
    diretor_id INTEGER NOT NULL,
    FOREIGN KEY (diretor_id) REFERENCES diretor(id)
);

CREATE TABLE IF NOT EXISTS filme_ator (
    filme_id INTEGER NOT NULL,
    ator_id INTEGER NOT NULL,
    PRIMARY KEY (filme_id, ator_id),
    FOREIGN KEY (filme_id) REFERENCES filme(id),
    FOREIGN KEY (ator_id) REFERENCES ator(id)
);

CREATE TABLE IF NOT EXISTS cinema (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    capacidade INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS sessao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cinema_id INTEGER NOT NULL,
    filme_id INTEGER NOT NULL,
    data TEXT NOT NULL,
    horario TEXT NOT NULL,
    sala TEXT NOT NULL,
    FOREIGN KEY (cinema_id) REFERENCES cinema(id),
    FOREIGN KEY (filme_id) REFERENCES filme(id)
);

CREATE TABLE IF NOT EXISTS registro_publico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sessao_id INTEGER NOT NULL,
    data_registro TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (sessao_id) REFERENCES sessao(id)
);