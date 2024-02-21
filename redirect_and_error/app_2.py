from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('error.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username == 'admin':
            return redirect(url_for('success'))
        else:
            error = "Invalid username"
            return render_template('error.html', error=error)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'Logged in successfully'

if __name__ == '__main__':
    app.run(debug=True)
