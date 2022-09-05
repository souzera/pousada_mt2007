from database.connect import ConnectDataBase
from modulos.reserva.reserva import Reserva


class ReservaDAO:

    _TABLE_NAME = 'reserva'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(cliente_id, comodo_id, status) VALUES(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE ID=%d'
    _SELECT_BY_CLIENTE = f"SELECT * FROM {_TABLE_NAME} WHERE cliente_id ILIKE %s"
    _SELECT_BY_COMODO = f"SELECT * FROM {_TABLE_NAME} WHERE comodo_id ILIKE %s"
    _SELECT_BY_STATUS = f"SELECT * FROM {_TABLE_NAME} WHERE status ILIKE %s"

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    # TODO implement
        # GET_ALL
        # EXCLUDE
        # UPDATE

    def salvar(self, reserva):
        if reserva.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO,(reserva.cliente.id, reserva.comodo.id, reserva.status))
            id = cursor.fetchone()[0]
            self.database.commit()
            cursor.close()
            reserva.id = id
            return reserva
        else:
            raise Exception('Não foi possivel salvar')

    def get_all(self):
        reservas = []
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_ALL)
        all_reservas = cursor.fetchall()
        colluns_name = [desc[0] for desc in cursor.description]
        for reserva_query in all_reservas:
            data = dict(zip(colluns_name, reserva_query))
            reserva = Reserva(**data)
            reservas.append(reserva)
        cursor.close()
        return reserva