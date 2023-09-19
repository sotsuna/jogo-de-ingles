from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')

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

@app.route('/levels/<levelnum>', methods=['GET', 'POST'])
def level1Page():
    return render_template('levels/1.html')

@app.route('/about', methods=['GET', 'POST'])
def aboutPage():
    return render_template('about.html')

app.run(debug=True)