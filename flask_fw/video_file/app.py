from flask import Flask, render_template, request, send_file, make_response
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder="template")
app.config['SECRET_KEY'] = 'secrets.token_hex(16)'
app.config['UPLOAD_FOLDER'] = 'upload'

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['rk']
videos_collection = db['videos']

@app.route('/')
def index():
    # Retrieve a list of video filenames from MongoDB
    video_filenames = [video['filename'] for video in videos_collection.find()]
    return render_template('index.html', video_filenames=video_filenames)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' in request.files:
        video = request.files['video']
        if video.filename != '':
            filename = secure_filename(video.filename)
            video.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            video_data = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb').read()
            videos_collection.insert_one({'filename': filename, 'data': video_data})
            return 'Video uploaded successfully'
    return 'No video provided'

@app.route('/download/<filename>')
def download_video(filename):
    video_data = videos_collection.find_one({'filename': filename})
    if video_data:
        response = make_response(video_data['data'])
        response.headers['Content-Type'] = 'video/mp4'  # Set the appropriate MIME type
        response.headers['Content-Disposition'] = f'attachment; filename={filename}'
        return response
    return 'Video not found'

if __name__ == '__main__':
    app.run(debug=True)

