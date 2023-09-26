from flask import Flask, render_template, request, session
import random

# cria o app do Flask
app = Flask(__name__, static_folder='static', template_folder='templates')

# chave genérica só pra fazer o app funcionar
app.secret_key = 'segredo'


# array com as respostas corretas
respostas_corretas = {
    1: [
        {'opcao': 'had wished', 'correta': True},
        {'opcao': 'wishing', 'correta': False},
        {'opcao': 'wish', 'correta': False},
        {'opcao': 'wished', 'correta': False},
    ],
    2: [
        {'opcao': 'wish', 'correta': True},
        {'opcao': 'wished', 'correta': False},
        {'opcao': 'wishing', 'correta': False},
        {'opcao': 'had wished', 'correta': False},
    ],
    3: [
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
    ],
    4: [
        {'opcao': 'wished', 'correta': True},
        {'opcao': 'had wish', 'correta': False},
        {'opcao': 'wish', 'correta': False},
        {'opcao': 'had wished', 'correta': False},
    ],
    5: [
        {'opcao': 'had left', 'correta': True},
        {'opcao': 'leaves', 'correta': False},
        {'opcao': 'left', 'correta': False},
        {'opcao': 'leave', 'correta': False},
    ],
    6: [
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
    ],
    7: [
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
    ],
    8: [
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
    ],
}


# route para puxar a index
@app.route('/')
def index():
    return render_template('index.html')

# route para puxar a tela de introdução do jogo
@app.route('/introduction', methods=['GET', 'POST'])
def namePage():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('levels/1.html', name=name)
    else:
        return render_template('introduction.html')

# route para puxar o sistema de níveis e testar se a resposta concedida foi a correta
@app.route('/level', methods=['GET', 'POST'])
def levelPage():
    # Verifique se 'levelnum' está na sessão, se não, defina-o como 1
    if 'levelnum' not in session:
        session['levelnum'] = 1

    # Obtém o número do nível atual
    levelnum = session['levelnum']

    mensagem_erro = None  # Inicialize a variável de mensagem de erro como None

    if request.method == 'POST':
        resposta_usuario = request.form.get('resposta')
        respostas_nivel_atual = respostas_corretas.get(levelnum)

        # Verifique se a resposta do usuário está entre as opções corretas
        resposta_correta = any(opcao['opcao'].lower() == resposta_usuario.lower() and opcao['correta'] for opcao in respostas_nivel_atual)

        if resposta_correta:
            # A resposta está correta, então vá para o próximo nível
            session['levelnum'] += 1
            levelnum = session['levelnum']
        else:
            # A resposta está incorreta, defina a mensagem de erro
            mensagem_erro = "Resposta incorreta. Tente novamente."

    # Embaralhe aleatoriamente as opções de resposta para o nível atual
    opcoes_resposta = random.sample(respostas_corretas[levelnum], 4)

    # Renderize o template HTML e passe as opções de resposta e a mensagem de erro
    return render_template('levels/{}.html'.format(levelnum), opcoes_resposta=opcoes_resposta, mensagem_erro=mensagem_erro)


@app.route('/about', methods=['GET', 'POST'])
def aboutPage():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)