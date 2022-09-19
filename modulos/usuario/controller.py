from flask import jsonify, make_response, Blueprint, request

from modulos.usuario.dao import UsuarioDAO
from modulos.usuario.usuario import Usuario

app_usuario = Blueprint('usuario_blueprint', __name__)
app_name = 'usuario'
dao_usuario = UsuarioDAO()

@app_usuario.route(f'/{app_name}/', methods=['GET'])
def get_usuarios():
    usuarios = dao_usuario.get_all()
    data = [usuario.get_data_dict() for usuario in usuarios]
    return make_response(jsonify(data))

@app_usuario.route(f'/{app_name}/add', methods=['POST'])
def save_usuario():
    data = request.get_json()
    usuario = Usuario(**data)
    if dao_usuario.salvar(usuario):
        return make_response(jsonify(data))
    return 404

@app_usuario.route(f'/{app_name}/<id>', methods=['GET'])
def get_id(id):
    usuario = dao_usuario.get_by_id(id)
    data = usuario.get_data_dict()
    return make_response(jsonify(data))

@app_usuario.route(f'/{app_name}/del/<id>', methods=['DELETE'])
def delete_id(id):
    return dao_usuario.delete_by_id(id)

@app_usuario.route(f'/{app_name}/disable/<id>', methods=['PATCH'])
def disable_id(id):
    return dao_usuario.disable_by_id(id)

@app_usuario.route(f'/{app_name}/att', methods=['PUT'])
def update_usuario():
    data = request.get_json()
    usuario = Usuario(**data)
    if dao_usuario.update_usuario(usuario):
        return make_response(jsonify(data))
    return 404