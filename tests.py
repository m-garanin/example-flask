#!/usr/bin/env python
import unittest
from example_app import * 
import tw_api

class AppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    
    def test_web(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        

    def test_rest(self):
        # good case
        resp = self.app.get('/api/tweets/top?q=Batman')
        print resp.status_code
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json' )
        data = json.loads(resp.data)
        self.assertTrue(isinstance(data['tweets'], list) )
        
        # good case (after expired cache)
        cache.clear()
        resp = self.app.get('/api/tweets/top?q=Batman')
        print resp.status_code
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertTrue(isinstance(data['tweets'], list) )
        

        # bad case (without query)
        resp = self.app.get('/api/tweets/top')
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.content_type, 'application/json' )
        data = json.loads(resp.data)
        self.assertTrue(isinstance(data['reason'], unicode) )
        


    def test_tw_api(self):
        # auth
        token = tw_api.get_authtoken()
        self.assertTrue(token)
        print token
        
        # top-tweets
        res = tw_api.get_toptweets(token, 'New Spiderman')
        self.assertEqual(type(res), tuple)
        self.assertEqual(res[0], 200)
        self.assertTrue(isinstance(res[1], list))
        


if __name__ == '__main__':
    unittest.main()

