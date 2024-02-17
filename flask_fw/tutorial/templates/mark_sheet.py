from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route('/')
def total():
    result = {'phy': 56, 'che': 67, 'math': 70, 'tamil': 80}
    return render_template('mark_sheet.html', dict = result)

if __name__ == '__main__':
    app.run(debug=True)