import httplib, urllib, base64, json


TW_API_URL = 'api.twitter.com'
TW_AUTH = ('9sso4SCHh9UUSKrMHB4mdSnxl', 'aQCb9CfAkxBale4XI9YfWgnW8AJ9CxgRcgNYT9HSsDR8ScqBOV')

def get_authtoken():
    "return token"
    conn = httplib.HTTPSConnection(TW_API_URL)
    headers = {'Authorization': 'Basic %s' % base64.b64encode(':'.join(TW_AUTH)), 
               'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    
    conn.request('POST', '/oauth2/token', 'grant_type=client_credentials', headers)
    resp = conn.getresponse()
    assert(resp.status == 200)
    data = json.loads(resp.read())
    conn.close()
    assert( data['token_type'] == 'bearer')
    return data['access_token']
    

def get_toptweets(token, q):
    "return (200, tweets) | (error_status, reason)"
    conn = httplib.HTTPSConnection(TW_API_URL)
    headers = {'Authorization': 'Bearer %s' % token} 
    params = {'q':q, 'result_type':'popular'}
    conn.request('GET', '/1.1/search/tweets.json?' + urllib.urlencode(params), headers=headers)
    resp = conn.getresponse()
    if resp.status != 200:
        return (resp.status, resp.reason)
        
    data = json.loads(resp.read())
    conn.close()
    return (200, data['statuses'])
    
