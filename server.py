from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key= 'qwerty'
@app.route('/')
def index():
    if 'count' not  in session:
        session['count'] =0
    else:
        session['count'] +=2
    return render_template('index.html', count = session['count'])


@   app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":    
    app.run(debug=True)  