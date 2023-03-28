# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
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
    user_data["watched"] = watched_list
    return user_data


def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    user_data["watchlist"] = watchlist
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched_list = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            watched_list.append(movie)
            user_data["watchlist"] = watchlist
            user_data["watched"] = watched_list
            break
    return user_data
    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    avg_list = [movie["rating"] for movie in watched]
    if len(avg_list) == 0:
        return 0
    avg_rating = sum(avg_list) / len(avg_list)
    return avg_rating


def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    genre_freq = [movie["genre"] for movie in watched]
    if genre_freq == []:
        return None
    return max(set(genre_freq), key=genre_freq.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

