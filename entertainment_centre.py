#import module(media) which contained 'class Movie' and fresh_tomatoes module.
import fresh_tomatoes
import media

#List of movies (instances) created.
man_infinity = media.Movie("The Man Who Knew Infinity",
                           "The biographical film about Ramanujan, an extra-ordinary mathematician who made a great breakthrough in pure Mathematics.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d8/The_Man_Who_Knew_Infinity_%28film%29.jpg",
                           "https://www.youtube.com/watch?v=oXGm9Vlfx4w")
Bilal_animated = media.Movie("Bilal: A New Breed of Hero",
                             "The historic biographical film about a black slave who rose and become one of the prominence figure in Islamic history.",
                             "http://t0.gstatic.com/images?q=tbn:ANd9GcTdxw63--qufzVji5uw5_-Fe0gQjLOW_VwNBxaGSojcVyAKgioS",
                             "https://www.youtube.com/watch?v=9l1x6TbwMXc")
Inception = media.Movie("Inception",
                        "A sci-fi movie about the theory of planting and extracting ideas through the dreams of dreamer.",
                        "https://vignette.wikia.nocookie.net/inception/images/f/f0/Wikia-Visualization-Main.png/revision/latest?cb=20130802174204",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

Bhajrangi = media.Movie("Bajrangi Bhaijaan",
                        "A 5-year-old Pakistani girl was separated from her mother and lost in India. Now, it's up to Pawan (Salman Khan) to bring her back home.",
                         "https://upload.wikimedia.org/wikipedia/en/d/dd/Bajrangi_Bhaijaan_Poster.jpg",
                         "https://www.youtube.com/watch?v=vyX4toD395U")
            
Sang_pencerah = media.Movie("The Enlightener: The Truth will Prevail",
                              "The historical biography film about the struggle of a group of young man to develop and progress the hearts and minds of under-privileged society",
                            "https://upload.wikimedia.org/wikipedia/en/d/d5/Sang_Pencerah_poster.jpg",
                             "https://www.youtube.com/watch?v=m7AcS7K6plw")
interstellar = media.Movie("Interstellar",
                            "A father left his beloved family and embarked the journey to the space to save mankind from extinction",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                            "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

#Group all movies_data instances in variable called movies.
movies = [man_infinity,Bilal_animated,Sang_pencerah,Inception,Bhajrangi,interstellar]

#call open_movies_page function within fresh_tomatoes module.
fresh_tomatoes.open_movies_page(movies)


