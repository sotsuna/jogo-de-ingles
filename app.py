from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'segredo'

respostas_corretas = {
    1: 'Had wished',
    2: 'Wish',
    3: 'Had arrived',
    4: 'Wished',
    5: 'Had left',
    6: 'Had wished',
    7: 'Had called',
    8: 'Wished'
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/newroom', methods=['GET', 'POST'])
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

        if resposta_usuario == resposta_correta:
            # A resposta está correta, então vá para o próximo nível
            session['levelnum'] += 1
            levelnum = session['levelnum']
        else:
            # A resposta está incorreta, defina a mensagem de erro
            mensagem_erro = "Resposta incorreta. Tente novamente."

    # Renderize o template HTML e passe a mensagem de erro
    return render_template('levels/{}.html'.format(levelnum), mensagem_erro=mensagem_erro)


@app.route('/start/levels/<int:levelnum>', methods=['GET', 'POST'])
def render_level(levelnum):
    return render_template(f'levels/{levelnum}.html')


@app.route('/about', methods=['GET', 'POST'])
def aboutPage():
    return render_template('about.html')


app.run(debug=True)
