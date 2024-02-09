from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    # Simulate some processing time
    time.sleep(3)

    # Process the form data (you can add your logic here)

    # Return a JSON response indicating success
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
