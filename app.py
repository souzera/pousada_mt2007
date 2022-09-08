from flask import Flask

from modulos.cliente.controller import app_cliente

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(app_cliente)
#app.register_blueprint()

@app.route('/')
def index():
    return centralizar("<h1 style='font-family:sans-serif;'>olá mundo</h1>")

#todo: metodo temporario para centralizar conteudo na tela -- apagar dps
def centralizar(texto):
    return f"<div style='display:flex; justify-content:center;align-items:center; box-sizing: border-box; wight: 40vh; height:40vw'>" \
           f"{texto}" \
           f"</div>"

if __name__ == "__main__":
    app.run(debug=True)