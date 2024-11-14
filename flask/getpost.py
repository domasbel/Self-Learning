from flask import Flask, render_template, request

# app initialization
app = Flask(__name__)

@app.route('/')
def welcome():
    return """
    <html>
        <head><title>Welcome Page</title></head>
        <body>
            <h1>Welcome to the Flask Course</h1>
            <p>Click below to navigate to different pages:</p>

            <!-- Button to go to index page -->
            <button onclick="window.location.href='/index'">Go to Index</button><br><br>

            <!-- Button to go to form page -->
            <button onclick="window.location.href='/form'">Go to Form</button>
        </body>
    </html>
    """

# here we can skip or write down GET since its a default in a way
# but by defining it in such way we remove the possibility of all other methods
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

# here it automatically assumes that this will handle GET method because nothing else is mentioned
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form')
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)