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

    if not isinstance(title, str) or not title:
        return user_data
    
    # if title in watchlist, remove from watchlist, add to watched
    movies_watched = user_data["watched"]
    movies_to_watch = user_data["watchlist"]

    movie_to_move = None
    for movie in movies_to_watch:
        if title in movie["title"]:
            # movie_to_move = movie[]
            print("title exists")

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

