from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Rota simples para verificar se a API está funcionando
@app.route('/')
def home():
    return jsonify({'message': 'API is working!'})

# Rota protegida que requer um token de API
@app.route('/protected')
def protected():
    # Verifica se o token enviado na requisição é válido
    token = request.headers.get('Authorization')
    if token != os.getenv('API_TOKEN'):
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Resposta se o token for válido
    return jsonify({'message': 'You accessed protected data!'})

if __name__ == '__main__':
    app.run(debug=True)
