from flask import jsonify, make_response, Blueprint

from modulos.cliente.dao import ClienteDAO

_app = Blueprint('example_blueprint', __name__)
app_name = 'cliente'
dao_cliente = ClienteDAO()

@_app.route(f'/{app_name}/', methods=['GET'])
def get_clientes():
    clientes = dao_cliente.get_all()
    data = [cliente.get_data_dict() for cliente in clientes]
    return make_response(jsonify(data))