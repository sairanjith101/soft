# Prototype of redirect() function is as below − Flask.redirect(location, statuscode, response)

# location parameter is the URL where response should be redirected.

# statuscode sent to browser’s header, defaults to 302.

# response parameter is used to instantiate response.

# The following status codes are standardized −

# HTTP_300_MULTIPLE_CHOICES
# HTTP_301_MOVED_PERMANENTLY
# HTTP_302_FOUND
# HTTP_303_SEE_OTHER
# HTTP_304_NOT_MODIFIED
# HTTP_305_USE_PROXY
# HTTP_306_RESERVED
# HTTP_307_TEMPORARY_REDIRECT

from flask import Flask , redirect, render_template, request,url_for

app = Flask(__name__, template_folder="template")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('home'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == '__main__':
    app.run(debug=True)
