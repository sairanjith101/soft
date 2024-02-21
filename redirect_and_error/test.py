from flask import Flask, render_template, request, redirect, url_for,abort

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username == 'admin':
            return redirect(url_for('success'))
        else:
            error = 'Invalid username'
            return render_template('test.html', error=error)
    else:
        return redirect(url_for('login'))
    


@app.route('/success')
def success():
    return 'Logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)