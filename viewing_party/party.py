# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # validate_parameters (empty strings and zero evaluate to Falsy)
    if title and genre and rating:
        movie = {"title": title, "genre": genre, "rating": rating}
        return movie
    else:
        return None
    
user_data = {"watched": [], "watchlist": []}

def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
        return user_data

def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
        return user_data

def watch_movie(user_data, title):
    pass

    # user_data = dictionary with 'watchlist' and 'watched': 
        # watchlist and watched represent that the user has a watchlist (<---is this a list as well?) 
        # and a list of watched movies.

        # title = str; represents the title of the movie the user has watched
    
    # if title in user's watchlist:
        # remove that movie from the watchlist
        # add that movie to watched
        # return user_data
    # elif not title in user's watchlist:
        #return user_data

# ****** Waves 2, 3, 4, 5: should not modify user_data ******










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

