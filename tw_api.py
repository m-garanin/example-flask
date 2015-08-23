import httplib, urllib, base64, json


TW_API_URL = 'api.twitter.com'
TW_AUTH = ('9sso4SCHh9UUSKrMHB4mdSnxl', 'aQCb9CfAkxBale4XI9YfWgnW8AJ9CxgRcgNYT9HSsDR8ScqBOV')

def get_authtokens():
    "return dict or None"
    conn = httplib.HTTPSConnection(TW_API_URL)
    headers = {'Authorization': 'Basic %s' % base64.b64encode(':'.join(TW_AUTH)), 
               'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    
    conn.request('POST', '/oauth2/token', 'grant_type=client_credentials', headers)
    resp = conn.getresponse()
    assert(resp.status == 200)
    body = resp.read()
    conn.close()
    return json.loads(body)
    

def get_toptweets(q, token):
    "return list"
    conn = httplib.HTTPSConnection(TW_API_URL)
    headers = {'Authorization': 'Bearer %s' % token} 
    params = {'q':q, 'result_type':'popular'}
    conn.request('GET', '/1.1/search/tweets.json?' + urllib.urlencode(params), headers=headers)
    resp = conn.getresponse()
    print resp.status, resp.reason
    assert(resp.status == 200)
    body = resp.read()
    print body
    
