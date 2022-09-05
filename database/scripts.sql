CREATE TABLE IF NOT EXISTS clientes(
	id serial PRIMARY KEY,
	nome varchar(255),
	cpf varchar(32),
	telefone varchar(32),
	dtNasc date,
	endereco varchar(255)
);

select * from clientes;