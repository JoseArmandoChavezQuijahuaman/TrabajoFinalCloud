from flask import Flask, render_template
import os
import socket
import subprocess

app = Flask(__name__)

@app.route("/")
def handle():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)