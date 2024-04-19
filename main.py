#framework -> Flask -> criar site
#site com scripts -> https://cdnjs.com/
#pip install python-socketio flask-socketio simple-websocket

#ambiente virtual -> local no seu computador com instalaçoes especificas

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciarMensagem(mensagem):
    send(mensagem, broadcast=True)

#criar a nossa primeira pagina = 1° rota
#rota é o que vem depois da "/"

@app.route("/")
def homepage():
    return render_template("homepage.html")

#roda o nosso app
socketio.run(app, host="localhost")


#newsocket -> tunel