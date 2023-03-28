# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if None in (title, genre, rating):
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watch_list"]:
        if ["title"] == title:
            
            user_data["watched"].append(user_data["watchlist"][movie])
            return user_data
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

