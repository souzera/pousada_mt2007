# Pousada Marea Turbo 2007

### Tema: 

API para Hotel/Pousada

### Objetivos:

Projeto construído para servir de base para construção de aplicação para auxiliar na gestão de uma pousada/hotel

### Principais Funcionalidades

* Clientes:
  * Cadastrar Cliente
  * Listar Clientes
  * Buscar Cliente

* Comodos:
  * Listar Comodos
  * Verificar Comodo
  * Ver Comodo

* Reserva:
  * Buscar Reserva
  * Incluir Reserva
  * Cancelar Reserva
  * Alterar Reserva

* Usuario:
  * Cadastro
  * Alterar Senha
  * Desativar
  * Excluir

### Como foi desenvolvido?

O projeto foi desenvolvido em python utilizando o banco de dados Postgresql. Além disso foram feito utilizadas as bibliotecas pycopgg2 e flask também tive auxilio da ferramenta Postman para realizar os teste durante o desenvolvimento.

### Como foi implementado?

O Projeto foi implementado na forma de uma API Rest, na qual cada requisição irá retornar um formato JSON. Cada rota irá retornar os dados de acordo com a entidade, os dados podem ser usados da forma mais pertinente de acordo com cada método.
