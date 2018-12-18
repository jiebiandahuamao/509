from flask import Blueprint, request, render_template
from app_backend import app
import os
import tempfile
from werkzeug.utils import secure_filename

bp_index = Blueprint('index', __name__, url_prefix='/index')

@app.route('/index/', methods=['GET', 'POST'])
def index():
    print(1233456789)
    return render_template('base.html')

@app.route('/upload/', methods=['GET', 'POST'])
def upload():

    # file = request.files['file']
    # if file:
    #     filename = secure_filename(file.filename)
    #     dst = os.path.join("C:/509/app_backend/static/pic", filename)
    #     file.save(dst)

    return render_template('upload.html')