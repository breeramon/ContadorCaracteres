from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analisar', methods=['POST'])
def analisar_texto():
    dados = request.get_json()

    if not dados or 'texto' not in dados:
        return jsonify({"erro": "O campo 'texto' é obrigatório no corpo da requisição."}), 400

    texto = dados['texto']

    caracteres_com_espacos = len(texto)
    caracteres_sem_espacos = len(texto.replace(" ", ""))
    
    palavras = len(texto.split() if texto else 0)

    resultados = {
        "com_espacos": caracteres_com_espacos,
        "sem_espacos": caracteres_sem_espacos,
        "palavras": palavras
    }

    return jsonify(resultados), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)