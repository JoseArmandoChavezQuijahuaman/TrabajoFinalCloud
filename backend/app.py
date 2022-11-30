from flask import Flask, render_template, request
from flask_cors import CORS
import os
import socket
import subprocess

app = Flask(__name__)

@app.route("/api", methods=['POST'])
def handle():
    data1 = {"josecin:": 123123}

    values = request.form.get('code', "")
    code = request.form.get("code", "")
    filename = request.form.get("filename", "")
    extension = request.form.get("extension", "")


    if not os.path.exists("temp"):
        os.makedirs("temp")
    FILE = "temp/{}.{}".format(filename, extension)
    with open(FILE, "+w") as File:
        File.write(code)
        execution = subprocess.Popen(
            ["python3", FILE],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=0,
        )

    while execution.poll() is None:
        pass
    if execution.poll() == 1:
        response = {"output": execution.stderr.readlines()}
        os.remove(FILE)
        return response, 406
        

    response = {"output": execution.stdout.readlines()}
    os.remove(FILE)
    return response, 200

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=3005)

