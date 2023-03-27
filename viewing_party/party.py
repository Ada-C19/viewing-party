MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    input: title, genre, rating
    output: 
    '''
    if not title or genre or rating:
        return None
    movie_dict = {"title":"", "genre":"", "rating":""}
    return movie_dict

def add_to_watched(user_data, movie):
    #user_data is a dict with key "watched"
    movies_user_has_watched = user_data["watched"]
    # a list of dicts rep the movies the user has watched
    # append (represent) movie to list of dict
    movies_user_has_watched.append(movie)
    #add movie to the "movies_user_has_watched" inside of user data

    return user_data

def add_to_watchlist(user_data, movie):
    pass

def watch_movie(user_data, title):
    pass



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

