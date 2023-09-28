from flask import Flask, render_template, request, session, redirect, url_for
import random

# cria o app do Flask
app = Flask(__name__, static_folder='static', template_folder='templates')

# chave genérica só pra fazer o app funcionar
app.secret_key = 'segredo'


# array com as respostas corretas
respostas_corretas = {
    1: [
        {'question_level': 'First Question'},
        {'questao': 'What is the correct conjugation of the verb "wish" in the "past perfect"?'},
        {'opcao': 'had wished', 'correta': True},
        {'opcao': 'wishing', 'correta': False},
        {'opcao': 'wish', 'correta': False},
        {'opcao': 'wished', 'correta': False},
    ],
    2: [
        {'question_level': 'Second Question'},
        {'questao': 'What is the correct conjugation of the verb "wish" in the "past perfect"?'},
        {'opcao': 'wish', 'correta': True},
        {'opcao': 'wished', 'correta': False},
        {'opcao': 'wishing', 'correta': False},
        {'opcao': 'had wished', 'correta': False},
    ],
    3: [
        {'question_level': 'Third Question'},
        {'questao': 'What is the correct conjugation of the verb "wish" in the "past perfect"?'},
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
    ],
    4: [
        {'question_level': 'Fourth Question'},
        {'questao': 'What is the correct conjugation of the verb "wish" in the "past perfect"?'},
        {'opcao': 'wished', 'correta': True},
        {'opcao': 'had wish', 'correta': False},
        {'opcao': 'wish', 'correta': False},
        {'opcao': 'had wished', 'correta': False},
    ],
    5: [
        {'question_level': 'Fifth Question'},
        {'questao': 'What is the correct conjugation of the verb "wish" in the "past perfect"?'},
        {'opcao': 'had left', 'correta': True},
        {'opcao': 'leaves', 'correta': False},
        {'opcao': 'left', 'correta': False},
        {'opcao': 'leave', 'correta': False},
    ],
    6: [
        {'question_level': 'Sixth Question'},
        {'questao': 'What is the correct conjugation of the verb "wish" in the "past perfect"?'},
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
    ],
    7: [
        {'question_level': 'Seventh Question'},
        {'questao': 'What is the correct conjugation of the verb "wish" in the "past perfect"?'},
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
    ],
    8: [
        {'question_level': 'Eighth Question'},
        {'questao': 'What is the correct conjugation of the verb "wish" in the "past perfect"?'},
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
    ],
}

def embaralhar_opcoes(opcoes):
    random.shuffle(opcoes)

# route para puxar a index
@app.route('/')
def index():
    return render_template('index.html')

# route para puxar a tela de introdução do jogo
@app.route('/introduction', methods=['GET', 'POST'])
def namePage():
    name = None  # Inicialize a variável name como None
    if request.method == 'POST':
        name = request.form['name']
    return render_template('introduction.html')

# Route para puxar o sistema de níveis e testar se a resposta concedida foi a correta
@app.route('/level', methods=['GET', 'POST'])
def levelPage():
    # Verifique se 'levelnum' está na sessão, se não, defina-o como 1
    if 'levelnum' not in session:
        session['levelnum'] = 1

    # Obtém o número do nível atual
    levelnum = session['levelnum']

    # Obtém as opções de resposta para o nível atual
    respostas_nivel_atual = respostas_corretas.get(levelnum, [])

    # Conta quantos botões estão visíveis
    quantidade_botao_visivel = len([opcao for opcao in respostas_nivel_atual if not opcao.get('oculto')])

    # Calcula a probabilidade com base na quantidade de botões visíveis
    probabilidade_acerto = 100 / quantidade_botao_visivel if quantidade_botao_visivel > 0 else 0

    mensagem_erro = None  # Inicialize a variável de mensagem de erro como None

    if request.method == 'POST':
        resposta_usuario = request.form.get('resposta')

        # Verifica se a resposta do usuário está entre as opções corretas
        resposta_correta = any(opcao.get('correta', False) and opcao.get('opcao', '').lower() == resposta_usuario.lower() for opcao in respostas_nivel_atual)

        if not resposta_correta:
            # Se a resposta estiver incorreta, marque o botão clicado como oculto
            botao_errado = request.form.get('resposta')
            mensagem_erro = "Resposta incorreta. Tente novamente."
            for opcao in respostas_nivel_atual:
                if opcao.get('opcao', '').lower() == resposta_usuario.lower():
                    opcao['oculto'] = True

        # Se a resposta estiver correta, vá para o próximo nível
        if resposta_correta:
            session['levelnum'] += 1

        opcoes_resposta_visiveis = [opcao for opcao in respostas_nivel_atual if not opcao.get('oculto')]
        def compara():
            if levelnum > 8:
                return redirect(url_for('endGame'))
            else:
                return render_template('levels/{}.html'.format(levelnum), opcoes_resposta=opcoes_resposta_visiveis, mensagem_erro=mensagem_erro, probabilidade_acerto=probabilidade_acerto)
    return compara()

@app.route('/about', methods=['GET', 'POST'])
def aboutPage():
    return render_template('about.html')

@app.route('/end', methods=['GET', 'POST'])
def endGame():
    return render_template('end_page.html')


if __name__ == '__main__':
    app.run(debug=True)