from flask import Flask

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    