from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route('/hello/<user>')
def hello(user):
    return render_template('index.html', name=user)

if __name__ == '__main__':
    app.run(debug=True)