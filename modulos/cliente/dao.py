from database.connect import ConnectDataBase

from modulos.cliente.cliente import Cliente

class ClienteDAO:

    _TABLE_NAME = 'clientes'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(nome, cpf, telefone,' \
                   f' dtnasc, endereco, sexo) VALUES(%s, %s, %s, %s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE ID=%s'
    _DELETE_BY_ID = f'DELETE FROM {_TABLE_NAME} WHERE ID=%s'
    _DISABLE_BY_ID = f'UPDATE {_TABLE_NAME} SET status=false WHERE id=%s'
    _UPDATE_BY_ID = f'UPDATE {_TABLE_NAME} SET nome=%s, cpf=%s, telefone=%s, dtnasc=%s, endereco=%s, sexo=%s' \
                    f'WHERE id=%s'

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    # TODO implement
        # UPDATE

    def salvar(self, cliente):
        if cliente.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (cliente.nome, cliente.cpf, cliente.telefone,
                                               cliente.dtnasc, cliente.endereco, cliente.sexo))
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
        colluns_name = [desc[0] for desc in cursor.description]
        cliente_query = cursor.fetchone()
        data = dict(zip(colluns_name, cliente_query))
        cliente = Cliente(**data)
        cursor.close()
        return cliente

    def delete_by_id(self, id):
        cliente_name = self.get_by_id(id).nome
        cursor = self.database.cursor()
        cursor.execute(self._DELETE_BY_ID, id)
        self.database.commit()
        cursor.close()
        return f'{cliente_name} foi excluído(a).'

    def disable_by_id(self, id):
        cliente_name = self.get_by_id(id).nome
        cursor = self.database.cursor()
        cursor.execute(self._DISABLE_BY_ID, str(id))
        self.database.commit()
        cursor.close()
        return f'{cliente_name} foi desativado(a).'

    def update_by_id(self, cliente):
        cursor = self.database.cursor()
        cursor.execute(self._UPDATE_BY_ID, (cliente.nome, cliente.cpf, cliente.telefone,
                                            cliente.dtnasc, cliente.endereco, cliente.sexo, cliente.id))
        self.database.commit()
        cursor.close()
        return self.get_by_id(str(cliente.id))

