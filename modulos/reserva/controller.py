from flask import Blueprint, make_response, jsonify

from modulos.reserva.dao import ReservaDAO

_app = Blueprint('example_blueprint', __name__)
app_name = 'reserva'
dao_reserva = ReservaDAO()

@_app.route(f'/{app_name}/', methods=['GET'])
def get_reserva():
    reservas = dao_reserva.get_all()
    data = [reserva.get_data_dict() for reserva in reservas]
    return make_response(jsonify(data))