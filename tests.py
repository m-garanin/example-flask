#!/usr/bin/env python
import unittest
from example_app import * 
import tw_api

class AppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    
    def test_web(self):
        resp = self.app.get('/')
        assert(resp.status_code == 200)

    def test_rest(self):
        resp = self.app.get('/api/tweets/top')
        assert(resp.status_code == 200)
        assert( resp.content_type == 'application/json' )
        
    def test_tw_api(self):
        # auth
        tks = tw_api.get_authtokens()
        assert(type(tks) == dict)
        assert(tks.get('token_type') == 'bearer')
        print tks
        
        # top-tweets
        res = tw_api.get_toptweets('Spiderman', tks['access_token'])
        

if __name__ == '__main__':
    unittest.main()

