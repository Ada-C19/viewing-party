# ------------- WAVE 1 --------------------
import copy
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating    }
    return movie    

def add_to_watched(user_data, movie):
    user_data_copy = copy.deepcopy(user_data)
    user_data_copy["watched"].append(movie)
    return user_data_copy

def add_to_watchlist(user_data, movie):
    user_data_copy = copy.deepcopy(user_data)
    user_data_copy["watchlist"].append(movie)
    return user_data_copy

def watch_movie(user_data, title):
    user_data_copy = copy.deepcopy(user_data)
    in_watchlist = False
    movie_index = 0
    for movie in user_data_copy["watchlist"]:
        if movie["title"] == title:
            in_watchlist = True
            break
        movie_index += 1
    if not in_watchlist:
        return user_data_copy
    movie = user_data_copy["watchlist"][movie_index]
    del user_data_copy["watchlist"][movie_index]
    user_data_copy["watched"].append(movie)
    return user_data_copy


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

