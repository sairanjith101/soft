from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/flask')
def home():
    return "Hello World"

@app.route('/guest/<guest>')
def guest(guest):
    return "Hi " + guest

@app.route('/user/<user>')
def user(user):
    if user == 'flask':
        return redirect(url_for('home'))
    else:
        return redirect(url_for('guest', guest = user))
    
if __name__ == '__main__':
    app.run(debug=True)
    