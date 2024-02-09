from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__,template_folder="template")

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['test']  # Replace 'your_database_name' with your actual database name
collection = db['test']  # Replace 'your_collection_name' with your actual collection name

# In app.py
@app.route('/')
def index():
    # ... other code

    # Retrieve data for both dropdowns in a single query
    data = list(collection.find({}, {'name': 1, 'value': 1}))  # Project only necessary fields

    dropdown_options_1 = [item['name'] for item in data]
    dropdown_options_2 = [item['value'] for item in data]

    return render_template('index.html', dropdown_options_1=dropdown_options_1, dropdown_options_2=dropdown_options_2)



@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        value = request.form.get('value')

        # Store data in MongoDB
        collection.insert_one({'name': name, 'value': value})

        return redirect(url_for('home'))

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
