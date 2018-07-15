from flask import Flask, render_template

#assigning app to the Flask namespace
app = Flask(__name__)

# Routes anytime a user hits / as a link to take them home
@app.route('/')
def home():
    return render_template('home.html')

# Routes anytime a user hits /welcome as a link to take them to the welcome page

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
    
if __name__ == '__main__':
    app.run()
