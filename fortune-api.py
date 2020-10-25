import subprocess
import json
import datetime

from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route('/')
def fortune():

  return_dict = {
    'generated': datetime.datetime.utcnow(),
    'fortune': subprocess.check_output(["fortune"]).decode('utf-8'),
    'username': request.headers.get('X-Username')
  }

  return jsonify(return_dict)

if __name__ == '__main__':
    app.run('0.0.0.0')