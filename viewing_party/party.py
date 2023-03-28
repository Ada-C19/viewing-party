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



def add_to_watchlist(user_data, movie):
    """
    input: user_data dictionary, and movie dictionary
    output: updated user_data dictionary
    """


def watch_movie(user_data, title):
    """
    input: user_data dictionary, and title string
    output: updated user_data dictionary 
    """ 


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: average rating float
    """

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