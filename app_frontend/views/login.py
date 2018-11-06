from flask import Blueprint, request, render_template
from app_frontend import app

bp_auth = Blueprint('login', __name__, url_prefix='/login')

@app.route('/aaa/', methods=['GET', 'POST'])
def login():
    print(123)
    return render_template('index.html')