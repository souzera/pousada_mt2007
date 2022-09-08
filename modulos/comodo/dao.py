from database.connect import ConnectDataBase
from modulos.comodo.comodo import Comodo

class ComodoDAO:

    _TABLE_NAME = 'comodo'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(descricao, valor_diaria, status) VALUES(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_CPF = "SELECT * FROM {} WHERE cpf ILIKE '{}'"

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    #TODO implement
        # EXCLUDE
        # UPDATE

    def salvar(self, comodo):
        if comodo.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (comodo.descricao, comodo.valor_diaria, comodo.status))
            id = cursor.fetchone()[0]
            self.database.commit()
            cursor.close()
            comodo.id = id
            return comodo
        else:
            raise Exception('Não foi possivel salvar')

    def get_all(self):
        comodos = []
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_ALL)
        all_comodos = cursor.fetchall()
        colluns_name = [desc[0] for desc in cursor.description]
        for comodo_query in all_comodos:
            data = dict(zip(colluns_name, comodo_query))
            comodo = Comodo(**data)
            comodos.append(comodo)
        cursor.close()
        return comodos