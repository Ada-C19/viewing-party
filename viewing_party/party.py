# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    Function creates a movie dictionairy
    '''
    if title is None or genre is None or rating is None:
        return None
    return {"title": title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    '''
    Function appends movie dictionairy to user_data "watched" list
    '''
    user_data["watched"].append(create_movie(movie["title"], movie["genre"], movie["rating"]))
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Function appends movie dictionairy to user_data "watchlist" list
    '''
    user_data["watchlist"].append(create_movie(movie["title"], movie["genre"], movie["rating"]))
    return user_data

def watch_movie(user_data, title):
    '''
    Function moves a movie from user_data "watchlist" list to "watched" list
    '''


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

