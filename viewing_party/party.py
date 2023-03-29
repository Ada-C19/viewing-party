import statistics
from statistics import mode
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
    for movie in user_data["watchlist"]:
        if title != movie["title"]:
            continue
        elif movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
        
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating = 0.0
    count = 0
    if not len(user_data["watched"]):
        return rating
    for movie in user_data["watched"]:
        rating += movie["rating"]
        count += 1
    avg_rating = rating / count
    return avg_rating

def get_most_watched_genre(user_data):
    genres = []
    if not len(user_data["watched"]):
        return None
    for movie in user_data["watched"]:
        genres.append(movie["genre"])
    return mode(genres)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_movies = [movie for movie in user_data["watched"]]
    friend_movies = [movie for friend_dict in user_data["friends"] for movie in friend_dict["watched"]]
    unique_movies = [movie for movie in user_movies if movie not in friend_movies]
    return unique_movies

def get_friends_unique_watched(user_data):
    user_movies = [movie for movie in user_data["watched"]]
    friend_movies = [movie for friend_dict in user_data["friends"] for movie in friend_dict["watched"]]
    unique_movies = []
    for movie in friend_movies:
        if movie not in user_movies and movie not in unique_movies:
            unique_movies.append(movie)
    # unique_movies = [movie for movie in friend_movies if movie not in user_movies and movie not in unique_movies]

    # unique_movies = dict.fromkeys(unique_movies)
    return unique_movies



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

