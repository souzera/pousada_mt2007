class Cliente:

    def __init__(self, nome, cpf, telefone, dtnasc, endereco, sexo, id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.dtnasc = dtnasc
        self.endereco = endereco
        self.sexo = sexo

    def __str__(self):
        return f'Nome: {self.nome}\n\t Telefone: {self.telefone}\n\t' \
               f'Endereço: {self.endereco}'

    def get_data_dict(self):
        return {'id': self.id,
                'nome': self.nome,
                'cpf': self.cpf,
                'telefone': self.telefone,
                'dtnasc': str(self.dtnasc),
                'endereco': self.endereco,
                'sexo': self.sexo}