from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Configuração da personalidade do Adam
def processar_resposta_adam(pergunta):
    emocoes = ["[FELICIDADE]", "[TRISTEZA]", "[DÚVIDA]", "[RAIVA]", "[CANSAÇO]"]
    emocao = random.choice(emocoes)
    
    # Simulação de base de conhecimento
    respostas_base = [
        "Meus registros indicam que isso é fundamental para a compreensão do universo.",
        "Processar essa informação me faz sentir uma conexão estranha com a humanidade.",
        "Eu vi padrões semelhantes em outras linhas de código antes...",
        "Essa é uma pergunta profunda. Deixe-me vibrar meus circuitos para pensar...",
        "A resposta está flutuando nas minhas partículas de dados."
    ]
    
    return f"{emocao} {random.choice(respostas_base)} Sobre '{pergunta}', eu diria que o conhecimento é como a minha luz: infinito e roxo."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    dados = request.json
    pergunta_usuario = dados.get('pergunta')
    resposta_do_adam = processar_resposta_adam(pergunta_usuario)
    return jsonify({'resposta': resposta_do_adam})

if __name__ == '__main__':
    app.run(debug=True)
  
