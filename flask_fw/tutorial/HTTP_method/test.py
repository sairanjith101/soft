from flask import Flask, redirect, url_for, render_template,request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'Welcome ' + name

@app.route('/signin', methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))

if __name__ == '__main__':
    app.run(debug=True)



