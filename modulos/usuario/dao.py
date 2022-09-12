from database.connect import ConnectDataBase
from modulos.usuario.usuario import Usuario


class UsuarioDAO:
    _TABLE_NAME = 'usuarios'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(username, senha, status) VALUES(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE ID=%s'
    _DELETE_BY_ID = f'DELETE FROM {_TABLE_NAME} WHERE ID=%s'

    def __init__(self):
        self.database = ConnectDataBase().get_instance()


    # TODO implement
        # EXCLUDE
        # UPDATE

    def salvar(self, usuario):

        if self.get_all_username().__contains__(usuario.username):
            raise Exception('Usuario já existe')

        if usuario.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (usuario.username, usuario.senha, usuario.status))
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

    def get_by_id(self, id):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID, id)
        colluns_name = [desc[0] for desc in cursor.description]
        usuario_query = cursor.fetchone()
        data = dict(zip(colluns_name, usuario_query))
        usuario = Usuario(**data)
        cursor.close()
        return usuario

    def get_all_username(self):
        usernames = []
        for user in self.get_all():
            usernames.append(user.username)
        return usernames






























    # -=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-= #
    def validar_senha(self, hashed):
        if bcrypt.hashpw(password, hashed) == hashed:
            return True
        else:
            return False
    # -=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-= #