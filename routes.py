from flask import *
from functools import wraps
from dbUtilities import *


#assigning app to the Flask namespace
app = Flask(__name__)

app.secret_key = '>wwx7M_9!>IU6z!ME[D"HxcLN#<)v('

def login_required(test):
    """Used to force users to login on specific pages"""
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You must login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
def home():
    """Routing for site homepage"""
    return render_template('home.html')

@app.route('/search')
def search_user():
    """Routing to a page where you can search users"""
    return render_template('search.html', clients = get_client_db())

@app.route('/check-in')
def check_in():
    """Routing to client check in page"""
    return render_template('check-in.html')

@app.route('/logout')
def logout():
    """Function to reset user session 'logs user out'"""
    session.pop('logged_in', None)
    flash("You've been logged out")
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Defines how users login; uses HTTP get and post requests"""
    error = None
    if request.method == 'POST':
        # TODO: Tie this to an admin database so that users and passwords can be managed properly

        # NOTE: Change the 'admin' credentials here; this is user login validation
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again'

        #if login succeeds
        else:
            session['logged_in'] = True
            return redirect(url_for('queuemanagement'))

    #first time viewing or refresh on failed login
    return render_template('login.html', error = error)

@app.route('/clientmanagement')
@login_required
def queuemanagement():
    """Manager view of the clients; allows you to remove clients, requires login"""
    return render_template('clientmanagement.html', clients = get_client_db())




if __name__ == '__main__':
    app.run()
