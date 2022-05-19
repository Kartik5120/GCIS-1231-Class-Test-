"""Create a class called Movie with the following attributes and behaviour:

The movie name
The movie year
A random rating between 1 – 5. You need to import random for this part.
Create a constructor and accessor methods for each attribute
Add the ability to get a string representation of the movie, which includes all attributes when a movie is printed.
Use best practice like private variables etc.

Create a main method containing the following:

At least 3 movie objects (the attribute values can be hardcoded – no user input is required)
Store the movie objects into a data structure that will allow constant time lookups by movie name.
Hint: the movie name is the key, and the movie object is the value.

Create and call a function called select_movie that accepts the data structure containing the movies as a parameter,
displays all the movie names to the screen, and asks the user to choose one. Then display all attributes of the chosen
movie to the screen, or an error message if the movie doesn't exist."""

import random

class Movie:

    __slots__ = ["__name", "__year", "__rating"]

    def __init__(self, name):
        self.__name = name
        self.__year = 0
        self.__rating = random.randint(1, 6)

    def input():
        movie_name = float(input("Enter the name of the Movie: "))


def main():
    print(Movie.input)

main()    