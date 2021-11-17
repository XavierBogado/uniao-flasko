from flask import Flask

app = Flask(__name__)

 # rota

 # funcao

@app.route("/contatos")
def index():
    return "<p>Olá Flask</p>"

#rodar

app.run()

