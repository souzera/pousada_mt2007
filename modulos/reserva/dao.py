from database.connect import ConnectDataBase
from modulos.reserva.reserva import Reserva


class ReservaDAO:

    _TABLE_NAME = 'reservas'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(checkin, checkout, cliente_id, comodo_id, status) ' \
                   f'VALUES(%s, %s, %s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE ID=%s'
    _DELETE_BY_ID = f'DELETE FROM {_TABLE_NAME} WHERE ID=%s'
    _DISABLE_BY_ID = f'UPDATE {_TABLE_NAME} SET status=false WHERE id=%s'
    _UPDATE_BY_ID = f'UPDATE {_TABLE_NAME} SET checkin=%s, checkout=%s, cliente_id=%s, comodo_id=%s, status=%s ' \
                        f'WHERE id=%s'

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    # TODO implement
        # GET_ALL
        # EXCLUDE
        # UPDATE

    def salvar(self, reserva):
        if reserva.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (reserva.checkin, reserva.checkout, reserva.cliente_id,
                                              reserva.comodo_id, reserva.status))
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
        return reservas

    def get_by_id(self, id):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID, id)
        colluns_name = [desc[0] for desc in cursor.description]
        reserva_query = cursor.fetchone()
        data = dict(zip(colluns_name, reserva_query))
        reserva = Reserva(**data)
        cursor.close()
        return reserva

    def delete_by_id(self, id):
        reserva_id = self.get_by_id(id).id
        cursor = self.database.cursor()
        cursor.execute(self._DELETE_BY_ID, id)
        self.database.commit()
        cursor.close()
        return f'A Reserva {reserva_id} foi excluída.'

    def disable_by_id(self, id):
        reserva_id = self.get_by_id(id).id
        cursor = self.database.cursor()
        cursor.execute(self._DISABLE_BY_ID, id)
        self.database.commit()
        cursor.close()
        return f'A Reserva {reserva_id} foi desativada.'

    def update_by_id(self, reserva):
        cursor = self.database.cursor()
        cursor.execute(self._UPDATE_BY_ID, (reserva.checkin, reserva.checkout, reserva.cliente_id,
                                            reserva.comodo_id, reserva.status, reserva.id))
        self.database.commit()
        cursor.close()
        return self.get_by_id(str(reserva.id))