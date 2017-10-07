import fresh_tomatoes #Reference html programming.
import media #Reference movie classes.

#Setup for movie title, description, poster_image, & trailer.

the_green_mile = media.Movie("The Green Mile",
                        "A movie about a magical deathrow inmate",
                        "https://upload.wikimedia.org/wikipedia/en/c/ce/Green_mile.jpg",
                        "https://youtu.be/ctRK-4Vt7dA")
#print (the_green_mile.storyline)


enter_the_dragon = media.Movie("Enter the Dragon",
                     "Brue Lee Martial Arts Movie",
                    "https://upload.wikimedia.org/wikipedia/en/e/ef/Enter_the_dragon.jpg",
                     "https://youtu.be/tB-QGOChuQc")
#print(enter_the_dragon.storyline)
#enter_the_dragon.show_trailer()

cars = media.Movie("Cars",
                   "Cartoon about cars",
                   "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
                   "https://www.youtube.com/watch?v=SbXIj2T-_uk")
#cars.show_trailer()
#print (cars.storyline)

the_accountant = media.Movie("The Accountant",
                   "The acountant assasin",
                   "https://upload.wikimedia.org/wikipedia/en/e/e4/The_Accountant_%282016_film%29.png",
                   "https://youtu.be/DBfsgcswlYQ")
#the_accountant.show_trailer()
#print (the_accountant.storyline)

austin_powers = media.Movie("Austin Powers",
                   "Spoof on James Bond",
                   "https://upload.wikimedia.org/wikipedia/en/d/d7/Austin_Powers_International_Man_of_Mystery_theatrical_poster.jpg",
                   "https://youtu.be/5vsANcS4Ml8")
#the_accountant.show_trailer()
#print (austin_powers.storyline)

django = media.Movie("Django",
                   "Escaped Slaved who turns in to a bounty hunter",
                   "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                   "https://youtu.be/6pKZbJHa17c")

movies = [the_green_mile, enter_the_dragon, cars, the_accountant, austin_powers, django]

# Uses list of movie instances as input to generate an HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

#This prints out the description of the class Movie.
print(media.Movie.__doc__)

#print(media.Movie.__name__)
#print(media.Movie.__module__)
