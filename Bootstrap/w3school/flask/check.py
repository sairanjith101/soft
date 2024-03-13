from flask import Flask, render_template, request
from pymongo import MongoClient

# Configure MongoDB connection (replace with your connection details)
client = MongoClient("mongodb://localhost:27017/")  # Localhost connection
db = client["Sai"]  # Replace with your database name
collection = db["New"]  # Replace with your collection name

app = Flask(__name__, template_folder="template")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {}
        for field in range(1, 8):  # Assuming 7 input fields
            field_name = f"field{field}"  # Dynamic field name generation
            if request.form.get(field_name):  # Check if data is present
                data[field_name] = request.form[field_name]

        if data:  # Save data only if at least one field has input
            collection.insert_one(data)
            return "Data submitted successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
