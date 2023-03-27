# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None

    movie = {
        "title" : title, 
        "genre" : genre, 
        "rating" : rating
    }

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    new_user_data = {
        "watchlist" : user_data["watchlist"].copy(),
        "watched" : user_data["watched"].copy()
    }
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            new_user_data["watchlist"].remove(movie)
            new_user_data["watched"].append(movie)

    return new_user_data

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

