from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'segredo'

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

def levelPage():
    # Verifique se 'levelnum' está na sessão, se não, defina-o como 1
    if 'levelnum' not in session:
        session['levelnum'] = 1
    else:
        # Incrementa o número do nível a cada acesso
        session['levelnum'] += 1

    # Obtém o número do nível atual
    levelnum = session['levelnum']

    # Redireciona para a rota com o novo número do nível
    return redirect(url_for('render_level', levelnum=levelnum))

@app.route('/start/levels/<int:levelnum>', methods=['GET', 'POST'])
def render_level(levelnum):
    return render_template(f'levels/{levelnum}.html')

@app.route('/about', methods=['GET', 'POST'])
def aboutPage():
    return render_template('about.html')

app.run(debug=True)