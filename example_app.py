#!/usr/bin/env python
import json, urllib

from flask import Flask, jsonify, send_from_directory, request
from werkzeug.contrib.cache import SimpleCache

import tw_api


app = Flask(__name__, static_url_path='')
cache = SimpleCache() 


@app.route('/')
def index():
    return send_from_directory('','index.html')


@app.route('/api/tweets/top')
def toptweets():
    """  
    request: /GET  /api/tweets/top?q=Query 

    response:  200, { tweets:[tweet] }   |  400, {reason:"error message"}
    """
    q = request.args.get('q', '')
    if not q:
        return err("Empty query is not valid")
     
    token = get_token()
    status, res = tw_api.get_toptweets(token, q)
    if status != 200:
        return err(res)

    return jsonify(dict(tweets=res))

    
def get_token():
    "wrapper for cache twitter auth-token"
    key = 'tw-token'
    tk = cache.get(key)
    if not tk:
        tk = tw_api.get_authtoken()
        cache.set(key, tk, timeout=10*60) 
    return tk
    

def err(reason):
    r = jsonify(dict(reason=reason))
    r.status_code = 400
    return r


if __name__ == "__main__":
    app.run()
