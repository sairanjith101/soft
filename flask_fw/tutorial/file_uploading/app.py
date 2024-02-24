from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder="template")

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file_handler():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
    
if __name__ == '__main__':
    app.run(debug=True)