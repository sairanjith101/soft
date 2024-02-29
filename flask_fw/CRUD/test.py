from flask import Flask, render_template, request
import pymongo
from faker import Faker
from bson import ObjectId

app = Flask(__name__, template_folder="template")

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['studentdb']
collection = db['students']

faker = Faker()

def generate_students(n):
    for _ in range(n):
        student = {
            'Sno': faker.random_int(min=1113, max=1200),
            'Sname': faker.name(),
            'Sclass': faker.random_int(min=1, max=12),
            'Saddress': faker.city()
        }
        collection.insert_one(student)

generate_students(48)

@app.route('/')
def index():
    # Retrieve data from MongoDB
    data = collection.find()
    return render_template('index.html', data=data)

@app.route('/delete/<id>', methods=['POST'])
def delete_student(id):
    collection.delete_one({'_id': ObjectId(id)})
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
