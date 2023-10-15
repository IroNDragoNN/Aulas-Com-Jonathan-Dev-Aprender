from flask import Flask, jsonify, request

app = Flask(__name__)
postagens = [
    {
        'título': 'Minha História',
        'autor': 'Amanda Dias'
    },
    {   'título': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'título': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }
]
# Rota padrão - GET http://localhost:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# GET com ID - GET http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])             # <int:indice> significa que queremos um índice do tipo inteiro
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])                            # Jsonify retornará um objeto que será uma postagem, indexado do indice
                                                                 # passado acima
app.run(port=5000, host='localhost', debug=True)