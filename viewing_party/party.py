# ------------- WAV

def create_movie(title, genre, rating):
    movie_dictionary = {}
    if title and genre and rating:
        movie_dictionary["title"] = title
        movie_dictionary["genre"] = genre
        movie_dictionary["rating"] = rating
    else:
        return None
    
    return movie_dictionary

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    copy_user_data = user_data
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            copy_user_data["watched"].append(movie)
            copy_user_data["watchlist"].remove(movie)
        user_data = copy_user_data

    return user_data
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

