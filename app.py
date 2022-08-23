from flask import Flask

app = Flask(__name__)
#app.register_blueprint()

@app.route('/')
def index():
    return "<div style='display:flex; justify-content:center;align-items:center; box-sizing: border-box; wight: 40vh; height:40vw'>" \
           "<h1 style='font-family:sans-serif;'>Olá mundo</h1>" \
           "</div>"

app.run()