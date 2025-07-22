from flask import*

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # placeholder for login view
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # TODO: handle signup logic
    # e.g., email = request.form['email'], password = request.form['password']
    return render_template('signup.html')

@app.route('/member')
def member():
    # user = session.get('user_email')
    # if not user:
    #     return redirect(url_for('login'))
    return render_template('member.html')

@app.route('/requests', methods=['GET', 'POST'])
def requests_page():
    # user = session.get('user_email')
    # if not user:
    #     return redirect(url_for('login'))
    # if request.method == 'POST':
    #     # TODO: process and save request data
    #     flash('您的需求已送出！', 'success')
    #     return redirect(url_for('member'))
    return render_template('requests.html')

app.run(host="0.0.0.0" ,port=5000)