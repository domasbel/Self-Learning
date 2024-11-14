from flask import Flask, render_template

# it creates an instance of Flask class which will be the WSGI application
# WSGI - web server gateway interface

# wsgi application
app = Flask(__name__)

@app.route('/')
def welcome():
    return '<html><H1>Welcome to the flask course</H1></html>'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)


