from flask import Flask, render_template, request, session, redirect


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
    if 'user' not in session:
        session["counter"]=0
    else:
        session["counter"]+= 1
    return render_template("index.html")


@app.route('/twice', methods=['POST'])
def twice():
    session ['user'] = request.form['name']
    return redirect("/")


@app.route('/counter', methods=['POST'])
def counter():
    session["counter"]+= 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')
    

# form_test/server.py
# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     # Here we add two properties to session to store the name and email
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')


# form_test/server.py
# @app.route('/show')
# def show_user():
#     return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

# Session in Templates

# @app.route('/show')
# def show_user():
#     return render_template('show.html')







if __name__=="__main__":
    app.run(debug=True)