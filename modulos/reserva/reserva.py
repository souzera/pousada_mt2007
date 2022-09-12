from modulos.cliente.dao import ClienteDAO
from modulos.comodo.dao import ComodoDAO

class Reserva:

    def __init__(self, checkin, checkout, cliente_id, comodo_id, status=True, id=None):
        self.id = id
        self.checkin = checkin
        self.checkout = checkout
        self.cliente_id = cliente_id
        self.comodo_id = comodo_id
        self.status = status

    def __str__(self):
        return f'Reserva {id} \n\t cliente: {self.get_cliente().nome}\n\t ' \
               f'quarto:{self.get_comodo().decricao}\n\t status:{self.status}'

    def get_data_dict(self):
        return {'id': self.id,
                'checkin': self.checkin,
                'checkout': self.checkout,
                'cliente_id': self.cliente_id,
                'comodo_id': self.comodo_id,
                'status': self.status}

    def get_cliente(self):
        dao_cliente = ClienteDAO()
        cliente = dao_cliente.get_by_id(self.cliente_id)
        return dao_cliente.get_by_id(self.cliente_id)

    def get_comodo(self):
        dao_comodo = ComodoDAO()
        return dao_comodo.get_by_id(self.comodo_id)