import media
import fresh_tomatoes


# Initializes movie - Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys coming to life",
                        "https://vignette4.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742", #noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Initializes movie - Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246", #noqa
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# Initializes movie - Doubt
doubt = media.Movie("Doubt",
                    "Sister Aloysius begins a personal crusade against the priest -- despite her lack of evidence.", #noqa
                    "https://troyster90.files.wordpress.com/2014/04/doubt-poster.jpeg", #noqa
                    "https://www.youtube.com/watch?v=Ad8gw-Qdjj8")

# Stores the movies in an array
movies = [toy_story, avatar, doubt]

# Initiates the opening of the html page with the above movies
fresh_tomatoes.open_movies_page(movies)
