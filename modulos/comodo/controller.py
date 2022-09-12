from flask import Blueprint, jsonify, make_response, request

from modulos.comodo.comodo import Comodo
from modulos.comodo.dao import ComodoDAO

app_comodo = Blueprint('comodo_blueprint', __name__)
app_name = 'comodo'
dao_comodo = ComodoDAO()

@app_comodo.route(f'/{app_name}/', methods=['GET'])
def get_comodos():
    comodos = dao_comodo.get_all()
    data = [comodo.get_data_dict() for comodo in comodos]
    return make_response(jsonify(data))

@app_comodo.route(f'/{app_name}/add/', methods=['POST'])
def save_cliente():
    data = request.get_json()
    comodo = Comodo(**data)
    if dao_comodo.salvar(comodo):
        return make_response(jsonify(data))
    return 404

@app_comodo.route(f'/{app_name}/<id>', methods=['GET'])
def get_id(id):
    comodo = dao_comodo.get_by_id(id)
    data = comodo.get_data_dict()
    return make_response(jsonify(data))

@app_comodo.route(f'/{app_name}/del/<id>', methods=['DELETE'])
def delete_id(id):
    return dao_comodo.delete_by_id(id)