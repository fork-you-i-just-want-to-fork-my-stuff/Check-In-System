from flask import *

#assigning app to the Flask namespace
app = Flask(__name__)

@app.route('/')
def home():
    """Routing for site homepage"""
    return render_template('home.html')

@app.route('/search')
def search_user():
    """Routing to a page where you can search users"""
    return render_template('search.html')

@app.route('/check-in')
def check_in():
    """Routing to client check in page"""
    return render_template('check-in.html')

@app.route('/queue')
def queue():
    """Routing to client view of the current client queue"""
    return render_template('queue.html')

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
            return redirect(url_for('queuemanagement'))

    #first time viewing or refresh on failed login
    return render_template('login.html', error = error)

@app.route('/queuemanagement')
def queuemanagement():
    """Manager view of the client queue; has access to remove clients from queue"""
    return render_template('queuemanagement.html')

if __name__ == '__main__':
    app.run()
