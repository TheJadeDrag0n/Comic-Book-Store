from bottle import run, route, view, get, post, request
from itertools import count



class Comic:

    _ids = count(0)

    def __init__(self, name, stock):

        self.id = next(self._ids)
        self.name = name
        self.stock = stock




#test data
comics = [
    Comic("Super Dude", 8),
    Comic("Lizard Man", 12),
    Comic("Water Woman", 3)
    ]


#Pages

#index
@route("/")
@view("index")
def index():

    pass


run(host='0.0.0.0',port = 8080, reloader=True, debug=True)