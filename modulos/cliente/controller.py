from flask import jsonify, make_response, Blueprint

from modulos.cliente.dao import ClienteDAO

app_cliente = Blueprint('cliente_blueprint', __name__)
app_name = 'cliente'
dao_cliente = ClienteDAO()

@app_cliente.route(f'/{app_name}/', methods=['GET'])
def get_clientes():
    clientes = dao_cliente.get_all()
    data = [cliente.get_data_dict() for cliente in clientes]
    return make_response(jsonify(data))

@app_cliente.route(f'/{app_name}/add/', methods=['POST'])
def save_cliente(cliente):
    cliente = dao_cliente.salvar(cliente)
    data = cliente.get_data_dict()
    return make_response(jsonify(data))

@app_cliente.route(f'/{app_name}/<id>', methods=['GET'])
def get_id(id):
    cliente = dao_cliente.get_by_id(id)
    data = cliente.get_data_dict()
    return make_response(jsonify(data))