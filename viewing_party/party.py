# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    for key, value in new_movie.items():
        if value == None:
            return None

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    add_movie = user_data
    return add_movie

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    watch_list = user_data
    return watch_list

# def watch_movie():


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

