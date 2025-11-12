from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secretkey'

users = {"admin": "1234"}


@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('signin'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('signin.html', error="ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

    return render_template('signin.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return render_template('register.html', error="ชื่อผู้ใช้นี้มีอยู่แล้ว!")
        users[username] = password
        return redirect(url_for('signin'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)
