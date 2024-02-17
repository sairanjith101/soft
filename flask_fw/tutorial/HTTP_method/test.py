from flask import Flask, redirect, url_for, request

app = Flask(__name__, template_folder="template")

@app.route('/success/<name>')
def success(name):
    return 'Welcome ' + name

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('success', name = user)

if __name__ == '__main__':
    app.run(debug=True)