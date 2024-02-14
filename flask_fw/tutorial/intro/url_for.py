from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi I am Ranjith"

@app.route('/guest/<guest>')
def guest(guest):
    return 'hello world ' + guest

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('home'))
    else:
        return redirect(url_for('guest', guest = name))
    
if __name__ == '__main__':
    app.run(debug=True)