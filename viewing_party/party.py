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
    

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    for user in user_data["watched"]:
        user_watched_list.append(user)


    for movie in user_watched_list: 
        if movie not in friends_watched_list:
            movies_user_watched_that_friends_didnt_watch.append(movie)
            

    return movies_user_watched_that_friends_didnt_watch




def get_friends_unique_watched(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: list of dictionaries (which represents list of movies)
    """
    user_watched_list = []
    friends_watched_list = []
    movies_friends_watched_that_user_didnt_watch = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    for user in user_data["watched"]:
        user_watched_list.append(user)

    for movie in friends_watched_list:
        if movie not in user_watched_list and movie not in movies_friends_watched_that_user_didnt_watch:
            movies_friends_watched_that_user_didnt_watch.append(movie)

    return movies_friends_watched_that_user_didnt_watch




# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """
    input: user_data dictionary with field "subscriptions", value of "subscriptions" is list of strings
    output: recommended movies list
    """
    # services_user_has_access_to = []
    # friends_streaming_services = []
    # movies_user_hasnt_watched = []
    # recommended_movies = []

    # # for element in user_data["subscriptions"]:
    # # streaming services the user has access to 
    # services_user_has_access_to.append(user_data["subscriptions"])


    # # streaming services friends host/have 
    # for friend in user_data["friends"]:
    #     for watched_movie in friend["watched"]:
    #         friends_streaming_services.append(watched_movie["host"])

    # # at least one friend has watched, user has not watched it -> use return statement from function get_friends_unique_watched
    # movies_user_hasnt_watched = get_friends_unique_watched(user_data)

    # # check if
    # if friends_streaming_services in services_user_has_access_to:

    #     return recommended_movies

    rec_movies = []

    for friend in user_data["friends"]:
            for watched_movie in friend["watched"]:
                if watched_movie["host"] in user_data["subscriptions"] and watched_movie not in user_data["watched"]:
                    rec_movies.append(watched_movie)
            return rec_movies







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