# app.py

from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId from bson module

app = Flask(__name__, template_folder="template")

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['check']  # Replace 'your_database_name' with your actual database name
collection = db['check']  # Replace 'your_collection_name' with your actual collection name

def get_all_data_from_mongodb():
    # Implement logic to query all data from MongoDB
    result = list(collection.find({}))
    return result

@app.route('/')
def index():
    selected_operation_id = request.args.get('selected_operation_id', '')
    # Retrieve data from MongoDB
    database_data = get_all_data_from_mongodb()
    return render_template('database.html', database_data=database_data, selected_operation_id=selected_operation_id)

@app.route('/delete/<operation_id>', methods=['POST'], endpoint='delete')
def delete_operation(operation_id):
    # Implement the logic to delete the operation
    # Delete the document from MongoDB
    collection.delete_one({'operation_id': operation_id})
    return redirect(url_for('index'))

@app.route('/details/<operation_id>')
def operation_details(operation_id):
    # Retrieve data for the selected operation from MongoDB
    operation_data = collection.find_one({'operation_id': operation_id})

    # Render the details template with the operation data
    return render_template('details.html', operation_data=operation_data)


if __name__ == '__main__':
    app.run(debug=True)
