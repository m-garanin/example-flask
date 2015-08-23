# example-flask
It exposes a restful api that pulls the top tweets from twitter.

API:
    request: /GET  /api/tweets/top?q=Query 

    response:  200, { tweets:[tweet] }   |  400, {reason:"error message"}
