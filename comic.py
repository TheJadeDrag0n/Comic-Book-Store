from bottle import run, route, view, get, post, request, static_file
from itertools import count



class Comic:

    _ids = count(0)

    def __init__(self, name, stock, image):

        self.id = next(self._ids)
        self.name = name
        self.stock = stock
        self.comic_cover = image



#test data
comics = [
    Comic("Super Dude", 8, "super_dude.jpg"),
    Comic("Lizard Man", 12, "war.png"),
    Comic("Water Woman", 3, "cosmic.jpg")
    ]


#Pages

#index
@route("/")
@view("index")
def index():

    pass

#test page
@route("/comic")
@view("comic")
def comic():
    
    data = dict (comics_list=comics)
    return data    
    


#pics
@route('/pictures/<filename>')
def serve_picture(filename):
    return static_file(filename, root='./images')



run(host='0.0.0.0',port = 8080, reloader=True, debug=True)