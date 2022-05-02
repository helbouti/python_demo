import ssl
from flask import Flask,render_template


app=Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")


app.run(host="0.0.0.0", port="5000", debug=True,)