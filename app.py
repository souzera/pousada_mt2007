from flask import Flask

app = Flask(__name__)
#app.register_blueprint()

@app.route('/')
def index():
    return centralizar("<h1 style='font-family:sans-serif;'>Parabéns viu seu coco</h1>")

#todo: metodo temporario para centralizar conteudo na tela -- apagar dps
def centralizar(texto):
    return f"<div style='display:flex; justify-content:center;align-items:center; box-sizing: border-box; wight: 40vh; height:40vw'>" \
           f"{texto}" \
           f"</div>"

if __name__ == "__main__":
    app.run(debug=True)