from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")
@app.route('/derbare')
def derbare():
    return render_template('derbare.html')
@app.route("/chaky")
def lekdany():
    yekem = "chony"
    dwem = "bashy"
    koke = yekem + dwem
    return render_template('chaky.html', koke=koke)