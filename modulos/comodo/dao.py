from database.connect import ConnectDataBase

class ComodoDAO:

    _TABLE_NAME = 'comodo'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(descricao, valor_diaria, status) VALUES(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_CPF = "SELECT * FROM {} WHERE cpf ILIKE '{}'"

    def __init__(self):
        self.database = ConnectDataBase().get_instance()