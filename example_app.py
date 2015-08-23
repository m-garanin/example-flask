#!/usr/bin/env python
from flask import Flask, jsonify

import tw_api


app = Flask(__name__)

@app.route('/')
def index():
    return 'index.html'


@app.route('/api/tweets/top')
def toptweets():
    res = {}
    return jsonify(res)



if __name__ == "__main__":
    app.run()
