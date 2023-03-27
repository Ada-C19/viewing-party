# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not title or not genre or not rating:
        return None
        
    movie = {
        "title": title, 
        "genre": genre,
        "rating": rating
    }
    return movie

def add_to_watched(user_data, movie):

    # Check movie isn't empty and is a dictionary
    # Try to add movie to watched, otherwise give error message
    if movie and isinstance(movie, dict):
        try:
            user_data["watched"].append(movie)
        except KeyError:
            print("'Watched' key does not exist; could not add movie")
    
    return user_data

def add_to_watchlist(user_data, movie):

    # Check movie isn't empty and is a dictionary
    # Try to add movie to watchlist, otherwise give error message
    if movie and isinstance(movie, dict):
        try:
            user_data["watchlist"].append(movie)
        except KeyError:
            print("'Watchlist' key does not exist; could not add movie")
    
    return user_data

def watch_movie(user_data, title):

    # Check title is a string and not empty, otherwise return user_data
    if not isinstance(title, str) or not title:
        return user_data

    # Check if movie with title in watchlist
    # If it is, append movie to watched and remove from watchlist
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

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

