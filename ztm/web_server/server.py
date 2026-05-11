from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

# flask --app server run --debug  (To run the server)

@app.route("/blog")
def blog():
    return "<p>These are my thoughts on blogs.</p>"