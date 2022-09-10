from flask import jsonify, make_response, Blueprint

from modulos.usuario.dao import UsuarioDAO

_app = Blueprint('usuario_blueprint', __name__)
app_name = 'users'
dao_usuario = UsuarioDAO()

@_app.route(f'/{app_name}/', methods=['GET'])
def get_usuarios():
    usuarios = dao_usuario.get_all()
    data = [usuario.get_data_dict() for usuario in usuarios]
    return make_response(jsonify(data))