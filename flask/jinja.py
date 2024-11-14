# building an url dynamically
# variable rule
# jinja 2 template engine

# {{ }} expressions to print output in html
# {% %} conditions for loops
# {# #} this is for comments

from flask import Flask, render_template, request, redirect, url_for

# initializing the app
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to the start page'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'passed'
    else:
        res = 'failed'
    
    return render_template('results.html', results = score)

# variable run example2 
@app.route('/successexp/<int:score>')
def successexp(score):
    res = ''
    if score >= 50:
        res = 'passed'
    else:
        res = 'failed'
    
    exp = {'score': score, 'res': res}
    return render_template('results1.html', results = exp)

#if condition
@app.route('/sucessif/<int:score>')
def successif(score):
    return render_template('results.html', results = score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('results.html', results = score)

@app.route('/submit', methods = ['GET','POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])

        total_score = (science + maths + c) / 3

    else:
        return render_template('getresults.html')
    return redirect(url_for('successexp', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
