# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    static_keys = ["title", "genre","rating"]
    inputs = [title, genre, rating]
    if (type(title)) is str and (type(genre)) is str and (type(rating)) is float:
        new_movie = {k:v for k, v in zip(static_keys, inputs)}
    else:
        return None
    
    return new_movie

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data
    


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

