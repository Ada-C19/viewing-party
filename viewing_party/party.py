import statistics 
from statistics import mode 

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    input: title, genre, rating
    output: dictionary with the three keys "title", "genre", and "rating"
    """
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

    return None 


def add_to_watched(user_data, movie):
    """
    input: user_data dictionary with nested list as values, movie dictionary
    output: updated user_data dictionary 
    """

    user_data["watched"].append(movie) 

    return user_data
    

def add_to_watchlist(user_data, movie):
    """
    input: user_data dictionary, and movie dictionary
    output: updated user_data dictionary
    """

    user_data["watchlist"].append(movie) 

    return user_data

# The data below is for testing function watch_movie()
# user_data = {
#     "watchlist": [
#         {"title": "Land Before Time"},
#         {"title": "Spirited Away"}
#     ],
#     "watched": [
#             {"title": "Lord of the Rings"},
#             {"title": "Parasyte"},
#             {"title": "Harry Potter"},
#             {"title": "Ready Player One"}
#     ]
# }

# title = 'Land Before Time'

def watch_movie(user_data, title):
    """
    input: user_data dictionary, and title string
    output: updated user_data dictionary 
    """ 

    for movie in user_data["watchlist"]:
        print(movie, 'here')
        print(title, "lll")
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    
    return user_data

# watch_movie(user_data, title)


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: average rating float
    """

    average_rating = 0.0
    movie_ratings = [] 

    for watched in user_data["watched"]:
        rating = watched["rating"]
        movie_ratings.append(rating)
    
    sum_of_movie_ratings = sum(movie_ratings)
    length_of_movie_ratings = len(movie_ratings)
    if length_of_movie_ratings == 0:
        return average_rating
    average_rating = sum_of_movie_ratings/length_of_movie_ratings

    return average_rating



def get_most_watched_genre(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: genre string
    """

    most_frequently_watched_genre = None
    movie_genres = []

    for watched in user_data["watched"]:
        genre = watched["genre"]
        movie_genres.append(genre)
    if len(movie_genres) == 0:
        return None

    most_frequently_watched_genre = (mode(movie_genres))
    return most_frequently_watched_genre




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: list of dictionaries (which represents list of movies)
    """

    user_watched_list = []
    friends_watched_list = []
    movies_user_watched_that_friends_didnt_watch = []
    movies_watched_by_all = []
    # unique_movies_dict = {}
    

    for friend in user_data["friends"]:
        # value_is_list_of_dicts = friend[0]["watched"]
        for movie in friend["watched"]:
            movie_title = movie["title"]
            friends_watched_list.append(movie_title)

    print(friends_watched_list)
    # return friends_watched_list


    for user in user_data["watched"]:
        value_is_list = user["title"]
        user_watched_list.append(value_is_list)


    for movie in user_watched_list: 
        if movie in friends_watched_list:
            movies_watched_by_all = {movies_user_watched_that_friends_didnt_watch}
        if movie not in friends_watched_list:
            movies_user_watched_that_friends_didnt_watch.append(movie)
            movies_user_watched_that_friends_didnt_watch = {movies_user_watched_that_friends_didnt_watch}


            return movies_user_watched_that_friends_didnt_watch



    # return user_watched_list




        # friends_watched_list = user_data["watched"]["title"]

        # user_data["title"]


    # for watched in user_data






def get_friends_unique_watched(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: list of dictionaries (which represents list of movies)
    """


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """
    input: user_data dictionary with field "subscriptions", value of "subscriptions" is list of strings
    output: recommended movies list
    """

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    input: user_data dictionary 
    output: recommended movies list
    """


def get_rec_from_favorites(user_data):
    """
    input: user_data dictionary with field "favorites", value of "favorites" is a list of movie dictionaries
    output: recommended movies list
    """