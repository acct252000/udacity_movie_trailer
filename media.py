

# media.py created November 15, 2016 by Christine Stoner

__copyright__ = """

    Copyright 2016 Christine Stoner

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
__license__ = "Apache 2.0"


# Imports python file that launches the web browser

import fresh_tomatoes

# Creates Movie class which contains title, poster image from wikepedia,
# and youtube url of movie trailer
# Explictly inherits from object based on google style guide

class Movie(object):
    """Lists title, poster image, and YouTube url of movies

    Attributes:
        title: string movie title
        poster_image_url: jpg reference of movie poster
        trailer_youtube_url:  url of youtube trailer
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Initializes the Movie class.

        Args:
            title: string movie title
            poster_image_url: jpg reference of movie poster
            trailer_youtube_url: url of youtube movie trailer
        """  

        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


# Create five movies

the_accountant = Movie("The Accountant", 
                       "img/accountant.jpg", 
                       "https://www.youtube.com/watch?v=DBfsgcswlYQ"
                       )

tarzan = Movie("The Legend of Tarzan",
               "img/tarzan.jpeg", 
               "https://www.youtube.com/watch?v=dLmKio67pVQ"
               )

dr_strange = Movie("Doctor Strange",
                   "img/drstrange.jpeg", 
                   "https://www.youtube.com/watch?v=HSzx-zryEgM"
                   )

moana = Movie("Moana",
              "img/moana.jpg",  
              "https://www.youtube.com/watch?v=LKFuXETZUsI"
              )

arrival = Movie("Arrival",
                "img/arrival.jpeg",
                "https://www.youtube.com/watch?v=AMgyWT075KY"
                )

# Populate movies array with movies created

movies = [the_accountant, tarzan, dr_strange, moana, arrival]

# Launch website



if __name__ == '__main__':
    fresh_tomatoes.open_movies_page(movies)
    


