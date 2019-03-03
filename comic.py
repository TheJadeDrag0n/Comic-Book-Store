from bottle import run, route, view, get, post, request
from itertools import count



class Thing:


    _ids = count(0)

    def __init__():

        self.id = next(self._ids)






#Pages

#index
@route("/")
@view("index")
def index():

    pass


run(host='0.0.0.0',port = 8080, reloader=True, debug=True)