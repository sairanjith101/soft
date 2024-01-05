from flask import Flask, render_template, request, flash

app = Flask(__name__, template_folder="template")
app.secret_key = "123"

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('success'):
            flash("Success Message", "success")  # Corrected category spelling here
        elif request.form.get('warning'):
            flash("Warning Message", "warning")
        elif request.form.get('primary'):
            flash("Primary Message", "primary")
        elif request.form.get('secondary'):
            flash("Secondary Message", "secondary")
        elif request.form.get('info'):
            flash("Info Message", "info")
        elif request.form.get('danger'):
            flash("Danger Message", "danger")
        elif request.form.get('dark'):
            flash("Dark Message", "dark")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)




