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
    if not len(user_data["watched"]):
        return 0.0
    ratings = [movie["rating"] for movie in user_data["watched"]]
    return statistics.mean(ratings)

def get_most_watched_genre(user_data):
    if not len(user_data["watched"]):
        return None
    genres = [movie["genre"]for movie in user_data["watched"]]
    return mode(genres)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_movies = get_user_movies(user_data)
    friend_movies = get_friends_movies(user_data)
    return [movie for movie in user_movies if movie not in friend_movies]

def get_friends_unique_watched(user_data):
    user_movies = get_user_movies(user_data)
    friend_movies = get_friends_movies(user_data)
    unique_movies = []
    for movie in friend_movies:
        if movie not in user_movies and movie not in unique_movies:
            unique_movies.append(movie)
    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended = []
    friends_watched = get_friends_unique_watched(user_data)
    for movie in friends_watched:
        if movie not in user_data["watched"]:
            if movie["host"] in user_data["subscriptions"] and movie not in recommended:
                recommended.append(movie)
    return recommended


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended = []
    if not len(user_data["watched"]):
        return recommended
    
    genres = [movie["genre"] for movie in user_data["watched"]]
    genre = mode(genres)
    friends_watched = get_friends_unique_watched(user_data)
    for movie in friends_watched:
        if movie["genre"] == genre and movie not in user_data["watched"] and movie not in recommended:
            recommended.append(movie)
    return recommended

def get_rec_from_favorites(user_data):
    friends_watched = get_friends_movies(user_data)
    return [movie for movie in user_data["favorites"] if not movie in friends_watched]

# -----------------------------------------
# -------- HELPER FUNCTIONS ---------------
# -----------------------------------------

def get_user_movies(user_data):
    return [movie for movie in user_data["watched"]]

def get_friends_movies(user_data):
    friend_movies = [] 
    for friend_dict in user_data["friends"]:
        for movie in friend_dict["watched"]:
            friend_movies.append(movie)
    return friend_movies
