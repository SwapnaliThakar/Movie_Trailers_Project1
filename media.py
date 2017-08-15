import webbrowser


class Movie():
    """This class initializes the details of a
    movie and shows trailer as required

        movie_title (str): is the title of the movie
        movie_storyline (str): is the storyline of the movie
        poster_image (url): is the url from which to get the poster image
        trailer_youtube (url): is the url to the youtube trailer of the movie
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # initializes movie title
        self.title = movie_title
        # initializes storyline of the movie
        self.storyline = movie_storyline
        # initializes poster image
        self.poster_image_url = poster_image
        # initializes movie trailer url
        self.trailer_youtube_url = trailer_youtube

    # Shows trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
