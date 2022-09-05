from database.connect import ConnectDataBase
from modulos.usuario.usuario import Usuario


class UsuarioDAO:
    _TABLE_NAME = 'usuario'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(username, senha, status) VALUES(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SELECT_BY_USERNAME = "SELECT * FROM {} WHERE username ILIKE '{}'"
    _SELECT_BY_STATUS = "SELECT * FROM {} WHERE status ILIKE '{}'"

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    # TODO implement
        # GET_ALL
        # EXCLUDE
        # UPDATE

    def salvar(self, usuario):
        if usuario.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO,(usuario.username, usuario.senha, usuario.status))
            id = cursor.fetchone()[0]
            self.database.commit()
            cursor.close()
            usuario.id = id
            return usuario
        else:
            raise Exception('Não foi possivel salvar')


    def get_all(self):
        usuarios = []
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_ALL)
        all_usuarios = cursor.fetchall()
        colluns_name = [desc[0] for desc in cursor.description]
        print(colluns_name)
        for usuario_query in all_usuarios:
            data = dict(zip(colluns_name, usuario_query))
            usuario = Usuario(**data)
            usuarios.append(usuario)
        cursor.close()
        return usuarios

