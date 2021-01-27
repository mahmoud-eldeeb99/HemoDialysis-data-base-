from flask import Flask,send_from_directory,render_template
from flask import send_from_directory
#############
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
############


from flask_restful import Resource, Api
from package.patient import Patients, Patient
from package.doctor import Doctors, Doctor
from package.common import Common
from package.medication import Medication, Medications
from package.nurse import Nurse, Nurses



import json
import os

with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')
api = Api(app)

api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')
api.add_resource(Doctors, '/doctor')
api.add_resource(Doctor, '/doctor/<int:id>')
api.add_resource(Common, '/common')
api.add_resource(Medications, '/medication')
api.add_resource(Medication, '/medication/<int:code>')
api.add_resource(Nurses, '/nurse')
api.add_resource(Nurse, '/nurse/<int:id>')

# Routes

######################################3 log in admin

"""
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    #def __repr__(self):
        #return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='eldeeb', password='123'))
users.append(User(id=2, username='ali', password='123'))
users.append(User(id=3, username='mahmoud', password='123'))


app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return  app.send_static_file('index.html')#redirect(url_for('index.html'))

        return app.send_static_file('login.html')

    return app.send_static_file('login.html')






"""






###########################################






#""""

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return app.send_static_file('index.html')


#"""
if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])
