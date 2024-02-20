from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'Diavangama'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == 'nehemiediav@gmail.com' and password == 'admin':
            flash('Connexion réussie !', 'success')
            return redirect(url_for('success'))
        else:
            flash('Identifiants incorrects. Veuillez réessayer.', 'danger')

    return render_template('login.html')

@app.route('/success')
def success():
    return 'Authentification réussie !'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000) 