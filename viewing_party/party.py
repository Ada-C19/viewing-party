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

# Barbara
def get_watched_avg_rating(user_data):
    sum_rating = 0
    watched_movies = user_data["watched"]
    if len(watched_movies) == 0: return 0.0
    for movie in watched_movies:
        sum_rating += movie["rating"]
    average_rating = sum_rating / len(watched_movies)
    return average_rating


# Alycia
def get_most_watched_genre(janes_data):
    pass
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# ------------------z-----------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
