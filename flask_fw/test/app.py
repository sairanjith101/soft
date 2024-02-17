from flask import Flask, render_template, request,flash

app = Flask(__name__, template_folder="template")
app.secret_key = "123"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('success'):
            flash("Success message", "success")
        elif request.form.get('warning'):
            flash("Warning message", "warning")
        elif request.form.get('primary'):
            flash("Primary message", "primary")
        elif request.form.get('secondary'):
            flash("Secondary message", "secondary")
        elif request.form.get('danger'):
            flash("Danger message", "danger")
        elif request.form.get('dark'):
            flash("Dark message", "dark")
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)