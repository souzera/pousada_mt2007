from database.connect import ConnectDataBase
from datetime import datetime, date

from modulos.cliente.cliente import Cliente

class ClienteDAO:

    _TABLE_NAME = 'clientes'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(nome, cpf, telefone,' \
                   f' dtNascimento, endereco, sexo) VALUES(%s, %s, %s, %s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE ID=%s'
    _SELECT_BY_CPF = "SELECT * FROM {} WHERE cpf ILIKE '{}'"

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    # TODO implement
        # EXCLUDE
        # UPDATE

    def salvar(self, cliente):
        if cliente.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (cliente.nome, cliente.cpf, cliente.endereco,
                                               cliente.telefone, cliente.dtNasc, cliente.sexo))
            id = cursor.fetchone()[0]
            self.database.commit()
            cursor.close()
            cliente.id=id
            return cliente
        else:
            raise Exception('Não foi possível salvar')

    def get_all(self):
        clientes = []
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_ALL)
        all_clientes = cursor.fetchall()
        coluns_name = [desc[0] for desc in cursor.description]
        for cliente_query in all_clientes:
            data = dict(zip(coluns_name, cliente_query))
            cliente = Cliente(**data)
            clientes.append(cliente)
        cursor.close()
        return clientes

    def get_by_id(self, id):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID, id)
        coluns_name = [desc[0] for desc in cursor.description]
        cliente_query = cursor.fetchone()
        data = dict(zip(coluns_name, cliente_query))
        cliente = Cliente(**data)
        cursor.close()
        return cliente
