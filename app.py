from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'segredo'

respostas_corretas = {
    1: [
        {'opcao': 'had wished', 'correta': True},
        {'opcao': 'wishing', 'correta': False},
        {'opcao': 'wish', 'correta': False},
        {'opcao': 'wished', 'correta': False},
    ],
    2: [
        {'opcao': 'wished', 'correta': True},
        {'opcao': 'wish', 'correta': False},
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
        {'opcao': 'had arrived', 'correta': True},
        {'opcao': 'arrives', 'correta': False},
        {'opcao': 'arrived', 'correta': False},
        {'opcao': 'arrive', 'correta': False},
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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/introduction', methods=['GET', 'POST'])
def namePage():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('levels/1.html', name=name)
    else:
        return render_template('introduction.html')


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
        resposta_correta = respostas_corretas.get(levelnum)

        if resposta_usuario.lower() == resposta_correta.lower():
            # A resposta está correta, então vá para o próximo nível
            session['levelnum'] += 1
            levelnum = session['levelnum']
        else:
            # A resposta está incorreta, defina a mensagem de erro
            mensagem_erro = "Resposta incorreta. Tente novamente."

    # Embaralhe aleatoriamente as opções de resposta para o nível atual
    opcoes_resposta = random.sample(list(respostas_corretas.values()), 4)

    # Renderize o template HTML e passe as opções de resposta e a mensagem de erro
    return render_template('levels/{}.html'.format(levelnum), opcoes_resposta=opcoes_resposta, mensagem_erro=mensagem_erro)


@app.route('/start/levels/<int:levelnum>', methods=['GET', 'POST'])
def render_level(levelnum):
    return render_template(f'levels/{levelnum}.html')


@app.route('/about', methods=['GET', 'POST'])
def aboutPage():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)