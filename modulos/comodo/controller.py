from flask import Blueprint, jsonify, make_response

from modulos.comodo.dao import ComodoDAO

app_comodo = Blueprint('comodo_blueprint', __name__)
app_name = 'comodo'
dao_comodo = ComodoDAO()

@_app.route(f'/{app_name}/', methods=['GET'])
def get_comodos():
    comodos = dao_comodo.get_all()
    data = [comodo.get_data_dict() for comodo in comodos]
    return make_response(jsonify(data))