from database.connect import ConnectDataBase

class ComodoDAO:

    _TABLE_NAME = 'comodo'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(descricao, valor_diaria, status) VALUES(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_CPF = "SELECT * FROM {} WHERE cpf ILIKE '{}'"

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    #TODO implement
        # GET_ALL
        # EXCLUDE
        # UPDATE

    def salvar(self, comodo):
        if comodo.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (comodo.decricao, comodo.valor_diaria, comodo.status))
            id = cursor.fetchone()[0]
            self.database.commit()
            cursor.close()
            comodo.id = id
            return comodo
        else:
            raise Exception('Não foi possivel salvar')