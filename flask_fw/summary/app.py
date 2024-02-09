# app.py

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="template")

# Mock data for demonstration
data = [
    {"operation_name": "Operation1", "operation_id": "1", "operation_grade": "A", "neck": 1, "leg": 2, "arm": 1, "eye": 2, "nose": 1},
    {"operation_name": "Operation2", "operation_id": "2", "operation_grade": "B", "neck": 1, "leg": 2, "arm": 1, "eye": 2, "nose": 1},
    # Add more data as needed
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/result/<operation_id>')
def result(operation_id):
    # Fetch the data for the index page (mock data for demonstration)
    index_data = {
        "operation_name": "Operation1",
        "operation_id": "1",
        "operation_grade": "A",
        "neck": 1,
        "leg": 2,
        "arm": 1,
        "eye": 2,
        "nose": 1,
    }

    # Fetch the data for the value details (mock data for demonstration)
    value_data = {
        "operation_name": "SelectedOperation",
        "operation_id": operation_id,
        "operation_grade": "A",
        # Add more data as needed
    }

    return render_template('result.html', operation_id=operation_id, index_data=index_data, value_data=value_data)

@app.route('/delete/<operation_id>', methods=['POST'], endpoint='delete')
def delete_operation(operation_id):
    # Implement the logic to delete the operation
    # This is a placeholder, adjust it based on your actual delete logic
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
