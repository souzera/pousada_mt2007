from database.connect import ConnectDataBase
from modulos.comodo.comodo import Comodo

class ComodoDAO:

    _TABLE_NAME = 'comodos'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}(descricao, valor_diaria, status) VALUES(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = f'SELECT * FROM {_TABLE_NAME} WHERE ID=%s'
    _DELETE_BY_ID = f'DELETE FROM {_TABLE_NAME} WHERE ID=%s'
    _DISABLE_BY_ID = f'UPDATE {_TABLE_NAME} SET status=false WHERE ID=%s'
    _UPDATE_BY_ID = f'UPDATE {_TABLE_NAME} SET descricao= %s, valor_diaria=%s, status=%s WHERE id=%s'

    def __init__(self):
        self.database = ConnectDataBase().get_instance()

    #TODO implement
        # EXCLUDE
        # UPDATE

    def salvar(self, comodo):
        if comodo.id is None:
            cursor = self.database.cursor()
            cursor.execute(self._INSERT_INTO, (comodo.descricao, comodo.valor_diaria, comodo.status))
            id = cursor.fetchone()[0]
            self.database.commit()
            cursor.close()
            comodo.id = id
            return comodo
        else:
            raise Exception('Não foi possivel salvar')

    def get_all(self):
        comodos = []
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_ALL)
        all_comodos = cursor.fetchall()
        colluns_name = [desc[0] for desc in cursor.description]
        for comodo_query in all_comodos:
            data = dict(zip(colluns_name, comodo_query))
            comodo = Comodo(**data)
            comodos.append(comodo)
        cursor.close()
        return comodos

    def get_by_id(self, id):
        cursor = self.database.cursor()
        cursor.execute(self._SELECT_BY_ID, id)
        colluns_name =[desc[0] for desc in cursor.description]
        comodo_query = cursor.fetchone()
        data = dict(zip(colluns_name, comodo_query))
        comodo = Comodo(**data)
        cursor.close()
        return comodo

    def delete_by_id(self, id):
        comodo_desc = self.get_by_id(id).descricao
        cursor = self.database.cursor()
        cursor.execute(self._DELETE_BY_ID, id)
        self.database.commit()
        cursor.close()
        return f'{comodo_desc} foi excluído(a).'

    def disable_by_id(self, id):
        comodo_desc = self.get_by_id(id).descricao
        cursor = self.database.cursor()
        cursor.execute(self._DISABLE_BY_ID, id)
        self.database.commit()
        cursor.close()
        return f'{comodo_desc} foi desativado(a).'

    def update_by_id(self, comodo):
        cursor = self.database.cursor()
        cursor.execute(self._UPDATE_BY_ID, (comodo.descricao, comodo.valor_diaria, comodo.status, str(comodo.id)))
        self.database.commit()
        cursor.close()
        return self.get_by_id(str(comodo.id))
