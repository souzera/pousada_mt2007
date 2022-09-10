class Reserva:

    def __init__(self, checkin, checkout, cliente, comodo, status, id=None):
        self.id = id
        self.checkin = checkin
        self.checkout = checkout
        self.cliente = cliente
        self.comodo = comodo
        self.status = status

    def __str__(self):
        return f'Reserva {id} \n\t cliente: {self.cliente.nome}\n\t ' \
               f'quarto:{self.comodo.decricao}\n\t status:{self.status}'

    def get_data_dict(self):
        return {'id': self.id,
                'checkin': self.checkin,
                'checkout': self.checkout,
                'cliente': self.cliente.get_data_dict(),
                'comodo': self.comodo.get_data_dict(),
                'status': self.status}