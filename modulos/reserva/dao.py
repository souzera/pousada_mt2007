from database.connect import ConnectDataBase

class ReservaDAO:

    _TABLE_NAME = 'reserva'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(cliente_id, comodo_id, status) VALUES(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_CLIENTE = "SELECT * FROM {} WHERE cliente_id ILIKE '{}'"
    _SELECT_BY_COMODO = "SELECT * FROM {} WHERE comodo_id ILIKE '{}'"

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    # TODO implement
        # GET_ALL
        # SAVE
        # EXCLUDE
        # UPDATE