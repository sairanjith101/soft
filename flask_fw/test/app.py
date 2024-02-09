from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")

@app.route("/")
def main():
    return render_template("Register.html")

@app.route("/Register", methods=["POST", "GET"])
def Register():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        address = request.form.get("address")
        contact = request.form.get("contact")
        email = request.form.get("email")
        return render_template("result.html", name=name, age=age, address=address, contact=contact, email=email)


if __name__ == "__main__":
    app.run(debug=True)