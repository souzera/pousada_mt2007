class Comodo:

    def __init__(self, descricao, valor_diaria, status=True, id=None):
        self.id = id
        self.descricao = descricao
        self.valor_diaria = valor_diaria
        self.status = status

    def __str__(self):
        return f'{self.descricao}\n\t diaria: {self.valor_diaria} \n\t status: {self.status}'

    def get_data_dict(self):
        return {'id': self.id,
                'descricao': self.descricao,
                'valor_diaria': self.valor_diaria,
                'status': self.status}