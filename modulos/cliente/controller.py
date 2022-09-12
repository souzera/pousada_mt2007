from flask import jsonify, make_response, Blueprint, request

from modulos.cliente.cliente import Cliente
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
def save_cliente():
    data = request.get_json()
    cliente = Cliente(**data)
    if dao_cliente.salvar(cliente):
        return make_response(jsonify(data))
    return 404

@app_cliente.route(f'/{app_name}/<id>', methods=['GET'])
def get_id(id):
    cliente = dao_cliente.get_by_id(id)
    data = cliente.get_data_dict()
    return make_response(jsonify(data))

@app_cliente.route(f'/{app_name}/del/<id>', methods=['DELETE'])
def delete_id(id):
    return dao_cliente.delete_by_id(id)

