from flask import Flask, render_template

#assigning app to the Flask namespace
app = Flask(__name__)

# Routes anytime a user hits / as a link to take them home
@app.route('/')
def home():
    return render_template('home.html')

# Routes anytime a user hits /welcome as a link to take them to the welcome page

@app.route('/search')
def search_user():
    return render_template('search.html')

@app.route('/check-in')
def check_in():
    return render_template('check-in.html')

if __name__ == '__main__':
    app.run()
