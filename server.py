from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if session['count']:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/plustwo')
def plusone():
    session['count'] +=1

    return redirect('/')
@app.route('/reset')
def reset():
    session['count'] = 0

    return redirect('/')


app.run(debug=True)
