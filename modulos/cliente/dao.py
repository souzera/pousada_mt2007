from database.connect import ConnectDataBase
from modulos.cliente.cliente import Cliente

class ClienteDAO:

    _TABLE_NAME = 'cliente'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(nome, cpf, telefone,' \
                   f' dtNascimento, endereco, sexo) VALUES(%s, %s, %s, %s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_CPF = "SELECT * FROM {} WHERE cpf ILIKE '{}'"

    def __init__(self):
        self.database = ConnectDataBase.get_instance()

    # TODO implement
        # EXCLUDE
        # UPDATE

    def salvar(self, cliente):
        if cliente.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (cliente.nome, cliente.cpf, cliente.endereco, cliente.telefone, cliente.dtNascimento, cliente.sexo))
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