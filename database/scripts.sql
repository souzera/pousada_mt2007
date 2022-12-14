CREATE TABLE IF NOT EXISTS usuarios(
    id serial PRIMARY KEY,
    username varchar(32),
    senha varchar(32),
    status bool
);

CREATE TABLE IF NOT EXISTS clientes(
	id serial PRIMARY KEY,
	nome varchar(255),
	cpf varchar(32),
	telefone varchar(32),
	dtNasc date,
	endereco varchar(255),
	sexo char(1) CHECK (sexo in ('m', 'f')));

ALTER TABLE clientes ADD IF NOT EXISTS status bool NULL ;

CREATE TABLE IF NOT EXISTS comodos(
    id serial PRIMARY KEY,
    descricao varchar(255),
    valor_diaria float,
    status bool
);

CREATE TABLE IF NOT EXISTS reservas(
    id serial PRIMARY KEY,
	checkin date,
	checkout date,
    cliente_id int references clientes(id),
    comodo_id int references comodos(id),
    status bool
);

select * from clientes;
