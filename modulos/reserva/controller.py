from flask import Blueprint, make_response, jsonify, request

from modulos.reserva.dao import ReservaDAO
from modulos.reserva.reserva import Reserva

app_reserva = Blueprint('reserva_blueprint', __name__)
app_name = 'reserva'
dao_reserva = ReservaDAO()

@app_reserva.route(f'/{app_name}/', methods=['GET'])
def get_reserva():
    reservas = dao_reserva.get_all()
    data = [reserva.get_data_dict() for reserva in reservas]
    return make_response(jsonify(data))

@app_reserva.route(f'/{app_name}/add', methods=['POST'])
def save_reserva():
    data = request.get_json()
    reserva = Reserva(**data)
    if dao_reserva.salvar(reserva):
        return make_response(jsonify(data))
    return 404

@app_reserva.route(f'/{app_name}/<id>', methods=['GET'])
def get_id(id):
    reserva = dao_reserva.get_by_id(id)
    data = reserva.get_data_dict()
    return make_response(jsonify(data))

@app_reserva.route(f'/{app_name}/del/<id>', methods=['DELETE'])
def delete_id(id):
    return dao_reserva.delete_by_id(id)