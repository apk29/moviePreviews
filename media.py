import webbrowser

class Movie():
#The print Movie.__doc__ is on the entertainment_center.py file 
    """This blass provides a way to store movie related inforamtion"""
 
    VALID_RATINGS = ["G","PG","PG-13","R"]

#This function initializes the title, storyline, poster images, & the trailer.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    

#This allows the python to open up the trailer in a webbrowser.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
