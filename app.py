from flask import *
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://victor:<db_password>@pengcluster.bhoffwm.mongodb.net/?retryWrites=true&w=majority&appName=pengCluster"
# Create a new client and connect to the server
client = MongoClient(uri)
app = Flask(__name__)

# --- Configuration ---
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
# MongoDB Atlas URI or local MongoDB
app.config['MONGO_URI'] = os.getenv(
    'MONGO_URI',
    'mongodb://localhost:27017/tutorapp'
)

mongo = PyMongo(app)
users = mongo.db.users  # users collection

# --- Routes ---
@app.route('/')
def home():
    user = session.get('username')
    return render_template('index.html', user=user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.find_one({'username': username}):
            flash('Username already exists.', 'error')
            return redirect(url_for('signup'))
        users.insert_one({
            'username': username,
            'password': password  # TODO: hash in production
        })
        session['username'] = username
        flash('Signed up successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username, 'password': password})
        if user:
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        flash('Invalid credentials.', 'error')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)