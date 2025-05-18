from flask import Flask, request, jsonify, render_template, send_file
from datetime import date
from musica import gerar_midi, midi_para_wav
from agentes import agente_selecionador, agente_confortador, agente_buscador_louvores, agente_musicoterapeuta

app = Flask(__name__, static_url_path="/static", static_folder="static", template_folder="templates")
WAV_PATH = "musica.wav"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gerar", methods=["POST"])
def gerar():
    data = request.json
    sentimento = data.get("sentimento", "")
    data_de_hoje = date.today().strftime("%d/%m/%Y") 
    versiculos = agente_selecionador(sentimento, data_de_hoje)
    conforto = agente_confortador(sentimento, versiculos)
    louvores = agente_buscador_louvores(sentimento, conforto, versiculos)
    notas = agente_musicoterapeuta(sentimento, conforto, versiculos)

    gerar_midi(notas)
    midi_para_wav()

    return jsonify({
        "data": data_de_hoje,
        "sentimento": sentimento,
        "versiculos": versiculos,
        "conforto": conforto,
        "louvores": louvores,
        "notas musicais": notas,
        "audio_url": "/musica"
    })

@app.route("/musica")
def musica():
    return send_file(WAV_PATH, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True, port=4000)
