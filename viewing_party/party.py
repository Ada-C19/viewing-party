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

    # need .round() in order to return float instead of int?

    average_rating = 0.0
    movie_ratings = []

    # if len(movie_ratings) == 0:
    #     return average_rating_list     

    for watched in user_data["watched"]:
        # print(watched)
        rating = watched["rating"]
        movie_ratings.append(rating)
        # if movie_ratings == 0:
        # if len(movie_ratings) == 0:

        # calculate_average_rating = sum(movie_ratings)/len(movie_ratings)
        # average_rating.append(average_rating)
        # length_of_movie_ratings_list = len(movie_ratings)
        # sum_of_movie_ratings_list = sum(movie_ratings)
        # average = sum_of_movie_ratings_list / length_of_movie_ratings_list
        # average_rating.append(average_rating)
        
        # return average_rating
    
    sum_of_movie_ratings = sum(movie_ratings)
    length_of_movie_ratings = len(movie_ratings)
    if length_of_movie_ratings == 0:
        return average_rating
    average_rating = sum_of_movie_ratings/length_of_movie_ratings

    return average_rating


# iterate through user data
    # for item in user_data.keys():
    #     user_data["watched"]["rating"]
        

    # for item in user_data: 
    #     for item in "watched":
    #         ["rating"]
    #     user_data["watched"]["rating"]
        # user_data["watched"]["rating"]


def get_most_watched_genre(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: genre string
    """


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: list of dictionaries (which represents list of movies)
    """

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