from bottle import run, route, view, get, post, request, static_file
from itertools import count



class Comic:

    _ids = count(0)

    def __init__(self, image, name, stock):

        self.id = next(self._ids)
        self.name = name
        self.stock = stock
        self.comic_cover = image



#test data
comics = [
    Comic("super_dude.jpg", "Super Dude", 8),
    Comic( "war.png", "Lizard Man", 12),
    Comic("cosmic.jpg", "Water Woman", 3)
    ]





#Pages

#index
@route("/")
@view("index")
def index():

    pass

#comic
@route("/comic")
@view("comic")
def comic():
    
    data = dict (comics_list=comics)
    return data    


@route("/comic-success/<comic_id>")
@view("comic-success")
def comic_success(comic_id):
    
    comic_id = int(comic_id)
    found_comic = None
    for comic in comics:
        if comic.id == comic_id:
            found_comic = comic
    data = dict (comic = found_comic)
    found_comic.stock = found_comic.stock - 1
    return data


    
#test
@route("/test")
@view("test")
def test():
    
    pass




#pics
@route('/pictures/<filename>')
def serve_picture(filename):
    return static_file(filename, root='./images')



run(host='0.0.0.0',port = 8080, reloader=True, debug=True)