from flask import Flask, url_for,request,render_template,make_response,redirect,session
from markupsafe import escape, Markup
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route("/")
def index():
    username = request.cookies.get('username')
    resp = make_response(render_template("index.html"))
    resp.set_cookie('username', 'the username')
    return resp


@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):

    url_for('static', filename='style.css')
    return render_template('hello.html', name=name)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
@app.route('/projects/')
def projects():
    return 'The project page'
@app.route('/about')
def about():
    return 'The about page'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

"""""@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)"""

from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(f"/var/www/uploads/{secure_filename(f.filename)}")

def do_the_login():
    return "Do the login"
def show_the_login_form():
    return "Your  login form"

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'


