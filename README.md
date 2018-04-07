# Movie_Project
**Movie_Project** is the python programmes that is used to create a websites for a list of movies. The user can create a website and update a new movies informations. The information includes movies's title, a brief storyline, poster image and a link to movie's trailer.

## Installation
The requirements to run Movie_Project were as follow:
* Install Python IDLE 2.7.14. The installer can be downloaded [here](https://www.python.org/downloads/).

## Movie_Project guidelines
There are three files
```
entertainment_centre.py 
media.py
fresh_tomatoes.py
```
media.py file contain the _class_ created (in this case, **class Movie**). The codes were as follow (Within ``` media.py ```):

```
 def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube
```

If the user wants to store/update a new movies informations, create a new instance within entertainment_centre.py (The code below set as an example):

```
Man_infinity = media.Movie("The Man Who Knew Infinity",
                           "The biographical film about Ramanujan, an extra-ordinary mathematician who made a great breakthrough in pure    Mathematics.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d8/The_Man_Who_Knew_Infinity_%28film%29.jpg",
                           "https://www.youtube.com/watch?v=oXGm9Vlfx4w")
```
Then, group all the instances (movies) in a variable. The codes below set as the example:
```
movies = [man_infinity,Bilal_animated,Sang_pencerah,Inception,Bhajrangi,interstellar]
```
For the fresh_tomatoes.py, it contains the code to build a websites. Therefore, this module was imported into entertainment_centre.py and the function ``` fresh_tomatoes.open_movies_page(movies) ``` was called in entertainment_centre.py.

## How to run Movie_Project

Open Python IDLE, then open ```entertainment_centre.py``` and run the module. The movie website will open by the default browser.

## License

Movie_Project is not under any license and is opened to public.

Thank You.
