class Usuario:

    def __init__(self, username, senha, status):
        self.username = username
        self.senha = senha
        self.status = status

    def __str__(self):
        return f'{self.username}\n\t status: {self.status}'

    def get_data_dict(self):
        return {'id': self.id,
                'username': self.username,
                'senha': self.senha,
                'status': self.status}