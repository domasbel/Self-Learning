from flask import Flask

# it creates an instance of flask class, which will be your WSGI app

# WSGI app
app = Flask(__name__)

@app.route('/')
def welcome():
    return '''
        <html>
            <head><title>Welcome</title></head>
            <body>
                <h1>Welcome to this Flask experiment</h1>
                <button onclick="window.location.href='/index'">Go to Index</button>
            </body>
        </html>
    '''


@app.route('/index')
def index():
    return '''
        <html>
            <head><title>Index Page</title></head>
            <body>
                <h1>This is some subpage that can be modified</h1>
                <button onclick="window.location.href='/'">Go Back to Home</button>
            </body>
        </html>
    '''

if __name__=='__main__':
    app.run(debug=True)
