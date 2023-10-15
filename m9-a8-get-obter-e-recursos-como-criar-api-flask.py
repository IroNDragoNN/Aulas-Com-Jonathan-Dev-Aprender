# NOSSO 1º API - FLASK E DJANGO
# (Flask tradicional e comum) & (Flask Restul - mais complexo)

"""
1 Definir o objetivo da API:
    Ex: Iremos montar uma API de blog, onde eu poderei...
    consultar, editar, criar e excluir postagens em um blog usando a API.

2 - Qual será o URL base do API?
    Ex: Quando você cria uma aplicação local ela terá um url tipo -> http://localhost:5000 , porém quando
    vocÊ for subir isso para núvem, você terá que comprar ou usar um domínio como url base, vamos
    imaginar um exemplo de devaprender.com/api/
3 - Quais são os endpoints?
    Ex: Se seu requísito é de poder consultar, editar, criar e excluir, você terá que...
    disponibilizar os endpoints para essas questões > /postagens/ !
4 - Quais recursos serão disponibilizados pelo api: informações sobre as postagens
5 - Quais verbos http serão disponibilizados?
    * GET
    * POST
    * PUT
    * DELETE
6 - Quais são os URL completos para cada um?            #(PODE SER PASSADA PARA UMA DOCUMENTAÇÃO PARA 
    * GET http:localhost:5000/postagens                   AS PESSOAS SABEREM DOS RECURSOS DISPONÍVEIS.)
    * GET id http:localhost:5000/postagens/1
    * POST id http:localhost:5000/postagens
    * PUT id http:localhost:5000/postagens/1
    * DELE id http:localhost:5000/postagens/1
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

postagens = [
    {
        'titulo': 'Minha História', 
        'autor': 'Amanda Dias'
    },
    {
        'titulo': 'Novo Dispositivo Sony', 
        'autor': 'Howard Stringer'
    },
    {
        'titulo': 'Lançamento do Ano', 
        'autor': 'Jeff Bezos'
    }
]

# Rota padrão (A PESSOA ESTARÁ RECEBENDO QUANDO FAZ ACESSO AO URL BASE)
# ROTA PADRÃO - GET passando URL base que é: http://localhost:5000
# Porém se eu quiser obter um recurso específico como por exemplo, apenas a segunda postagem do exemplo 'Novo Dispositivo Sony'
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

app.run(port=5000, host='localhost', debug=True)