from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route('/result/<int:score>')
def result(score):
    return render_template('result.html', mark = score)

if __name__ == '__main__':
    app.run(debug=True)